# image-gaze-visualizer-mit-license

Python で視線データを解析し、画像上に視線の軌跡や注目ポイントを可視化するツールです。

## 概要

- CSV形式の視線データ（位置と滞在時間）を処理し、動きや注目した場所を可視化
- `merge_close_points()` 関数で近接する点をまとめ、グループ化
- Matplotlib を使用して、視線の軌跡や注目ポイントを描画
- 滞在時間に応じて点のサイズと色を変化させ、視覚的に注目エリアを表現

## 必要な環境・依存パッケージ

- Python 3.x  
- pandas  
- numpy  
- matplotlib  
- (必要に応じて) japanize_matplotlib  

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
このスクリプトは、コマンドライン操作なしで、ファイルをダブルクリックするだけで実行できます。

実行すると、同じフォルダにある sample.csv と fish.png を自動で読み込み、視線データの可視化を行います。

### 注意点
ファイル名や場所を変えたい場合は、スクリプト内の設定を変更してください。

実行結果のグラフが表示されるまで少し時間がかかることがあります。

## 注意事項
使用する画像やデータは、ライセンスに問題のないものを利用してください。

本スクリプトは「個別ユーザーの視線可視化」に特化しており、複数ユーザーに向けたヒートマップ描画は別手法を推奨しています。

## LICENSE
MIT License（詳細はLICENSEファイルをご参照ください）

#### 開発者： iwakazusuwa(Swatchp)
