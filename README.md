# image-gaze-visualizer-mit-license

Python で視線データを解析し、画像上に視線の軌跡や注目ポイントを可視化するツールです。

---

## 概要

- CSV形式の視線データ（位置と滞在時間）を処理し、動きや注目した場所を可視化
- `merge_close_points()` 関数で近接する点をまとめ、グループ化
- Matplotlib を使用して、視線の軌跡や注目ポイントを描画
- 滞在時間に応じて点のサイズと色を変化させ、視覚的に注目エリアを表現

---

## 必要な環境・依存パッケージ

- Python 3.x
- 必要なパッケージ：

  ```bash
  pip install pandas numpy matplotlib japanize_matplotlib
  ```

## ファイル構成例

```
project_root/
├── visualize_gaze.py        # メインの視線可視化スクリプト
├── sample.csv               # サンプル視線データ（CSV）
├── fish.png                 # 対象画像（1360×840） 
├── README.md
└── LICENSE
```

## 使い方
1. sample.csv に視線データを準備（位置と滞在時間）
2. visualize_gaze.py を実行して視線の軌跡を可視化。

```
python visualize_gaze.py
```

# 今後の展望
- 複数ユーザーの視線データ統合機能の追加
- ヒートマップや注視点のアニメーション表示
- インタラクティブな視線データの操作機能

- 
# 貢献方法
プロジェクトへの貢献は以下の方法で歓迎します：
- バグ報告や機能追加の提案は Issues で
- コード改善や新機能追加は Pull Request で
- ドキュメント改善や翻訳も歓迎

# LICENSE
MIT License（詳細はLICENSEファイルをご参照ください）

#### 開発者： iwakazusuwa(Swatchp)
