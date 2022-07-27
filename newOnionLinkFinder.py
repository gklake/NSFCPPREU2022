import codecs
import re
from bs4 import BeautifulSoup


def gatherLinksFromHTML():
	global rootURL, allLinks
	# this will need to loop through all collected pages to gather all outgoing links
	htmlDoc = codecs.open("positiveHTMLPages/Phishing Method 2021 - CryptBB.htm", encoding='utf-8')
	soup = BeautifulSoup(htmlDoc, 'html.parser')
	# this root URL is for CryptBB, it must be changed for other website domains
	rootURL = "cryptbbtg65gibadeeo2awe3j7s6evg7eklserehqr4w4e2bis5tebid"
	allLinks = re.findall(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com)(/[a-zA-Z\d/-]*)*', soup.decode('utf-8'))


def printAllLinks():
	for printLink in allLinks:
		print("".join(printLink))


def saveClearNetLink(clearNetLink):
	outgoingClearNetLinks.add("".join(clearNetLink))
	with open('outgoingClearNetLinks.txt', 'a') as file:
		# adding link to file to keep track of all collected outgoing links
		file.write(str("".join(clearNetLink)) + "\n")


def saveOnionLink(onionLink):
	outgoingOnionLinks.add("".join(onionLink))
	with open('outgoingOnionLinks.txt', 'a') as file:
		# adding link to file to keep track of all collected outgoing links
		file.write(str("".join(onionLink)) + "\n")


def filterLinks():
	for filterLink in allLinks:
		onionLink = ".onion"
		if rootURL in "".join(filterLink):
			continue
		else:
			if onionLink not in "".join(filterLink):
				# checking if link ends in .com and saving in a different set
				saveClearNetLink(filterLink)
			else:
				saveOnionLink(filterLink)


def printOutgoingOnionLinks():
	for link in outgoingOnionLinks:
		print(link)


def main():
	global outgoingOnionLinks, outgoingClearNetLinks
	gatherLinksFromHTML()
	print("\n\nAll Links: ")
	print("**************************************************")
	printAllLinks()
	print("\n\nOutgoing Links: ")
	print("**************************************************")
	outgoingOnionLinks = set()
	outgoingClearNetLinks = set()
	filterLinks()
	printOutgoingOnionLinks()
	print("# of All Links: " + str(len(allLinks)))
	print("# of Outgoing Onion Links: " + str(len(outgoingOnionLinks)))
	print("# of Outgoing Clear Net Links: " + str(len(outgoingClearNetLinks)))


if __name__ == "__main__":
	main()
