def kansu(a, *args, **kwargs):
    print(a, type(a))
    print(args, type(args))
    print(kwargs, type(kwargs))


kansu(
    1,
    2,
    3,
    4,
    x=10,
    y=20,
    z=30,
)
