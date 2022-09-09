def main():
    i = 10
    while i < 100:
        print(i, i % 5)
        i += 1
        if i % 5 == 0:
            break


if __name__ == "__main__":
    main()
