import re

import psycopg2

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


def insertRecordIntoDatabase(currId, currContent):
	try:
		connection = psycopg2.connect(host='localhost',
																	user='postgres',
																	password='p@ssword',
																	dbname='DarkWeb')
		cursor = connection.cursor()
		postgresInsertQuery = """INSERT INTO public.classified_post_content (classified_id, posts_id, post_content) 
														 VALUES (DEFAULT, %s, %s)"""
		recordToInsert = (currId, currContent)
		cursor.execute(postgresInsertQuery, recordToInsert)
		connection.commit()
		count = cursor.rowcount
		print(count, "record(s) inserted successfully into table")
	except(Exception, psycopg2.Error) as error:
		print("Failed to insert record into table", error)


def updateRecordContentInDatabase(postContent, surroundingContent):
	try:
		connection = psycopg2.connect(host='localhost',
																	user='postgres',
																	password='p@ssword',
																	dbname='DarkWeb')
		cursor = connection.cursor()
		query = """UPDATE public.classified_post_content SET surrounding_text = %s WHERE post_content = %s"""

		cursor.execute(query, (surroundingContent, postContent))

		# commit the changes to the database
		connection.commit()
		count = cursor.rowcount
		print(count, "record updated successfully")
	except(Exception, psycopg2.Error) as error:
		print("Failed to update record into table", error)


def updateRecordLinksInDatabase(postContent, links):
	try:
		connection = psycopg2.connect(host='localhost',
																	user='postgres',
																	password='p@ssword',
																	dbname='DarkWeb')
		cursor = connection.cursor()
		query = """UPDATE public.classified_post_content SET post_links = %s WHERE post_content = %s"""

		cursor.execute(query, (links, postContent))

		# commit the changes to the database
		connection.commit()
		count = cursor.rowcount
		print(count, "record updated successfully")
	except(Exception, psycopg2.Error) as error:
		print("Failed to update record into table", error)


def initializeDB():
	global dbRow, joinedPositiveLinks, positiveLine, surroundingText
	with open('C:/Users/gabby/Documents/REUPythonPrograms/txtFiles/topics_v5.txt', 'r', encoding='utf-8',
						errors='ignore') as csv_file:
		txtFile = csv_file.readlines()
		for i, row in enumerate(txtFile):
			if i > 0:
				dbLine = row.split('\t')
				db.append(dbLine)

	for dbRow in db:
		if dbRow[3] == 'None\n' or dbRow[3] == 'n\n':
			continue
		else:
			content.append(dbRow[2])
			print("ID:", dbRow[0])
			print("\t\tContent:", dbRow[2])
			insertRecordIntoDatabase(dbRow[0], dbRow[2])

		currentLinks = re.findall(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*',
															str(dbRow))
		if len(currentLinks) > 0:
			dbLinesWithLinks.append(dbRow)
			positiveContent.append(dbRow)


def main():
	initializeDB()
	for positiveLine in positiveContent:
		positiveLinks = re.findall(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*',
															 str(positiveLine))
		joinedPositiveLinks = [''.join(tups) for tups in positiveLinks]
		print("\t\tLinks:", joinedPositiveLinks)
		updateRecordLinksInDatabase(positiveLine[2], str(joinedPositiveLinks))
		surroundingText = re.sub(r'(http://|https://)?([a-zA-Z\d.-]+)([.])(onion|com|org|net)(/[a-zA-Z\d/-]*)*', '',
														 positiveLine[2])
		positiveSurroundingText.append(surroundingText)
		updateRecordContentInDatabase(positiveLine[2], surroundingText)
		positiveContentDict[surroundingText] = joinedPositiveLinks
	print("All Done")


if __name__ == "__main__":
	main()
