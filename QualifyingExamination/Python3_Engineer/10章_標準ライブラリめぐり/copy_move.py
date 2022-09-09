import shutil

# ファイルをコピー
# カレントディレクトリにsample1.txtを作成後
shutil.copyfile('sample1.txt', 'sample2.txt')

# ファイルを移動
# コピーして作成したsample2.txtをカレントディレクトリにあるsampleディレクトリに移動させる
shutil.move('sample2.txt', './sample/sample.txt')
