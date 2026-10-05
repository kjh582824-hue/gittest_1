#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
实用代码片段集合

按需取用。每个函数都尽量独立、无外部依赖。
"""

from datetime import datetime
from pathlib import Path


def human_size(num_bytes: int) -> str:
    """把字节数转成人类可读的大小，例如 1536 -> '1.5 KB'"""
    size = float(num_bytes)
    for unit in ("B", "KB", "MB", "GB", "TB"):
        if size < 1024 or unit == "TB":
            return f"{size:.1f} {unit}" if unit != "B" else f"{int(size)} B"
        size /= 1024


def timestamp(fmt: str = "%Y-%m-%d %H:%M:%S") -> str:
    """返回当前时间的格式化字符串"""
    return datetime.now().strftime(fmt)


def ensure_dir(path) -> Path:
    """确保目录存在，返回 Path 对象"""
    p = Path(path)
    p.mkdir(parents=True, exist_ok=True)
    return p


def chunked(items, size: int):
    """把列表按 size 分批，用于批量请求等场景"""
    for i in range(0, len(items), size):
        yield items[i:i + size]


if __name__ == "__main__":
    # 简单自测
    assert human_size(0) == "0 B"
    assert human_size(1536) == "1.5 KB"
    assert list(chunked([1, 2, 3, 4, 5], 2)) == [[1, 2], [3, 4], [5]]
    print(f"[{timestamp()}] 自测通过")
