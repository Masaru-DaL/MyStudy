squares=[]
cubes=[]

def culc(a, b=1):
    squares.append(a ** 2)
    cubes.append(b ** 3)
    return squares, cubes

print(culc(1))
print(culc(2, 3))
print(culc(3, 4))
print(culc(4, 5))
