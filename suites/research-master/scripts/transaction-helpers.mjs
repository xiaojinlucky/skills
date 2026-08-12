import fs from "node:fs";
import path from "node:path";

function exists(filePath) {
  return fs.existsSync(filePath) || fs.lstatSync(filePath, { throwIfNoEntry: false }) !== undefined;
}

function move(source, target) {
  if (!exists(source)) return false;
  fs.mkdirSync(path.dirname(target), { recursive: true });
  fs.renameSync(source, target);
  return true;
}

export function rollbackPath({ current, backup, failed, existedInitially }) {
  if (exists(backup)) {
    if (exists(current)) move(current, failed);
    move(backup, current);
  } else if (!existedInitially && exists(current)) {
    move(current, failed);
  }
}

export function acquireExclusiveFileLock(lockPath, metadata) {
  fs.mkdirSync(path.dirname(lockPath), { recursive: true });
  try {
    const fd = fs.openSync(lockPath, "wx");
    fs.writeFileSync(fd, `${JSON.stringify(metadata)}\n`, "utf8");
    return { fd, lockPath };
  } catch (error) {
    if (error.code !== "EEXIST") throw error;
    throw new Error(`安装锁已存在：${lockPath}；确认没有安装任务后再人工移除`);
  }
}

export function releaseExclusiveFileLock(lock) {
  if (!lock) return;
  try { fs.closeSync(lock.fd); } catch {}
  if (exists(lock.lockPath)) fs.unlinkSync(lock.lockPath);
}
