import zlib

sentence = "あいうえお" * 100
print(len(sentence))

after_file = zlib.compress(sentence.encode("UTF-8"))
print(len(after_file))
