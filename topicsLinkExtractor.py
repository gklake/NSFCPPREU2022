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

with open('topics_v4.txt', 'r', encoding='utf-8', errors='ignore') as csv_file:
	txtFile = csv_file.readlines()
	# csvreader = csv.reader(csv_file, delimiter='\t')
	for i, row in enumerate(txtFile):
		if i > 0:
			line = row.split('\t')
			db.append(line)

for row in db:
	if row[3] == 'None\n':
		continue
	else:
		content.append(row[2])
	# print("Row: ", row[2], "\n\n")
	currentLinks = re.findall(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', str(row))
	if len(currentLinks) > 0:
		dbLinesWithLinks.append(row)
		if row[3] == 'n\n':
			negativeContent.append(row)
		else:
			positiveContent.append(row)

# for link in allLinks:
# 	print("Link: ", "".join(link))

allLinks = re.findall(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', str(content))
print("# of All Links:", len(allLinks))
print("Size of content:", len(content))
print("Size of positive content:", len(positiveContent))
print("Size of negative content:", len(negativeContent))

print("***********************************************************************************************")

for filterLink in allLinks:
	onionLink = ".onion"
	if onionLink not in "".join(filterLink):
		# checking if link ends in .com and saving in a different set
		clearNetLinks.add("".join(filterLink))
	else:
		onionLinks.add("".join(filterLink))

print("# of Clear Net Links: ", len(clearNetLinks))
print("# of Onion Links: ", len(onionLinks))

print("***********************************************************************************************")

print("All Onion Links: ")
for link in onionLinks:
	print("".join(link))

print("***********************************************************************************************")

# for line in dbLinesWithLinks:
# 	print("Line:", line, '\n')
print("# of db lines with links:", len(dbLinesWithLinks))

print("***********************************************************************************************")

for line in positiveContent:
	positiveLinks.append(re.findall(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', str(line)))
	positiveSurroundingText.append(re.sub(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', '', line[2]))

for line in negativeContent:
	negativeLinks.append(re.findall(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', str(line)))
	negativeSurroundingText.append(re.sub(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', '', line[2]))

print("***********************************************************************************************")

print("Size of positive surrounding text:", len(positiveSurroundingText))
print("Size of negative surrounding text:", len(negativeSurroundingText))

print("***********************************************************************************************")

positiveFile = open('positiveSurroundingContent.txt', 'a+')
print("Positive Surrounding Text: ")
for line in positiveSurroundingText:
	print("Line:", line, "\n")
	positiveFile.write(line)
	positiveFile.write('\n')
positiveFile.close()

# for link in positiveLinks:
# 	print("Positive Link:", ''.join(''.join(l) for l in link), '\n')
print("***********************************************************************************************")

negativeFile = open('negativeSurroundingContent.txt', 'a+')
print("Negative Surrounding Text: ")
for line in negativeSurroundingText:
	print("Line:", line, "\n")
	negativeFile.write(line)
	negativeFile.write('\n')
negativeFile.close()

# for link in negativeLinks:
# 	print("Negative Link:", ''.join(''.join(l) for l in link), '\n')
print("***********************************************************************************************")
