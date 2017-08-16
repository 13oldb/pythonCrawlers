import re
import urllib.request

try:
    url_btc = "https://coinmarketcap.com/currencies/bitcoin" #Bitcoin
    #Open url and decode utf8
    data_btc = urllib.request.urlopen(url_btc).read()
    data1_btc = data_btc.decode("utf-8")

    m = re.search('id="quote_price">', data1_btc)
    start = m.end()
    end = start + 15

    newString = data1_btc[start:end]
    #print(newString)
        #Exclude the shit, all we care about is the price.
    for char in '</span>':
            newString = newString.replace(char,"")
        #Simply print out price
    print("Current Bitcoin price:\n" + newString)

    url_eth = "https://coinmarketcap.com/currencies/ethereum" #Ethereum
    #Open url and decode utf8
    data_eth = urllib.request.urlopen(url_eth).read()
    data1_eth = data_eth.decode("utf-8")

    m = re.search('id="quote_price">', data1_eth)
    start = m.end()
    end = start + 15

    newString = data1_eth[start:end]
    #print(newString)
        #Exclude the shit, all we care about is the price.
    for char in '</span>':
            newString = newString.replace(char,"")
        #Simply print out price
    print("Current Ethereum price:\n" + newString)

    url_pivx = "https://coinmarketcap.com/currencies/pivx" #Pivx
    #Open url and decode utf8
    data_pivx = urllib.request.urlopen(url_pivx).read()
    data1_pivx = data_pivx.decode("utf-8")

    m = re.search('id="quote_price">', data1_pivx)
    start = m.end()
    end = start + 15

    newString = data1_pivx[start:end]
    #print(newString)
        #Exclude the shit, all we care about is the price.
    for char in '</span>':
            newString = newString.replace(char,"")
        #Simply print out price
    print("Current PIVX price:\n" + newString)

    url_dash = "https://coinmarketcap.com/currencies/dash" #Dash
    #Open url and decode utf8
    data_dash = urllib.request.urlopen(url_dash).read()
    data1_dash = data_dash.decode("utf-8")

    m = re.search('id="quote_price">', data1_dash)
    start = m.end()
    end = start + 15

    newString = data1_dash[start:end]
    #print(newString)
        #Exclude the shit, all we care about is the price.
    for char in '</span>':
            newString = newString.replace(char,"")
        #Simply print out price
    print("Current Dash price:\n" + newString)

    url_dcr = "https://coinmarketcap.com/currencies/decred" #Decred
    #Open url and decode utf8
    data_dcr = urllib.request.urlopen(url_dcr).read()
    data1_dcr = data_dcr.decode("utf-8")

    m = re.search('id="quote_price">', data1_dcr)
    start = m.end()
    end = start + 15

    newString = data1_dcr[start:end]
    #print(newString)
        #Exclude the shit, all we care about is the price.
    for char in '</span>':
            newString = newString.replace(char,"")
        #Simply print out price
    print("Current Decred price:\n" + newString)

    url_nxs = "https://coinmarketcap.com/currencies/nexus" #Nexus
    #Open url and decode utf8
    data_nxs = urllib.request.urlopen(url_nxs).read()
    data1_nxs = data_nxs.decode("utf-8")

    m = re.search('id="quote_price">', data1_nxs)
    start = m.end()
    end = start + 15

    newString = data1_nxs[start:end]
    #print(newString)
        #Exclude the shit, all we care about is the price.
    for char in '</span>':
            newString = newString.replace(char,"")
        #Simply print out price
    print("Current Nexus price:\n" + newString)

    url_storj = "https://coinmarketcap.com/currencies/storj" #Storj
    #Open url and decode utf8
    data_storj = urllib.request.urlopen(url_storj).read()
    data1_storj = data_storj.decode("utf-8")

    m = re.search('id="quote_price">', data1_storj)
    start = m.end()
    end = start + 15

    newString = data1_storj[start:end]
    #print(newString)
        #Exclude the shit, all we care about is the price.
    for char in '</span>':
            newString = newString.replace(char,"")
        #Simply print out price
    print("Current Storj price:\n" + newString)

    url_pay = "https://coinmarketcap.com/currencies/tenx" #Tenx
    #Open url and decode utf8
    data_pay = urllib.request.urlopen(url_pay).read()
    data1_pay = data_pay.decode("utf-8")

    m = re.search('id="quote_price">', data1_pay)
    start = m.end()
    end = start + 15

    newString = data1_pay[start:end]
    #print(newString)
        #Exclude the shit, all we care about is the price.
    for char in '</span>':
            newString = newString.replace(char,"")
        #Simply print out price
    print("Current TenX price:\n" + newString)
except:
    print("Something went wrong bitch, see http://downforeveryoneorjustme/coinmarketcap.com")
