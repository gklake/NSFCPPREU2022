import re

db = []
content = []
allLinks = []
dbLinesWithLinks = []
surroundingText = []
positiveContent = []
negativeContent = []
positiveSurroundingText = []
negativeSurroundingText = []
positiveLinks = []
negativeLinks = []
clearNetLinks = set()
onionLinks = set()
positiveContentDict = {}
negativeContentDict = {}


def initializeDB():
	with open('topics_v5.txt', 'r', encoding='utf-8', errors='ignore') as csv_file:
		txtFile = csv_file.readlines()
		for i, row in enumerate(txtFile):
			if i > 0:
				dbLine = row.split('\t')
				db.append(dbLine)


def extractContent():
	for dbRow in db:
		if dbRow[3] == 'None\n':
			continue
		else:
			content.append(dbRow[2])
		currentLinks = re.findall(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', str(dbRow))
		if len(currentLinks) > 0:
			dbLinesWithLinks.append(dbRow)
			if dbRow[3] == 'n\n':
				negativeContent.append(dbRow)
			else:
				positiveContent.append(dbRow)


def gatherSurroundingText():
	for positiveLine in positiveContent:
		positiveLinks = re.findall(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', str(positiveLine))
		joinedPositiveLinks = [''.join(tups) for tups in positiveLinks]
		positiveSurroundingText.append(
			re.sub(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', '', positiveLine[2]))
		positiveContentDict[re.sub(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', '', positiveLine[2])] = joinedPositiveLinks
	for negativeLine in negativeContent:
		negativeLinks = re.findall(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', str(negativeLine))
		joinedNegativeLinks = [''.join(tups) for tups in negativeLinks]
		negativeSurroundingText.append(
			re.sub(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', '', negativeLine[2]))
		negativeContentDict[re.sub(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', '', negativeLine[2])] = joinedNegativeLinks


def filterLinks():
	for filterLink in allLinks:
		onionLink = ".onion"
		if onionLink not in "".join(filterLink):
			# checking if link ends in .com and saving in a different set
			clearNetLinks.add("".join(filterLink))
		else:
			onionLinks.add("".join(filterLink))


def appendToPositiveFile():
	positiveFile = open('positiveSurroundingContent.txt', 'a+')
	print("Positive Surrounding Text: ")
	for line in positiveSurroundingText:
		print("Line:", line, "\n")
		positiveFile.write(line)
		positiveFile.write('\n')
	positiveFile.close()


def appendToNegativeFile():
	negativeFile = open('negativeSurroundingContent.txt', 'a+')
	print("Negative Surrounding Text: ")
	for line in negativeSurroundingText:
		print("Line:", line, "\n")
		negativeFile.write(line)
		negativeFile.write('\n')
	negativeFile.close()


initializeDB()

extractContent()


allLinks = re.findall(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', str(content))
print("# of All Links:", len(allLinks))
print("Size of content:", len(content))
print("Size of positive content:", len(positiveContent))
print("Size of negative content:", len(negativeContent))

print("***********************************************************************************************")

filterLinks()

print("# of Clear Net Links: ", len(clearNetLinks))
print("# of Onion Links: ", len(onionLinks))

print("***********************************************************************************************")

print("All Onion Links: ")
for link in onionLinks:
	print("".join(link))

print("***********************************************************************************************")

print("# of db lines with links:", len(dbLinesWithLinks))

print("***********************************************************************************************")

gatherSurroundingText()

print("***********************************************************************************************")

print("Size of positive surrounding text:", len(positiveSurroundingText))
print("Size of negative surrounding text:", len(negativeSurroundingText))

print("***********************************************************************************************")

appendToPositiveFile()

print("***********************************************************************************************")

appendToNegativeFile()

print("***********************************************************************************************")

print("Positive Content Dictionary:")
for key in positiveContentDict:
	print("Key:", key, "\n\tValue:", positiveContentDict[key])

print("***********************************************************************************************")

print("Negative Content Dictionary:")
for key in negativeContentDict:
	print("Key:", key, "\n\tValue:", negativeContentDict[key])

print("***********************************************************************************************")
