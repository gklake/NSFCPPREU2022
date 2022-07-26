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
# allLinks = re.findall(r'[a-zA-Z0-9.:/-]+[.]com[a-zA-Z0-9:/-]*', rawHTML.decode('utf-8'))
allLinks = re.findall(r'"((http|ftp)s?://.*?)"', rawHTML.decode('utf-8'))

'''
# All Regex I've Tried:

   # (http|ftp|https):\/\/([\w\-_]+(?:(?:\.[\w\-_]+)+))([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?
      # Returns link separated: ('https', 'meta.stackexchange.com', '/questions/380295/announcing-the-stacks-editor-beta-release')
   # https?:\/\/(?:[-\w.]|(?:%[\da-zA-Z]{2}))+
      # Returns link without the ending path&/query: https://chat.stackoverflow.com instead of https://chat.stackoverflow.com/withStuffAtTheEnd
   # "((http|ftp)s?://.*?)"
      # Returns the link with everything, but in a tuple with 'http': ('https://cdn.sstatic.net/Sites/stackoverflow/Img/favicon.ico?v=ec617d715196', 'http')
      # The filtering doesn't work, len(allLinks) = len(outgoingLinks). Presumably due to the link being returned in a tuple

'''

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
	if rootURL in link[0]:  # need to use index 0 if the link is returned in a tuple
		continue
	else:
		# outgoingLinks.append(link)
		outgoingLinks.append(link[0])  # need to use index 0 if the link is returned in a tuple

for link in outgoingLinks:
	print(link)

print(len(allLinks))
print(len(outgoingLinks))
