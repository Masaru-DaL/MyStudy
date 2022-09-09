from decimal import Decimal

print(0.70 * 1.05)

# round(式, 丸める桁数)
print(round(0.70 * 1.05, 2))

# decimalを用いて丸め規則に則って結果を出力する
print(round(Decimal("0.70") * Decimal("1.05"), 2))
