class MyError(Exception):
    pass


def main():
    try:
        raise MyError("マイエラー")
    except MyError as e:
        print("Error Massage: ", e)
        raise


if __name__ == "__main__":
    main()
