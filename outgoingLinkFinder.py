import urllib.request
import bs4 as bs

url = "https://stackoverflow.com/questions/70807518/does-not-match-size-of-target-names"
request = urllib.request.urlopen(url)
splitRootAndPath = url.split(".com")
rawHTML = request.read()
rootURL = splitRootAndPath[0]
print(rootURL)

# Regex to Extract .onion Links: "[a-zA-Z:\/]+.onion[a-zA-Z:\/]*"

articleHTML = bs.BeautifulSoup(rawHTML, 'html.parser')
allLinks = articleHTML.find_all('a')

print("All Links from " + rootURL + ": ")
print("**************************************************")
for link in allLinks:
   print(link.get('href'))

print("Outgoing Links: ")
print("**************************************************")
outgoingLinks = []
for link in allLinks:
   href = link.get('href')
   if str(href).startswith(rootURL):
      continue
   else:
      outgoingLinks.append(href)

for link in outgoingLinks:
   print(link)

print(len(allLinks))
print(len(outgoingLinks))