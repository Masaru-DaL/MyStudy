try:
    file = open("try.py")
except IOError:
    print("cannot open")
else:
    print(file.read())
    file.close()
