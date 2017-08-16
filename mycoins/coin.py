import re
import urllib.request

#url we'll be searching from
url = "https://coinmarketcap.com/currencies/"

try:
    #Propmt for coin price to be searched
    word = input("Enter full name of the coin: ")

    #Mash together searched coin -> url
    url = url + word

    #Open url and decode utf8
    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8")

    #Search for correct spot
    m = re.search('id="quote_price">', data1)
    start = m.end()
    end = start + 15

    #Make a variable out of the crawled string
    newString = data1[start:end]

    #Exclude the shit, all we care about is the price.
    for char in '</span>':
        newString = newString.replace(char,"")
    #Simply print out price
    print("Current coin price:\n" + newString)
    #print("Crawled from  " + url)
except:
    print("The coin could not be found, please try again")
