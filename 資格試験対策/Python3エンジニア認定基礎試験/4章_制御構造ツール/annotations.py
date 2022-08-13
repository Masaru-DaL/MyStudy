from zlib import adler32


def plus_one(x: "x is int") -> int:
    return x + 1


print(plus_one(1))
print(plus_one.__annotations__)
