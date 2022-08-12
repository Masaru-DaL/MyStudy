def kansu(a, *args, **kwargs):
  print(a, type(a))
  print(args, type(args))
  print(kwargs, type(kwargs))

kansu("a", "b", "c", "d")
