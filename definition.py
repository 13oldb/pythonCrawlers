import re
import urllib.request

#https://dictionary.reference.com/browse/

url = "http://dictionary.com/browse/"
try:
	word = input("Enter your word: ")

	url = url + word + "?s=t"
	#print(url)
	data = urllib.request.urlopen(url).read()
	data1 = data.decode("utf-8")

	#print(data1)

	m = re.search('meta name="description" content="',data1)
	start = m.end()
	end = start + 300

	newString = data1[start:end]
	#print(newString)

	m = re.search("See more",newString)
	end = m.start()-1

	definition = newString[0:end]

	print("Definition of " + word + ":\n" + definition)
except:
	print("The word you're looking for isn't in the dictionary")
