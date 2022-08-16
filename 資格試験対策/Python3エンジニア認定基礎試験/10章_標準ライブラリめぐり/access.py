from urllib.request import urlopen

with urlopen("https://google.com") as google:
    print(google.read().decode("UTF-8"))
