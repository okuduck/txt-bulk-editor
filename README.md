# 使用に向けての準備
## Pythonのインストール
HomeBrewの
pyenvのインストール

ls -a
で隠しファイルの表示
最初にPythonのインストールが必要

## 想定しているフォルダの構成


## pathの設定
.envファイルを作成し、そこに.env.sampleファイル内の全テキストをコピペ
folder, fileへのパスを任意で設定する。

## .envファイルを読み込めるようにする
以下のコマンドをターミナルに打ち込む
pip3 install python-dotenv


# 実行方法
main.pyディレクトリまで移動
python main.py {関数名}

## 関数一覧
delete_txt_files
-> フォルダ内の.txtファイルを全て削除
delete_words_from_txt
-> strings_to_remove.txtで指定した文字列をフォルダ内のファイルから一括削除
join_commandline
-> .txtフォルダの分割されたコマンドラインを結合して、ターミナルに出力


# 実装関連

参照した記事
https://chayarokurokuro.hatenablog.com/entry/2021/01/11/160928

# How to use git
## pull
git pull

## push
git add .
git commit -m "message"
git push origin main