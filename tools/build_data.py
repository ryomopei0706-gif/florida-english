#!/usr/bin/env python3
"""Obsidianの『フロリダ旅行_英単語500.md』を読み、アプリ用の data.js を生成する。
使い方: python3 tools/build_data.py  (mdのパスは引数で上書き可)
"""
import json, re, sys, pathlib

DEFAULT_MD = pathlib.Path.home() / "Library/Mobile Documents/iCloud~md~obsidian/Documents/Peisidian/04_Private/フロリダ旅行_英単語500.md"
md_path = pathlib.Path(sys.argv[1]) if len(sys.argv) > 1 else DEFAULT_MD
out_path = pathlib.Path(__file__).resolve().parent.parent / "data.js"

CAT_ICONS = ["✈️","💺","🛂","🚕","🏨","🍽️","🛍️","🎢","💊","💳","⛅","👋","💬"]

cats, words = [], []
cat_idx = -1
for line in md_path.read_text(encoding="utf-8").splitlines():
    m = re.match(r"^## (\d+)\. (.+?)（(\d+)語）\s*$", line)
    if m:
        cat_idx += 1
        cats.append({"id": cat_idx, "name": m.group(2), "icon": CAT_ICONS[cat_idx % len(CAT_ICONS)]})
        continue
    if cat_idx < 0 or not line.startswith("|"):
        continue
    cells = [c.strip() for c in line.strip().strip("|").split("|")]
    if len(cells) != 4 or cells[0] in ("英語", "---"):
        continue
    en, ja, ex, exja = cells
    words.append({"id": len(words), "c": cat_idx, "en": en, "ja": ja, "ex": ex, "exja": exja})

js = "// 自動生成: tools/build_data.py が『フロリダ旅行_英単語500.md』から生成。手で編集しない。\n"
js += "const CATEGORIES = " + json.dumps(cats, ensure_ascii=False) + ";\n"
js += "const WORDS = " + json.dumps(words, ensure_ascii=False, separators=(",", ":")) + ";\n"
out_path.write_text(js, encoding="utf-8")
print(f"{len(cats)} categories, {len(words)} words -> {out_path}")
for c in cats:
    print(f"  {c['icon']} {c['name']}: {sum(1 for w in words if w['c']==c['id'])}")
