#!/usr/bin/env python3
import os
from argparse import ArgumentParser
from pathlib import Path

"""
rst2html5 must be installed:
> pip install rst2html5
"""


def rst2html(src: Path, dst: Path):
    print(f"{src} -> {dst}")
    dst.parent.mkdir(parents=True, exist_ok=True)
    cmd = f"rst2html5 '{src}' > '{dst}'"
    os.system(cmd)


def build_all(args):
    src_root = Path(args.src)
    dst_root = Path(args.dst)

    if src_root.is_file():
        dst_path = dst_root / src_root.with_suffix('.html')
        rst2html(src_root, dst_path)
        return

    for src_path in src_root.glob('**/*.rst'):
        relative = src_path.relative_to(src_root)
        dst_path = dst_root / relative.with_suffix('.html')
        rst2html(src_path, dst_path)


def parse_args():
    parser = ArgumentParser()
    parser.add_argument('--src', default='src', type=Path,
        help='source path')
    parser.add_argument('--dst', default='bld', type=Path,
        help='destination path')
    return parser.parse_args()


def main():
    args = parse_args()
    build_all(args)


if __name__ == '__main__':
    main()
