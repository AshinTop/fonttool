#!/usr/bin/env sh
ROOT=$(cd $(dirname "$0") || exit; pwd)
GIT_ROOT="$(git rev-parse --show-toplevel)"

TARGET_DIR="$GIT_ROOT/src/assets/font/"
OUTPUT_FILE="$ROOT/icons.woff2"

# Install requirements
pip3 install -t "$ROOT/Library" -r "$ROOT/requirements.txt"

# https://fonttools.readthedocs.io/en/latest/subset/index.html
# 添加了一些优化命令行参数并使用了zopfli进一步压缩字体文件
pyftsubset "$ROOT/material-icons.woff2" \
  --unicodes-file="$ROOT/unicodes.txt" \
  --output-file="$OUTPUT_FILE" \
  --drop-tables=meta \
  --ignore-missing-unicodes \
  --desubroutinize \
  --recalc-timestamp \
  --with-zopfli \
  --no-hinting \
  --verbose

cp "$OUTPUT_FILE" "$TARGET_DIR"

python "$ROOT/generate_icons.py"

cp "$ROOT/icons.ts" "$GIT_ROOT/src/config/"

exit 0
