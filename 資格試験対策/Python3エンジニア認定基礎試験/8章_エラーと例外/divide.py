def divide(x, y):
    try:
        result = x / y
    except ZeroDivisionError as ZDE:
        print(" 0除算されました ")
    else:
        print(" 答えは ", result)
    finally:
        print("finally 実行中 ")


# divide(10, 5)
divide(10, 0)
