import urllib.request

# make a HTTP request
req = urllib.request.urlopen("https://en.wikipedia.org")
# read content as utf-8 string
content = req.read().decode("utf-8")

# save to file
file = open("wikipedia.html", mode="w", encoding="utf-8")
file.write(content)
file.close()