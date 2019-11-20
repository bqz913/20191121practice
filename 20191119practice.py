# インポート
import numpy as np                                                          # 配列計算ライブラリ
import pandas as pd                                                         # 時系列データを扱うライブラリ
import matplotlib.pyplot as plt                                             # プロット描画ライブラリ
import japanize_matplotlib

# ファイル読み込み
with open('weather_data.csv') as f:
    weather_data = [line.split(',') for line in f]                          # for文内包表記

# データを配列化 ・ DataFrame作成
weather_data = np.array(weather_data)                                       # リストの配列化(列指定が楽になる)
getcol = [0, 1, 4, 7, 10]                                                   # 取得したい列リスト

weather_dataframe = pd.DataFrame(weather_data[6:, getcol],                  # DataFrameの作成
                                 columns=weather_data[3, getcol])
weather_dataframe['年月日'] = pd.to_datetime(weather_dataframe['年月日'])    # 年月日をdatetime化
weather_dataframe.set_index('年月日', inplace=True)                          # 年月日をindexに配置(DataFrameのindexにdatetime型を入れると時系列データが扱いやすくなる)
weather_dataframe = weather_dataframe.astype(float)                         # DataFrameのValueがstrになってたっぽいんでfloat化

# グラフ化
ax = weather_dataframe.plot(y=['平均気温(℃)'], color='k')                    # dataframe型なら簡単にプロット可能！
ax.set_ylabel('気温')
ax2 = weather_dataframe.plot(y=['平均気温(℃)', '最低気温(℃)', '最高気温(℃)'],
                            color=['k', 'b', 'r'],
                            linewidth=0.5)
ax2.set_ylabel('気温')
ax3 = weather_dataframe.plot(y=['降雪量合計(cm)'])
plt.show()