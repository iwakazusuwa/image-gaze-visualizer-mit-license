# ---
# jupyter:
#   jupytext:
#     formats: py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.17.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %%
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import matplotlib.image as mpimg
import japanize_matplotlib

#=============================================
# 入力データ読み込み
#=============================================
df = pd.read_csv("サンプル.csv",encoding='UTF-8')

#=============================================
# 近い点をまとめる関数（前の点と距離20以内なら同じ座標に）
#=============================================
def merge_close_points(x, y, threshold=20):
    # 近い点をまとめる
    merged_x = []
    merged_y = []
    for i in range(len(x)):
        if i == 0:
            merged_x.append(x[i])
            merged_y.append(y[i])
        else:
            dx = x[i] - merged_x[-1]
            dy = y[i] - merged_y[-1]
            dist = np.sqrt(dx*dx + dy*dy)
            if dist <= threshold:
                merged_x.append(merged_x[-1])
                merged_y.append(merged_y[-1])
            else:
                merged_x.append(x[i])
                merged_y.append(y[i])

    # 連続するグループ番号の付与
    group_numbers = []
    group_id = 0
    for i in range(len(merged_x)):
        if i == 0:
            group_numbers.append(group_id)
        else:
            if merged_x[i] != merged_x[i-1] or merged_y[i] != merged_y[i-1]:
                group_id += 1
            group_numbers.append(group_id)

    return merged_x, merged_y, group_numbers

merged_x, merged_y, group_numbers = merge_close_points(df['position_x'], df['position_y'])

#=============================================
# 画像読み込み
#=============================================
img = mpimg.imread("fish.png")

plt.figure(figsize=(13.8, 8.6))
plt.imshow(img)

# 軌跡の線（黒）
plt.plot(merged_x, merged_y, color='black', linewidth=1)

# 点の大きさと色
sizes = df['time'] * 10
colors = df['time']

scatter = plt.scatter(merged_x, merged_y, s=sizes, c=colors, cmap='viridis', alpha=0.8)

plt.colorbar(scatter, label='time')

# 画像の座標系に合わせて軸を設定（左上0,0）
plt.xlim(0, img.shape[1])
plt.ylim(img.shape[0], 0)  # Y軸反転

plt.xlabel("position_x")
plt.ylabel("position_y")
plt.title("視線軌跡 with Gradient Color and Labels")

# 点の中心に time の数字を入れる

for x, y, g, s in zip(merged_x, merged_y, group_numbers, sizes):
    fontsize = np.sqrt(s)  # 面積の平方根を文字サイズに
    plt.text(x, y, str(g), color='red', fontsize=fontsize, ha='center', va='center')

plt.show()

# %%

# %%

# %%
