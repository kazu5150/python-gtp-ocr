# AI画像テキスト処理プロジェクト

このプロジェクトは、画像からテキストを抽出し、GPT-4を使用して処理し、結果をCSVファイルに保存します。

## セットアップ

1. リポジトリをクローンします
2. `.env.example` を `.env` にコピーし、OpenAI APIキーを追加します
3. `data/input/` ディレクトリに `image.jpg` という名前の画像ファイルを配置します

## 使用方法

Docker Composeを使用して実行（推奨）:

```bash
docker-compose up --build
```

注: 初回実行時や Dockerfile、docker-compose.yml を変更した後は `--build` オプションを付けてください。それ以外の場合は `docker-compose up` で十分です。

または、Pythonを直接使用して実行:

1. 依存関係をインストール: `pip install -r requirements.txt`
2. スクリプトを実行: `python main.py`

結果は `data/output/results.csv` に保存されます。

## 要件

- Docker と Docker Compose（推奨）
- または Python 3.9以上
- OpenAI APIキー

## ライセンス

[MITライセンス](https://opensource.org/licenses/MIT)