# カード画像ダウンローダー使い方
## 事前準備
* pythonのインストール
最新版のpythonをインストールしてください。pythonには大きく分けてver2とver3がありますが、ver3の方をインストールしてください。詳しいインストール方法は各自調べてください。
インストール後、コマンドプロンプト(Windows)またはターミナル(MacOS)を開き、pip install requests または　python -m pip install requestsを実行してください。

## 使い方
1. コマンドプロンプト(Windows)またはターミナル(MacOS)を開き、card_image_downloader.pyが置かれているフォルダ(移動していなければこのファイルと同じ場所にあります)に移動します。

2. 以下のコマンドを実行します
python card_image_downloader.py 取得したいカード画像の存在するカードページ名 画像の保存先の相対フォルダ名

※画像の保存先の相対フォルダ名は任意です。指定しない場合、card_image_downloader.pyのあるフォルダと同じ場所に保存されます。なお、相対フォルダとはcard_image_downloader.pyのあるフォルダから見たフォルダです。

3. 実行に成功すると、card_image_downloader.pyのあるフォルダと同じ場所(フォルダ名を指定した場合はそのフォルダ)にダウンロードしたカード画像が保存されます。