import glob

# globディレクトリの「.txt」ファイルを探す
# glob.glob('*.py')
files = glob.glob('./glob/*.txt')
print(files)
