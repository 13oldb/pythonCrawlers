import re
import os
import urllib.request

'''
URL we are searching from and decoded to utf8 
'''
data = urllib.request.urlopen('http://iplocation.net/find-ip-address').read()
data1 = data.decode('utf-8')

'''
Finding the right spot from the crawled page
'''

m = re.search('<table class="iptable">',data1)
start = m.end()
end = start + 400

newString = data1[start:end]

m = re.search('<span style="font-size: 1.8em; font-weight: bold;">',newString)
start = m.end()
end = start + 400

newString2 = newString[start:end]

'''
Printing the IP, reduced to 11 chars, IPv4, lazy way.
'''
print(newString2[0:11])


m = re.search('<tr><th>IP Location</th><td>',newString2)
start = m.end()
end = start + 30

'''
Printing the location the lazy way too, limited to 25 chars.
'''
newString3 = newString2[start:end]

print(newString3[0:25])
