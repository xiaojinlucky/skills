import assert from "node:assert/strict";
import fs from "node:fs";
import os from "node:os";
import path from "node:path";
import { acquireExclusiveFileLock, releaseExclusiveFileLock, rollbackPath } from "../scripts/transaction-helpers.mjs";

const root = fs.mkdtempSync(path.join(os.tmpdir(), "research-master-transaction-"));
try {
  const untouched = path.join(root, "untouched.txt");
  fs.writeFileSync(untouched, "original", "utf8");
  rollbackPath({
    current: untouched,
    backup: path.join(root, "missing-backup"),
    failed: path.join(root, "failed-untouched"),
    existedInitially: true
  });
  assert.equal(fs.readFileSync(untouched, "utf8"), "original");

  const replaced = path.join(root, "replaced.txt");
  const backup = path.join(root, "backup/replaced.txt");
  fs.mkdirSync(path.dirname(backup), { recursive: true });
  fs.writeFileSync(replaced, "new", "utf8");
  fs.writeFileSync(backup, "original", "utf8");
  rollbackPath({ current: replaced, backup, failed: path.join(root, "failed/replaced.txt"), existedInitially: true });
  assert.equal(fs.readFileSync(replaced, "utf8"), "original");
  assert.equal(fs.readFileSync(path.join(root, "failed/replaced.txt"), "utf8"), "new");

  const created = path.join(root, "created.txt");
  fs.writeFileSync(created, "new", "utf8");
  rollbackPath({
    current: created,
    backup: path.join(root, "missing-created-backup"),
    failed: path.join(root, "failed/created.txt"),
    existedInitially: false
  });
  assert.equal(fs.existsSync(created), false);
  assert.equal(fs.readFileSync(path.join(root, "failed/created.txt"), "utf8"), "new");

  const lockPath = path.join(root, "shared/install.lock");
  const first = acquireExclusiveFileLock(lockPath, { pid: 1 });
  assert.throws(() => acquireExclusiveFileLock(lockPath, { pid: 2 }), /安装锁已存在/);
  releaseExclusiveFileLock(first);
  const second = acquireExclusiveFileLock(lockPath, { pid: 3 });
  releaseExclusiveFileLock(second);
  assert.equal(fs.existsSync(lockPath), false);
} finally {
  fs.rmSync(root, { recursive: true, force: true });
}

console.log("transaction helper tests passed: 4/4");
