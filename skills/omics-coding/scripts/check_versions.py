#!/usr/bin/env python3
"""Check local OmicVerse/SCOP versions against current upstream versions."""

import json
from pathlib import Path
import re
import shutil
import subprocess
import sys
import tarfile
import tempfile
from urllib.request import Request, urlopen


CONDA_FALLBACK = "/hwdata/home/jinqc/miniconda3/condabin/conda"


def conda_cmd():
    found = shutil.which("conda")
    return found or CONDA_FALLBACK


def run_text(command, timeout=180):
    try:
        output = subprocess.check_output(command, stderr=subprocess.STDOUT, timeout=timeout)
        return output.decode("utf-8", errors="replace").strip(), None
    except Exception as exc:
        return "", str(exc)


def fetch_text(url, max_time=5):
    curl = shutil.which("curl")
    if curl:
        output = subprocess.check_output(
            [
                curl,
                "-L",
                "--connect-timeout",
                "5",
                "--retry",
                "1",
                "--max-time",
                str(max_time),
                "-A",
                "omics-coding/1.0",
                "-fsS",
                url,
            ],
            stderr=subprocess.STDOUT,
            timeout=max_time + 5,
        )
        return output.decode("utf-8", errors="replace")
    request = Request(url, headers={"User-Agent": "omics-coding/1.0"})
    with urlopen(request, timeout=max_time) as response:
        return response.read().decode("utf-8", errors="replace")


def fetch_bytes(url, max_time=8):
    curl = shutil.which("curl")
    if curl:
        return subprocess.check_output(
            [
                curl,
                "-L",
                "--connect-timeout",
                "5",
                "--retry",
                "1",
                "--max-time",
                str(max_time),
                "-A",
                "omics-coding/1.0",
                "-fsS",
                url,
            ],
            stderr=subprocess.STDOUT,
            timeout=max_time + 5,
        )
    request = Request(url, headers={"User-Agent": "omics-coding/1.0"})
    with urlopen(request, timeout=max_time) as response:
        return response.read()


def description_field(text, field):
    match = re.search(r"^{0}:\s*(.+)$".format(re.escape(field)), text, flags=re.M)
    return match.group(1).strip() if match else ""


def local_omicverse():
    command = [
        conda_cmd(),
        "run",
        "-n",
        "omicverse",
        "python",
        "-c",
        "import omicverse as ov; print(getattr(ov, '__version__', 'unknown'))",
    ]
    version, error = run_text(command)
    return version or "unknown", "", error


def local_scop():
    command = [
        conda_cmd(),
        "run",
        "-n",
        "seurat_v5",
        "Rscript",
        "-e",
        'd <- utils::packageDescription("scop"); cat(as.character(utils::packageVersion("scop")), "\\t", d[["Date"]], "\\n", sep = "")',
    ]
    output, error = run_text(command)
    if output:
        parts = output.split("\t", 1)
        version = parts[0].strip() or "unknown"
        date = parts[1].strip() if len(parts) > 1 else ""
        return version, date, error
    return "unknown", "", error


def latest_omicverse():
    try:
        data = json.loads(fetch_text("https://pypi.org/pypi/omicverse/json", max_time=5))
        return data.get("info", {}).get("version", "unknown"), "", None
    except Exception as exc:
        return "unknown", "", str(exc)


def latest_scop():
    try:
        text = fetch_text("https://raw.githubusercontent.com/mengxu98/scop/main/DESCRIPTION", max_time=5)
        version = description_field(text, "Version") or "unknown"
        return version, description_field(text, "Date"), None
    except Exception as first_exc:
        try:
            payload = fetch_bytes("https://api.github.com/repos/mengxu98/scop/tarball/main", max_time=8)
            with tempfile.TemporaryFile() as handle:
                handle.write(payload)
                handle.seek(0)
                with tarfile.open(fileobj=handle, mode="r:gz") as archive:
                    member = next(
                        item
                        for item in archive.getmembers()
                        if item.isfile() and Path(item.name).name == "DESCRIPTION"
                    )
                    extracted = archive.extractfile(member)
                    if extracted is None:
                        raise RuntimeError("DESCRIPTION not readable from SCOP tarball")
                    text = extracted.read().decode("utf-8", errors="replace")
            version = description_field(text, "Version") or "unknown"
            return version, description_field(text, "Date"), None
        except Exception as second_exc:
            return "unknown", "", "{0}; tarball fallback: {1}".format(first_exc, second_exc)


def status_row(name, local, latest, local_error, latest_error, local_date="", latest_date=""):
    if local == "unknown" or latest == "unknown":
        status = "unknown"
    elif local == latest:
        if name == "scop" and local_date and latest_date and local_date != latest_date:
            status = "mismatch"
        else:
            status = "match"
    else:
        status = "mismatch"
    return {
        "package": name,
        "local_version": local,
        "latest_version": latest,
        "local_date": local_date or "",
        "latest_date": latest_date or "",
        "status": status,
        "local_error": local_error or "",
        "latest_error": latest_error or "",
    }


def main():
    ov_local, ov_local_date, ov_local_error = local_omicverse()
    ov_latest, ov_latest_date, ov_latest_error = latest_omicverse()
    scop_local, scop_local_date, scop_local_error = local_scop()
    scop_latest, scop_latest_date, scop_latest_error = latest_scop()

    rows = [
        status_row("omicverse", ov_local, ov_latest, ov_local_error, ov_latest_error, ov_local_date, ov_latest_date),
        status_row("scop", scop_local, scop_latest, scop_local_error, scop_latest_error, scop_local_date, scop_latest_date),
    ]

    print("package\tlocal_version\tlatest_version\tlocal_date\tlatest_date\tstatus")
    for row in rows:
        print(
            "{package}\t{local_version}\t{latest_version}\t{local_date}\t{latest_date}\t{status}".format(
                package=row["package"],
                local_version=row["local_version"],
                latest_version=row["latest_version"],
                local_date=row["local_date"],
                latest_date=row["latest_date"],
                status=row["status"],
            )
        )

    mismatches = [row for row in rows if row["status"] == "mismatch"]
    unknowns = [row for row in rows if row["status"] == "unknown"]
    if mismatches:
        print("")
        print("WARNING: local package version differs from latest upstream docs/source.")
        print("Warn the user before using latest-docs-only functions or parameters.")
    if unknowns:
        print("")
        print("WARNING: at least one version could not be checked. Verify manually before trusting latest docs.")
        for row in unknowns:
            if row["local_error"] or row["latest_error"]:
                print("{0}: {1} {2}".format(row["package"], row["local_error"], row["latest_error"]).strip())
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
