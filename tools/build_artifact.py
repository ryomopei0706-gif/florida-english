#!/usr/bin/env python3
"""index.html を claude.ai Artifact 用の1ファイル（外側タグなし・データ内蔵）に変換する。"""
import re,sys,pathlib
root=pathlib.Path(__file__).resolve().parent.parent
src=(root/'index.html').read_text(encoding='utf-8')
out=re.sub(r'^<!DOCTYPE html>\s*<html lang="ja">\s*<head>\s*','',src).replace('</head>\n<body>\n','')
out=re.sub(r'</body>\s*</html>\s*$','',out); out=re.sub(r'<meta name="viewport"[^>]*>\n','',out); out=re.sub(r'<meta charset="utf-8">\n','',out)
out=re.sub(r'<link rel="(apple-touch-icon|icon|manifest)"[^>]*>\n','',out)
for f in ('data.js','dialog.js'):
    out=out.replace(f'<script src="{f}"></script>','<script>\n'+(root/f).read_text(encoding='utf-8')+'</script>')
assert '<html' not in out and 'src="data.js"' not in out and 'src="dialog.js"' not in out
pathlib.Path(sys.argv[1]).write_text(out,encoding='utf-8'); print('artifact built', len(out))
