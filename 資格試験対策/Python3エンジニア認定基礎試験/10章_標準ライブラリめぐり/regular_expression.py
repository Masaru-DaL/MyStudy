import re

# 何羽いるのか？ -> .羽
print(re.findall(r".羽", "庭には3羽のニワトリがいる"))

# 何がいるのか？ -> [ア-ン]
print(re.findall(r"([ア-ン]*)がいる", "庭には3羽のニワトリがいる"))
