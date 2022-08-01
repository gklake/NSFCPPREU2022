import csv
import re

db = []
content = []
allLinks = []
dbLinesWithLinks = []
surroundingText = []
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
	content.append(row[2])
	# print("Row: ", row[2], "\n\n")
	currentLinks = re.findall(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', str(row))
	if len(currentLinks) > 0:
		dbLinesWithLinks.append(row)

# for link in allLinks:
# 	print("Link: ", "".join(link))

allLinks = re.findall(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', str(content))
print("# of All Links: ", len(allLinks))

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

for line in dbLinesWithLinks:
	print("Line:", line, '\n')

print("***********************************************************************************************")

for line in dbLinesWithLinks:
	surroundingText.append(re.sub(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', '', line[2]))


print("dbLinesWithLinks[0]:", dbLinesWithLinks[0], '\n')
print("surroundingText[0]:", surroundingText[0], '\n')
