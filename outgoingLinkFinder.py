import re
import html
import urllib.request
import bs4 as bs

url = "https://stackoverflow.com/questions/70807518/does-not-match-size-of-target-names"
request = urllib.request.urlopen(url)
splitRootAndPath = url.split(".com")
rawHTML = request.read()
rootURL = splitRootAndPath[0]
print(rootURL)

articleHTML = bs.BeautifulSoup(rawHTML, 'html.parser')
# allLinks = articleHTML.find_all('a')
allLinks = re.findall(r'[a-zA-Z0-9.:/-]+[.]com[a-zA-Z0-9:/-]*', rawHTML.decode('utf-8'))

print("\n\nAll Links from " + url + ": ")
print("**************************************************")
for link in allLinks:
   # print(link.get('href'))
   print(link)

print("\n\nOutgoing Links: ")
print("**************************************************")
outgoingLinks = []
for link in allLinks:
   # href = link.get('href')
   if rootURL in link:
      continue
   else:
      outgoingLinks.append(link)

for link in outgoingLinks:
   print(link)

print(len(allLinks))
print(len(outgoingLinks))
