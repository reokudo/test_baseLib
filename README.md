# baseLib.py 概要

`baseLib.py` は，Python 開発でよく使う処理を 1 ファイルにまとめたユーティリティライブラリです．  
数値計算・ファイル入出力・画像処理・動画処理・シリアライズ関連の機能を横断的に提供します．

## 主な公開クラス

### `pyExLib`

Python 汎用ユーティリティ群です．関数名文字列からの実行，時刻/ハッシュ補助，深いコピー補助などを含みます．

### `IOLib`

ファイル/ディレクトリ操作，CSV などの保存，サイズ取得，パス操作などの I/O 系機能です．  
また，内部の `FileStore` で DataFrame や ndarray などをバンドル形式で保存・復元できます．

### `mathLib`

整数/実数判定，型変換，範囲調整，素数判定，素因数分解，GCD などの数学系ユーティリティです．

### `imgLib`

OpenCV ベースの画像処理ユーティリティです．画像表示，テキスト描画，矩形/ポリゴン描画などを提供します．
さらにYOLO ultralyticsを中心とした物体検出関連機能を提供します．

### `videoLib`  

動画の読み書きやフレーム単位処理を行うクラスです．ストリーム処理や並列実行オプションを備えます．

## 依存関係について

`baseLib.py` は多くの外部ライブラリ（例: `numpy`, `pandas`, `matplotlib`, `opencv-python`, `torch`, `ultralytics` など）を利用します．  
一部ライブラリは「未インストールでも import を継続し，該当機能のみ無効化」する設計です．

必要パッケージの導入:

```bash
pip install -r requirements.txt
```

## 最小利用例

```python
from baseLib import pyExLib, IOLib, mathLib, imgLib, videoLib

print(mathLib.isPrime(17))          # True
print(IOLib.getFileSize("README.md"))
```

## 補足

このライブラリは機能範囲が広く，`baseLib.py` は大きなファイルです．  
詳細は各クラス配下の docstring を参照してください．
