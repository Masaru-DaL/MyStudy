from datetime import date

# 現在時間の取得
print(date.today())

# 現在時間(now)と誕生日(birthday)の差を日分で取得する
now = date.today()
birthday = date(2000, 1, 1)
print((now - birthday).days)
