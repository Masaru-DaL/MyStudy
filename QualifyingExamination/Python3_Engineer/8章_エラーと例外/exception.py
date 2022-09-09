# raise Exception("何らかの例外")

# try:
#     raise Exception("何らかの例外")
# except Exception as E:
#     print(E)

try:
  raise NameError("Hi There")
except NameError:
  print("NameErrorが出た")
  raise
