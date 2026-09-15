# Florida 500

2026-11-14 出発のフロリダ旅行に向けた、自分専用の英単語・フレーズ学習アプリ（iPhone ホーム画面用 Web アプリ）。

## 構成
- `index.html` … アプリ本体（1ファイル）
- `data.js` … 単語データ。**手で編集しない**。`tools/build_data.py` が Obsidian の `04_Private/フロリダ旅行_英単語500.md` から生成する
- `sw.js` / `manifest.webmanifest` / `icon-*.png` … オフライン動作・ホーム画面アイコン用

## 単語データを更新する
```bash
python3 tools/build_data.py && git add -A && git commit -m "update words" && git push
```

## 公開（GitHub Pages）
1. GitHub でリポジトリ `florida-english` を作る（Public）
2. このフォルダで `git remote add origin https://github.com/<user>/florida-english.git && git push -u origin main`
3. リポジトリの Settings › Pages › Source を「Deploy from a branch / main / (root)」にする
4. 数分後 `https://<user>.github.io/florida-english/` を iPhone の Safari で開き、共有 › 「ホーム画面に追加」

## ローカルで動かす
```bash
python3 -m http.server 8765
```
→ http://localhost:8765
