def square(x):
  result = x ** 2
  return result

a = [1, 2, 3, 4, 5]

result = map(square, a)
print(result)
