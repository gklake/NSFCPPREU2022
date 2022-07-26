import codecs
import re
from bs4 import BeautifulSoup

htmlDoc = codecs.open("positiveHTMLPages/Phishing Method 2021 - CryptBB.htm", encoding='utf-8')
soup = BeautifulSoup(htmlDoc, 'html.parser')

# this root URL is for CryptBB, it must be changed for other website domains
rootURL = "cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid"

allLinks = re.findall(r'(http:\/\/|https:\/\/)?([a-zA-Z0-9.-]+)([.])(onion|com)(\/[a-zA-Z0-9\/-]*)*', soup.decode('utf-8'))

print("\n\nAll Links: ")
print("**************************************************")
for link in allLinks:
	print("".join(link))

print("\n\nOutgoing Links: ")
print("**************************************************")
outgoingOnionLinks = set()
outgoingClearNetLinks = set()
for link in allLinks:
	clearNet = ".com"
	if rootURL in "".join(link):
		continue
	else:
		if clearNet in "".join(link):
			# checking if link ends in .com and saving in a different set
			outgoingClearNetLinks.add("".join(link))
			with open('outgoingClearNetLinks.txt', 'a') as file:
				# adding link to file to keep track of all collected outgoing links
				file.write(str("".join(link)) + "\n")
		else:
			outgoingOnionLinks.add("".join(link))
			with open('outgoingOnionLinks.txt', 'a') as file:
				# adding link to file to keep track of all collected outgoing links
				file.write(str("".join(link)) + "\n")

for link in outgoingOnionLinks:
	print(link)

print("# of All Links: " + str(len(allLinks)))
print("# of Outgoing Onion Links: " + str(len(outgoingOnionLinks)))
print("# of Outgoing Clear Net Links: " + str(len(outgoingClearNetLinks)))
