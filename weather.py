import re
import urllib.request

#http://www.weather-forecast.com/locations/Helsinki/forecasts/latest


try:
    city = input("Enter your city for 1-3 days forecast: ")
    url = "http://www.weather-forecast.com/locations/" + city + "/forecasts/latest"

    data = urllib.request.urlopen(url).read()
    data1 = data.decode("utf-8")


    m = re.search('span class="phrase">', data1)
    start = m.end()
    end = start + 400

    newString = data1[start:end]
    m = re.search("</span>", newString)
    end = m.start()

    final = newString[0:end]

    print(final)

except:
    print("Can't find " + city + ", please try again")
