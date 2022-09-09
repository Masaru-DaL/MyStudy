# raise NameError("Hi There")
try:
    raise NameError("Hi There")
except NameError as e:
    print(e)
