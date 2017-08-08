import re
import urllib.request

#https://www.google.com/finance?q=

url = "https://www.google.com/finance?q="
stock = input("Enter your stock: ")

try:
    url = url + stock
    print("Page used to crawl stock: " + url)

    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8")

    m = re.search('meta itemprop="price"',data1)

    start = m.start()
    end = start + 50
    newString = data1[start:end]

    m = re.search('content="',newString)
    start = m.end()

    newString1 = newString[start:]
    m = re.search("/",newString1)
    start = 0
    end = m.end()-3
    final = newString1[0:end]

    print("The value of " + stock.upper() + ": " +  final)

except:
    print("Cannot find " + stock + ", please try again." )
