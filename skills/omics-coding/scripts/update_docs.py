#!/usr/bin/env python3
"""Build local OmicVerse and SCOP Markdown docs plus function/parameter indexes."""

import argparse
import csv
import datetime as dt
import html
from html.parser import HTMLParser
import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
import time
from typing import Dict, Iterable, List, Optional, Tuple
from urllib.parse import urljoin
from urllib.request import Request, urlopen


ROOT = Path(__file__).resolve().parents[1]
REFERENCES = ROOT / "references"

OMICVERSE_INDEX = "https://omicverse.readthedocs.io/en/latest/api/user.html"
SCOP_INDEX = "https://mengxu98.github.io/scop/reference/index.html"
SCOP_MAN_API = "https://api.github.com/repos/mengxu98/scop/contents/man?ref=main"
SCOP_TARBALL = "https://api.github.com/repos/mengxu98/scop/tarball/main"
SCOP_REFERENCE_BASE = "https://mengxu98.github.io/scop/reference/"


class LinkParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.links = []  # type: List[Tuple[str, str]]
        self._href = None  # type: Optional[str]
        self._text = []  # type: List[str]

    def handle_starttag(self, tag, attrs):
        if tag == "a":
            attrs_dict = dict(attrs)
            href = attrs_dict.get("href")
            if href:
                self._href = href
                self._text = []

    def handle_data(self, data):
        if self._href is not None:
            self._text.append(data)

    def handle_endtag(self, tag):
        if tag == "a" and self._href is not None:
            text = clean_text("".join(self._text))
            self.links.append((self._href, text))
            self._href = None
            self._text = []


class MarkdownParser(HTMLParser):
    def __init__(self):
        super().__init__()
        self.parts = []  # type: List[str]
        self._heading = None  # type: Optional[int]
        self._in_pre = False
        self._in_code = False

    def handle_starttag(self, tag, attrs):
        if tag in {"h1", "h2", "h3", "h4"}:
            self._heading = int(tag[1])
            self.parts.append("\n" + "#" * self._heading + " ")
        elif tag in {"p", "div", "section", "dl"}:
            self.parts.append("\n")
        elif tag == "li":
            self.parts.append("\n- ")
        elif tag == "dt":
            self.parts.append("\n")
        elif tag == "dd":
            self.parts.append(" ")
        elif tag == "br":
            self.parts.append("\n")
        elif tag == "pre":
            self._in_pre = True
            self.parts.append("\n```text\n")
        elif tag == "code" and not self._in_pre:
            self._in_code = True
            self.parts.append("`")

    def handle_data(self, data):
        if not data:
            return
        if self._in_pre:
            self.parts.append(html.unescape(data))
        else:
            self.parts.append(clean_text(data) + " ")

    def handle_endtag(self, tag):
        if tag in {"h1", "h2", "h3", "h4"}:
            self.parts.append("\n")
            self._heading = None
        elif tag in {"p", "li", "dt", "dd"}:
            self.parts.append("\n")
        elif tag == "pre":
            self.parts.append("\n```\n")
            self._in_pre = False
        elif tag == "code" and self._in_code:
            self.parts.append("`")
            self._in_code = False


def clean_text(value):
    value = html.unescape(value)
    value = re.sub(r"\s+", " ", value)
    return value.strip()


def strip_tags(value):
    value = re.sub(r"<script.*?</script>", " ", value, flags=re.S | re.I)
    value = re.sub(r"<style.*?</style>", " ", value, flags=re.S | re.I)
    value = re.sub(r"<[^>]+>", " ", value)
    return clean_text(value)


def curl_fetch(url, pause, retries=3, max_time=20):
    last_error = None
    command = [
        "curl",
        "--http1.1",
        "--tlsv1.2",
        "-L",
        "--connect-timeout",
        "10",
        "--retry",
        "1",
        "--max-time",
        str(max_time),
        "-A",
        "omics-coding/1.0",
        url,
    ]
    for attempt in range(retries):
        try:
            data = subprocess.check_output(command, stderr=subprocess.DEVNULL)
            if data:
                if pause:
                    time.sleep(pause)
                return data.decode("utf-8", errors="replace")
        except Exception as exc:  # noqa: BLE001 - record and retry transient curl failures.
            last_error = exc
        time.sleep(max(pause, 0.5) * (attempt + 1))
    if last_error:
        raise last_error
    raise RuntimeError("curl returned empty response")


def curl_fetch_bytes(url, pause, retries=3, max_time=60):
    last_error = None
    command = [
        "curl",
        "--http1.1",
        "--tlsv1.2",
        "-L",
        "--connect-timeout",
        "10",
        "--retry",
        "1",
        "--max-time",
        str(max_time),
        "-A",
        "omics-coding/1.0",
        url,
    ]
    for attempt in range(retries):
        try:
            data = subprocess.check_output(command, stderr=subprocess.DEVNULL)
            if data:
                if pause:
                    time.sleep(pause)
                return data
        except Exception as exc:  # noqa: BLE001 - record and retry transient curl failures.
            last_error = exc
        time.sleep(max(pause, 0.5) * (attempt + 1))
    if last_error:
        raise last_error
    raise RuntimeError("curl returned empty response")


def fetch(url, pause, retries=3):
    if "mengxu98.github.io/scop" in url or "raw.githubusercontent.com" in url or "api.github.com" in url:
        return curl_fetch(url, pause, retries=2, max_time=8)

    request = Request(url, headers={"User-Agent": "omics-coding/1.0"})
    last_error = None
    for attempt in range(retries):
        try:
            with urlopen(request, timeout=20) as response:
                data = response.read()
            if pause:
                time.sleep(pause)
            return data.decode("utf-8", errors="replace")
        except Exception as exc:  # noqa: BLE001 - retry network failures from docs hosts.
            last_error = exc
            if attempt + 1 < retries:
                time.sleep(max(pause, 0.5) * (attempt + 1))
    try:
        return curl_fetch(url, pause, retries=3, max_time=20)
    except Exception:
        raise last_error


def markdown_from_html(block):
    parser = MarkdownParser()
    parser.feed(block)
    text = "".join(parser.parts)
    lines = [re.sub(r"[ \t]+", " ", line).strip() for line in text.splitlines()]
    compact = []  # type: List[str]
    blank = False
    for line in lines:
        if not line:
            if not blank:
                compact.append("")
            blank = True
            continue
        compact.append(line)
        blank = False
    return "\n".join(compact).strip() + "\n"


def safe_slug(name):
    slug = re.sub(r"\(\)$", "", name)
    slug = re.sub(r"[^A-Za-z0-9_.-]+", "_", slug)
    slug = slug.strip("._-")
    return slug or "unnamed"


def rel_path(path):
    return str(path.relative_to(ROOT))


def parse_links(html_text):
    parser = LinkParser()
    parser.feed(html_text)
    return parser.links


def remove_suffix(value, suffix):
    if value.endswith(suffix):
        return value[: -len(suffix)]
    return value


def discover_omicverse(limit, pause):
    html_text = fetch(OMICVERSE_INDEX, pause)
    entries = []  # type: List[Dict[str, str]]
    seen = set()  # type: set
    for href, _text in parse_links(html_text):
        if "reference/omicverse." not in href or not href.endswith(".html"):
            continue
        url = urljoin(OMICVERSE_INDEX, href)
        name = remove_suffix(Path(href).name, ".html")
        if name in seen:
            continue
        seen.add(name)
        entries.append({"package": "omicverse", "name": name, "url": url, "language": "Python"})
        if limit and len(entries) >= limit:
            break
    return entries


def discover_scop(limit, pause, scop_source):
    if scop_source == "local":
        return discover_scop_from_local(limit)
    if scop_source == "github":
        return discover_scop_from_github(limit, pause)
    try:
        html_text = fetch(SCOP_INDEX, pause)
    except Exception as exc:  # noqa: BLE001 - pkgdown can be flaky from this host.
        print(f"SCOP pkgdown index failed, using GitHub man pages: {exc}", file=sys.stderr)
        return discover_scop_from_github(limit, pause)
    entries = []  # type: List[Dict[str, str]]
    seen = set()  # type: set
    for href, text in parse_links(html_text):
        if not href.endswith(".html"):
            continue
        if href.startswith("../") or "/" in href:
            continue
        if href in {"index.html"}:
            continue
        url = urljoin(SCOP_INDEX, href)
        name = safe_slug(remove_suffix(Path(href).name, ".html"))
        display_name = clean_text(text) or name
        display_name = display_name.replace("()", "")
        if name in seen:
            continue
        seen.add(name)
        raw_url = "https://raw.githubusercontent.com/mengxu98/scop/main/man/{0}.Rd".format(name)
        entries.append(
            {
                "package": "scop",
                "name": name,
                "display_name": display_name,
                "url": url,
                "raw_url": raw_url,
                "prefer_raw": "0",
                "language": "R",
            }
        )
        if limit and len(entries) >= limit:
            break
    return entries


def discover_scop_from_local(limit):
    """Read the help pages bundled with the installed SCOP runtime."""
    r_code = """
args <- commandArgs(trailingOnly = TRUE)
out <- args[[1]]
dir.create(out, recursive = TRUE, showWarnings = FALSE)
db <- tools::Rd_db(\"scop\")
for (rd_name in names(db)) {
  output_path <- file.path(out, paste0(sub(\"[.]Rd$\", \"\", rd_name), \".html\"))
  tools::Rd2HTML(db[[rd_name]], out = output_path)
}
"""
    entries = []  # type: List[Dict[str, str]]
    version = local_scop_version()
    with tempfile.TemporaryDirectory(prefix="scop-rd-") as temp_dir:
        subprocess.check_call(["Rscript", "-e", r_code, temp_dir], stdout=subprocess.DEVNULL)
        for html_path in sorted(Path(temp_dir).glob("*.html")):
            html_text = html_path.read_text(encoding="utf-8", errors="replace")
            if not re.search(r"<h3>Usage</h3>", html_text, flags=re.I):
                continue
            name = safe_slug(html_path.stem)
            entries.append(
                {
                    "package": "scop",
                    "name": name,
                    "display_name": name,
                    "url": "local://scop/{0}/{1}".format(version, name),
                    "local_html": html_text,
                    "source_mode": "installed SCOP runtime documentation",
                    "language": "R",
                }
            )
            if limit and len(entries) >= limit:
                break
    return entries


def local_scop_version():
    output = subprocess.check_output(
        ["Rscript", "-e", "cat(as.character(utils::packageVersion('scop')))"],
        universal_newlines=True,
    )
    return output.strip()


def discover_scop_from_github(limit, pause):
    entries = discover_scop_from_tarball(limit, pause)
    if entries:
        return entries
    api_text = fetch(SCOP_MAN_API, pause)
    data = json.loads(api_text)
    entries = []  # type: List[Dict[str, str]]
    for item in data:
        filename = item.get("name", "")
        if not filename.endswith(".Rd"):
            continue
        name = safe_slug(remove_suffix(filename, ".Rd"))
        raw_url = item.get("download_url") or "https://raw.githubusercontent.com/mengxu98/scop/main/man/{0}".format(filename)
        url = urljoin(SCOP_REFERENCE_BASE, "{0}.html".format(name))
        entries.append(
            {
                "package": "scop",
                "name": name,
                "display_name": name,
                "url": url,
                "raw_url": raw_url,
                "prefer_raw": "1",
                "language": "R",
            }
        )
        if limit and len(entries) >= limit:
            break
    return entries


def discover_scop_from_tarball(limit, pause):
    try:
        payload = curl_fetch_bytes(SCOP_TARBALL, pause, retries=1, max_time=12)
    except Exception as exc:  # noqa: BLE001 - fall back to GitHub contents API.
        print("SCOP tarball download failed, using GitHub contents API: {0}".format(exc), file=sys.stderr)
        return []

    entries = []  # type: List[Dict[str, str]]
    with tempfile.TemporaryFile() as handle:
        handle.write(payload)
        handle.seek(0)
        with tarfile.open(fileobj=handle, mode="r:gz") as archive:
            members = [
                member
                for member in archive.getmembers()
                if member.isfile() and "/man/" in member.name and member.name.endswith(".Rd")
            ]
            members.sort(key=lambda item: Path(item.name).name)
            for member in members:
                filename = Path(member.name).name
                name = safe_slug(remove_suffix(filename, ".Rd"))
                extracted = archive.extractfile(member)
                if extracted is None:
                    continue
                rd_text = extracted.read().decode("utf-8", errors="replace")
                url = urljoin(SCOP_REFERENCE_BASE, "{0}.html".format(name))
                raw_url = "https://raw.githubusercontent.com/mengxu98/scop/main/man/{0}".format(filename)
                entries.append(
                    {
                        "package": "scop",
                        "name": name,
                        "display_name": name,
                        "url": url,
                        "raw_url": raw_url,
                        "rd_text": rd_text,
                        "prefer_raw": "1",
                        "language": "R",
                    }
                )
                if limit and len(entries) >= limit:
                    break
    return entries


def first_h1(block, fallback):
    match = re.search(r"<h1[^>]*>(.*?)</h1>", block, flags=re.S | re.I)
    if not match:
        return fallback
    text = strip_tags(match.group(1))
    return text or fallback


def first_paragraph(block):
    match = re.search(r"<p>(.*?)</p>", block, flags=re.S | re.I)
    if not match:
        return ""
    return strip_tags(match.group(1))


def extract_block(html_text, package):
    if package == "omicverse":
        match = re.search(r"<article[^>]*class=\"[^\"]*bd-article[^\"]*\"[^>]*>(.*?)</article>", html_text, flags=re.S | re.I)
    else:
        match = re.search(r"<main[^>]*>(.*?)</main>", html_text, flags=re.S | re.I)
    return match.group(1) if match else html_text


def extract_omicverse_signature(block, name):
    match = re.search(r"<dt[^>]*class=\"[^\"]*sig[^\"]*\"[^>]*>.*?</dt>", block, flags=re.S | re.I)
    if not match:
        return name
    return strip_tags(match.group(0)).replace(" [source] #", "").replace("#", "").strip()


def extract_scop_signature(block, name):
    usage = section_after_heading(block, "ref-usage")
    if usage:
        return strip_tags(usage)
    local_usage = section_after_text_heading(block, "Usage")
    if local_usage:
        return strip_tags(local_usage)
    return name


def section_after_heading(block, heading_id):
    pattern = rf"<h2[^>]*id=\"{re.escape(heading_id)}\"[^>]*>.*?</h2>(.*?)(?=<h2|$)"
    match = re.search(pattern, block, flags=re.S | re.I)
    return match.group(1) if match else ""


def section_after_text_heading(block, heading):
    pattern = r"<h[23][^>]*>\s*{0}\s*</h[23]>(.*?)(?=<h[23]|$)".format(re.escape(heading))
    match = re.search(pattern, block, flags=re.S | re.I)
    return match.group(1) if match else ""


def extract_omicverse_parameters(block):
    match = re.search(
        r"<dt[^>]*>\s*Parameters\s*<span[^>]*>\s*:\s*</span>\s*</dt>\s*<dd[^>]*>(.*?)</dd>",
        block,
        flags=re.S | re.I,
    )
    section = match.group(1) if match else ""
    params = []  # type: List[Dict[str, str]]

    def add_param(item):
        strong = re.search(r"<strong>(.*?)</strong>", item, flags=re.S | re.I)
        if not strong:
            return
        name = strip_tags(strong.group(1))
        meaning = strip_tags(item)
        meaning = re.sub(rf"^{re.escape(name)}\s*", "", meaning).strip(" -:")
        params.append({"name": name, "meaning": meaning})

    for item in re.findall(r"<li[^>]*>\s*<p>(.*?)</p>\s*</li>", section, flags=re.S | re.I):
        add_param(item)
    if not params:
        for item in re.findall(r"<p>(.*?)</p>", section, flags=re.S | re.I):
            add_param(item)
    return params


def split_signature_args(value):
    parts = []  # type: List[str]
    current = []  # type: List[str]
    depth = 0
    quote = ""  # type: str
    for char in value:
        if quote:
            current.append(char)
            if char == quote:
                quote = ""
            continue
        if char in {"'", '"'}:
            quote = char
            current.append(char)
            continue
        if char in "([{":
            depth += 1
            current.append(char)
            continue
        if char in ")]}":
            depth = max(0, depth - 1)
            current.append(char)
            continue
        if char == "," and depth == 0:
            parts.append("".join(current).strip())
            current = []
            continue
        current.append(char)
    if current:
        parts.append("".join(current).strip())
    return parts


def extract_signature_parameters(signature):
    start = signature.find("(")
    end = signature.rfind(")")
    if start < 0 or end <= start:
        return []
    params = []  # type: List[Dict[str, str]]
    for item in split_signature_args(signature[start + 1 : end]):
        item = item.strip()
        if not item or item in {"*", "/"}:
            continue
        name = re.split(r"\s*[=:]\s*", item, maxsplit=1)[0].strip()
        if name in {"*", "/"}:
            continue
        if name.startswith("*"):
            name = re.sub(r"\s+", "", name)
        else:
            name = name.split()[-1]
        if not name:
            continue
        params.append({"name": name, "meaning": "Detected from function signature; no parameter description detected."})
    return params


def merge_signature_parameters(params, signature):
    seen = {param["name"] for param in params}
    for param in extract_signature_parameters(signature):
        if param["name"] not in seen:
            params.append(param)
            seen.add(param["name"])
    return params


def extract_scop_parameters(block):
    section = section_after_heading(block, "arguments")
    params = []  # type: List[Dict[str, str]]
    for match in re.finditer(r"<dt[^>]*>(.*?)</dt>\s*<dd[^>]*>(.*?)</dd>", section, flags=re.S | re.I):
        name = strip_tags(match.group(1))
        name = re.sub(r"\s*#", "", name).strip()
        meaning = strip_tags(match.group(2))
        if name:
            params.append({"name": name, "meaning": meaning})
    if params:
        return params
    section = section_after_text_heading(block, "Arguments")
    for match in re.finditer(r"<tr[^>]*>\s*<td[^>]*>(.*?)</td>\s*<td[^>]*>(.*?)</td>\s*</tr>", section, flags=re.S | re.I):
        name = strip_tags(match.group(1)).strip()
        meaning = strip_tags(match.group(2))
        if name:
            params.append({"name": name, "meaning": meaning})
    return params


def extract_rd_command(text, command):
    marker = "\\{0}{{".format(command)
    start = text.find(marker)
    if start < 0:
        return ""
    pos = start + len(marker)
    depth = 1
    out = []
    while pos < len(text) and depth:
        char = text[pos]
        if char == "{":
            depth += 1
            out.append(char)
        elif char == "}":
            depth -= 1
            if depth:
                out.append(char)
        else:
            out.append(char)
        pos += 1
    return "".join(out).strip()


def clean_rd(text):
    text = re.sub(r"(?m)^%.*$", "", text)
    replacements = {
        r"\dots": "...",
        r"\ldots": "...",
        r"\cr": "\n",
        r"\tab": " ",
        r"\R": "R",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    for _ in range(8):
        updated = re.sub(r"\\(?:code|link|pkg|strong|emph|var|file|samp|url|href)\{([^{}]*)\}", r"\1", text)
        if updated == text:
            break
        text = updated
    text = re.sub(r"\\[A-Za-z]+\{([^{}]*)\}", r"\1", text)
    text = re.sub(r"\\[A-Za-z]+", "", text)
    text = text.replace("\\%", "%").replace("\\_", "_")
    return clean_text(text)


def parse_rd_items(section):
    params = []  # type: List[Dict[str, str]]
    pos = 0
    while True:
        marker = section.find("\\item{", pos)
        if marker < 0:
            break
        name_start = marker + len("\\item{")
        name_end = section.find("}", name_start)
        if name_end < 0:
            break
        name = clean_rd(section[name_start:name_end])
        desc_start = name_end + 1
        while desc_start < len(section) and section[desc_start].isspace():
            desc_start += 1
        if desc_start >= len(section) or section[desc_start] != "{":
            pos = name_end + 1
            continue
        depth = 1
        desc_pos = desc_start + 1
        desc = []
        while desc_pos < len(section) and depth:
            char = section[desc_pos]
            if char == "{":
                depth += 1
                desc.append(char)
            elif char == "}":
                depth -= 1
                if depth:
                    desc.append(char)
            else:
                desc.append(char)
            desc_pos += 1
        params.append({"name": name, "meaning": clean_rd("".join(desc))})
        pos = desc_pos
    return params


def parse_scop_rd(entry, rd_text):
    title = clean_rd(extract_rd_command(rd_text, "title")) or entry["name"]
    summary = clean_rd(extract_rd_command(rd_text, "description"))
    usage = clean_rd(extract_rd_command(rd_text, "usage")) or entry["name"]
    params = parse_rd_items(extract_rd_command(rd_text, "arguments"))
    sections = [
        "# {0}".format(title),
        "",
        "## Usage",
        "",
        "```text",
        usage,
        "```",
        "",
    ]
    if summary:
        sections.extend(["## Description", "", summary, ""])
    value = clean_rd(extract_rd_command(rd_text, "value"))
    if value:
        sections.extend(["## Value", "", value, ""])
    examples = extract_rd_command(rd_text, "examples").strip()
    if examples:
        sections.extend(["## Examples", "", "```r", examples, "```", ""])
    return title, summary, usage, params, "\n".join(sections).strip() + "\n"


def fetch_detail(entry, fetched_at, pause, output_references=REFERENCES):
    if entry["package"] == "omicverse":
        html_text = fetch(entry["url"], pause)
        block = extract_block(html_text, entry["package"])
        title = first_h1(block, entry.get("display_name") or entry["name"])
        summary = first_paragraph(block)
        signature = extract_omicverse_signature(block, entry["name"])
        params = extract_omicverse_parameters(block)
        params = merge_signature_parameters(params, signature)
        doc_dir = output_references / "omicverse" / "functions"
    else:
        if entry.get("local_html"):
            block = extract_block(entry["local_html"], entry["package"])
            title = first_h1(block, entry.get("display_name") or entry["name"])
            summary = first_paragraph(block)
            signature = extract_scop_signature(block, entry["name"])
            params = extract_scop_parameters(block)
            body = markdown_from_html(block)
        else:
            try:
                if entry.get("prefer_raw") == "1":
                    raise RuntimeError("using GitHub Rd source by request")
                html_text = fetch(entry["url"], pause)
                block = extract_block(html_text, entry["package"])
                title = first_h1(block, entry.get("display_name") or entry["name"])
                summary = first_paragraph(block)
                signature = extract_scop_signature(block, entry["name"])
                params = extract_scop_parameters(block)
                body = markdown_from_html(block)
            except Exception as exc:  # noqa: BLE001 - fall back to upstream Rd when pkgdown is unreachable.
                raw_url = entry.get("raw_url")
                if not raw_url:
                    raise exc
                rd_text = entry.get("rd_text") or fetch(raw_url, pause)
                title, summary, signature, params, body = parse_scop_rd(entry, rd_text)
        doc_dir = output_references / "scop" / "functions"
    doc_dir.mkdir(parents=True, exist_ok=True)
    doc_path = doc_dir / f"{safe_slug(entry['name'])}.md"
    canonical_doc_path = REFERENCES / entry["package"] / "functions" / f"{safe_slug(entry['name'])}.md"
    write_function_doc(
        doc_path=doc_path,
        title=title,
        entry=entry,
        fetched_at=fetched_at,
        summary=summary,
        signature=signature,
        params=params,
        body=body if entry["package"] == "scop" else markdown_from_html(block),
    )
    function_row = {
        "package": entry["package"],
        "function": entry["name"],
        "summary": summary,
        "language": entry["language"],
        "source_url": entry["url"],
        "doc_path": rel_path(canonical_doc_path),
        "fetched_at": fetched_at,
    }
    parameter_rows = [
        {
            "package": entry["package"],
            "function": entry["name"],
            "parameter": param["name"],
            "meaning": param["meaning"],
            "doc_path": rel_path(canonical_doc_path),
            "source_url": entry["url"],
            "fetched_at": fetched_at,
        }
        for param in params
    ]
    return function_row, parameter_rows


def section_text(text, heading):
    """Return one Markdown section body without its next heading."""
    match = re.search(r"^## {0}\s*$\n(.*?)(?=^## |\Z)".format(re.escape(heading)), text, flags=re.M | re.S)
    return match.group(1).strip() if match else ""


def reuse_cached_detail(entry, cached_references, output_references=REFERENCES):
    """Reuse one verified page from an interrupted refresh without refetching it."""
    cached_path = cached_references / entry["package"] / "functions" / "{0}.md".format(safe_slug(entry["name"]))
    if not cached_path.is_file():
        return None

    text = cached_path.read_text(encoding="utf-8")
    package_match = re.search(r"^- Package: (.+)$", text, flags=re.M)
    function_match = re.search(r"^- Function: `(.+)`$", text, flags=re.M)
    source_match = re.search(r"^- Source: (.+)$", text, flags=re.M)
    fetched_match = re.search(r"^- Fetched at: (.+)$", text, flags=re.M)
    if not all((package_match, function_match, source_match, fetched_match)):
        return None
    if package_match.group(1) != entry["package"] or function_match.group(1) != entry["name"]:
        return None
    if source_match.group(1) != entry["url"]:
        return None

    summary = section_text(text, "Summary").split("\n\n", 1)[0].strip()
    signature = section_text(text, "Signature")
    signature_match = re.search(r"```text\n(.*?)\n```", signature, flags=re.S)
    signature = signature_match.group(1).strip() if signature_match else ""
    parameter_rows = []
    for line in section_text(text, "Parameters").splitlines():
        match = re.match(r"^- `([^`]+)`: ?(.*)$", line)
        if match:
            parameter_rows.append({"name": match.group(1), "meaning": match.group(2).strip()})

    doc_dir = output_references / entry["package"] / "functions"
    doc_dir.mkdir(parents=True, exist_ok=True)
    doc_path = doc_dir / cached_path.name
    shutil.copy2(cached_path, doc_path)
    canonical_doc_path = REFERENCES / entry["package"] / "functions" / cached_path.name
    function_row = {
        "package": entry["package"],
        "function": entry["name"],
        "summary": summary,
        "language": entry["language"],
        "source_url": entry["url"],
        "doc_path": rel_path(canonical_doc_path),
        "fetched_at": fetched_match.group(1),
    }
    parameter_rows = [
        {
            "package": entry["package"],
            "function": entry["name"],
            "parameter": param["name"],
            "meaning": param["meaning"],
            "doc_path": rel_path(canonical_doc_path),
            "source_url": entry["url"],
            "fetched_at": fetched_match.group(1),
        }
        for param in parameter_rows
    ]
    return function_row, parameter_rows


def write_function_doc(doc_path, title, entry, fetched_at, summary, signature, params, body):
    lines = [
        f"# {title}",
        "",
        f"- Package: {entry['package']}",
        f"- Language: {entry['language']}",
        f"- Function: `{entry['name']}`",
        f"- Source: {entry['url']}",
    ]
    if entry.get("raw_url"):
        lines.append(f"- Raw source: {entry['raw_url']}")
    if entry.get("source_mode"):
        lines.append(f"- Source mode: {entry['source_mode']}")
    lines.extend(
        [
            f"- Fetched at: {fetched_at}",
            "",
            "## Summary",
        ]
    )
    lines.extend(
        [
        "",
        summary or "No short summary detected.",
        "",
        "## Signature",
        "",
        "```text",
        signature,
        "```",
        "",
        "## Parameters",
        "",
        ]
    )
    if params:
        for param in params:
            lines.append(f"- `{param['name']}`: {param['meaning'] or 'No description detected.'}")
    else:
        lines.append("No parameters detected.")
    lines.extend(["", "## Full Documentation", "", body])
    doc_path.write_text("\n".join(lines).rstrip() + "\n", encoding="utf-8")


def write_tsv(path, rows, fields):
    with path.open("w", encoding="utf-8", newline="") as handle:
        writer = csv.DictWriter(handle, fieldnames=fields, delimiter="\t", extrasaction="ignore")
        writer.writeheader()
        for row in rows:
            writer.writerow(row)


def read_tsv(path):
    if not path.is_file():
        return []
    with path.open("r", encoding="utf-8", newline="") as handle:
        return list(csv.DictReader(handle, delimiter="\t"))


def write_reference_index(fetched_at, function_rows, parameter_rows, package, references=REFERENCES):
    counts = {}  # type: Dict[str, int]
    for row in function_rows:
        counts[row["package"]] = counts.get(row["package"], 0) + 1
    lines = [
        "# Omics Coding Local Index",
        "",
        f"- Fetched at: {fetched_at}",
        f"- Package argument: {package}",
        f"- Function rows: {len(function_rows)}",
        f"- Parameter rows: {len(parameter_rows)}",
        "",
        "## Counts",
        "",
    ]
    for name in sorted(counts):
        lines.append(f"- {name}: {counts[name]} function docs")
    lines.extend(
        [
            "",
            "## Files",
            "",
            "- `function_index.tsv`: one row per function.",
            "- `parameter_index.tsv`: one row per parameter occurrence.",
            "- `omicverse/functions/*.md`: OmicVerse function docs.",
            "- `scop/functions/*.md`: SCOP function docs.",
            "- `tooling-and-evidence.md`: official tool bridge and evidence triage rules.",
            "",
            "## Refresh",
            "",
            "Run from the skill directory:",
            "",
            "```bash",
            "python3 scripts/update_docs.py --package all",
            "```",
            "",
            "<!-- omicos-reference:begin -->",
            "## OmicOS Reference Layer",
            "",
            "- OmicOS raw skills: 60",
            "- OmicOS strict omics agents: 32",
            "- `omicos/skill_index.tsv`: one row per OmicOS skill with route role and risk note.",
            "- `omicos/agent_index.tsv`: one row per strict omics OmicOS agent with routing, NOT-FOR, handoff, and risk note.",
            "- `omicos/integration_policy.md`: authority order and Murphy acceptance checks.",
            "- `omicos/route_cards/*.md`: compact workflow reminders; use only after OmicVerse/SCOP function discovery.",
            "- `omicos/agent_route_cards/*.md`: compact agent handoff reminders; not an authority layer.",
            "- `omicos/raw_agents/`: selected public agent JSON plus runtime roster for audit.",
            "<!-- omicos-reference:end -->",
        ]
    )
    (references / "index.md").write_text("\n".join(lines) + "\n", encoding="utf-8")


def publish_staged_docs(staged_references, packages):
    for package_name in packages:
        staged_dir = staged_references / package_name / "functions"
        if not staged_dir.exists():
            continue
        target_dir = REFERENCES / package_name / "functions"
        target_dir.mkdir(parents=True, exist_ok=True)
        for doc_path in staged_dir.glob("*.md"):
            shutil.copy2(doc_path, target_dir / doc_path.name)
    for filename in ("function_index.tsv", "parameter_index.tsv", "index.md", "sources.json"):
        shutil.copy2(staged_references / filename, REFERENCES / filename)


def run(package, limit, pause, scop_source, resume_from=None):
    fetched_at = dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat()
    REFERENCES.mkdir(parents=True, exist_ok=True)
    packages = ["omicverse", "scop"] if package == "all" else [package]
    entries = []  # type: List[Dict[str, str]]
    if "omicverse" in packages:
        entries.extend(discover_omicverse(limit, pause))
    if "scop" in packages:
        entries.extend(discover_scop(limit, pause, scop_source))
    if not entries:
        print("No documentation entries discovered.", file=sys.stderr)
        return 1

    cached_references = None
    if resume_from is not None:
        cached_references = resume_from / "references"
        if not cached_references.is_dir():
            raise FileNotFoundError("resume snapshot has no references directory: {0}".format(cached_references))

    scratch_dir = ROOT / "scratch"
    scratch_dir.mkdir(parents=True, exist_ok=True)
    staging_root = Path(tempfile.mkdtemp(prefix="omics-docs-", dir=str(scratch_dir)))
    staged_references = staging_root / "references"
    staged_references.mkdir(parents=True, exist_ok=True)
    try:
        function_rows = []  # type: List[Dict[str, str]]
        parameter_rows = []  # type: List[Dict[str, str]]
        errors = []  # type: List[Dict[str, str]]
        for entry in entries:
            try:
                cached_detail = None
                if cached_references is not None:
                    cached_detail = reuse_cached_detail(entry, cached_references, output_references=staged_references)
                if cached_detail is not None:
                    function_row, params = cached_detail
                    function_rows.append(function_row)
                    parameter_rows.extend(params)
                    print(f"reused {entry['package']}: {entry['name']}", flush=True)
                    continue
                function_row, params = fetch_detail(entry, fetched_at, pause, output_references=staged_references)
                function_rows.append(function_row)
                parameter_rows.extend(params)
                print(f"wrote {entry['package']}: {entry['name']}", flush=True)
            except Exception as exc:  # noqa: BLE001 - update script records failures explicitly.
                errors.append({"package": entry["package"], "function": entry["name"], "url": entry["url"], "error": str(exc)})
                print(f"failed {entry['package']}: {entry['name']}: {exc}", file=sys.stderr)

        # 单包刷新时保留另一包的现有索引，避免发布后总索引只剩当前包。
        if package != "all":
            current_packages = set(packages)
            function_rows.extend(
                row
                for row in read_tsv(REFERENCES / "function_index.tsv")
                if row.get("package") not in current_packages
            )
            parameter_rows.extend(
                row
                for row in read_tsv(REFERENCES / "parameter_index.tsv")
                if row.get("package") not in current_packages
            )
        package_label = "all" if len({row["package"] for row in function_rows}) > 1 else package

        write_tsv(
            staged_references / "function_index.tsv",
            function_rows,
            ["package", "function", "summary", "language", "source_url", "doc_path", "fetched_at"],
        )
        write_tsv(
            staged_references / "parameter_index.tsv",
            parameter_rows,
            ["package", "function", "parameter", "meaning", "doc_path", "source_url", "fetched_at"],
        )
        write_reference_index(fetched_at, function_rows, parameter_rows, package_label, references=staged_references)
        manifest = {
            "fetched_at": fetched_at,
            "package": package_label,
            "limit": limit,
            "function_count": len(function_rows),
            "parameter_count": len(parameter_rows),
            "errors": errors,
            "sources": {
                "omicverse": OMICVERSE_INDEX,
                "scop": "installed SCOP runtime {0}".format(local_scop_version()) if scop_source == "local" else SCOP_INDEX,
            },
            "scop_source": scop_source,
        }
        (staged_references / "sources.json").write_text(json.dumps(manifest, indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        if errors:
            print(f"completed with {len(errors)} errors; canonical docs were not changed", file=sys.stderr)
            return 2
        if limit is None:
            publish_staged_docs(staged_references, packages)
            print("published complete documentation snapshot", flush=True)
        else:
            print("smoke test completed; canonical docs were not changed", flush=True)
        return 0
    finally:
        shutil.rmtree(staging_root, ignore_errors=True)


def parse_args(argv):
    parser = argparse.ArgumentParser(description="Update local OmicVerse and SCOP docs.")
    parser.add_argument("--package", choices=["all", "omicverse", "scop"], default="all")
    parser.add_argument("--limit", type=int, default=None, help="Limit detail pages per package for smoke tests.")
    parser.add_argument("--pause", type=float, default=0.1, help="Seconds to wait between requests.")
    parser.add_argument("--scop-source", choices=["auto", "pkgdown", "github", "local"], default="auto")
    parser.add_argument(
        "--resume-from",
        type=Path,
        default=None,
        help="Reuse verified function pages from an interrupted staging directory.",
    )
    return parser.parse_args(list(argv))


def main(argv=None):
    args = parse_args(sys.argv[1:] if argv is None else argv)
    return run(
        package=args.package,
        limit=args.limit,
        pause=args.pause,
        scop_source=args.scop_source,
        resume_from=args.resume_from,
    )


if __name__ == "__main__":
    raise SystemExit(main())
