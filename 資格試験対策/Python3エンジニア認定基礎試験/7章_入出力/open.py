# 変数にはファイルの格納場所のパスを指定出来る(絶対パス or 相対パス)
path = './str.py'
file1 = open(path)
print(file1.read())

# カレントディレクトリの場合はこちらの書き方でOK
file2 = open('str.py')
print(file2.read())
