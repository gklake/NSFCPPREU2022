# TODO: Label about random 1000(500 p, 500n) rows  to use for training & testing(give best assumption)
# TODO: Clear Negative: links to the same website(internal link)
# TODO: Clear Positive: links to a new website(outgoing link)
# TODO: Based on what row has the link, grab n rows before and after(for the model)
# TODO: 1st neighborhood parameter for model, grabbing n rows above and below the positive case
# TODO: 3rd delta t parameter for model, looking at the date posted, if it is too long ago don't worry about it
# TODO: 2nd searchForOtherOccurance once a new website is found, use that website in a query to see if other rows mention that same website

import re
from datetime import timedelta

import psycopg2
import traceback

links = []
surroundingText = []
positiveContentDict = dict()
negativeContentDict = dict()
cleanedPosContent = dict()
cleanedNegContent = dict()


def connectDB():
	try:
		return psycopg2.connect(host='localhost', user='postgres', password='p@ssword', dbname='DarkWeb')
	except:
		trace = traceback.format_exc()
		print("Data base (DarkWeb) not found.")
		raise SystemExit


def selectRecordByDate(cur, date, t, forumId, topicId):

	# calculate the end date for the query
	end_date = date + timedelta(days=t)

	# execute the SQL query to select records by date range
	query = "SELECT * FROM public.classified_post_content " \
					"WHERE posted_date >= %s " \
					"AND posted_date <= %s " \
					"AND forums_id = %s " \
					"AND topics_id = %s"

	cur.execute(query, (date, end_date, forumId, topicId))
	rows = cur.fetchall()
	return rows


def findOtherOccurrence(cur, link):
	# execute the SQL query to check if the link is in the post_content column
	cur.execute("SELECT * FROM public.classified_post_content WHERE post_content LIKE '%{}%'".format(link))

	rows = cur.fetchall()
	cur.close()
	return rows


def selectNeighborhoodById(cur, neighborhood, post_id, forumId, topicId):
	# execute the SQL query to select records by neighborhood
	query = "SELECT * FROM public.classified_post_content " \
					"WHERE posts_id >= %s - %s " \
					"AND posts_id <= %s + %s " \
					"AND forums_id = %s " \
					"AND topics_id = %s"
	cur.execute(query, (post_id, neighborhood, post_id, neighborhood, forumId, topicId))

	rows = cur.fetchall()
	cur.close()
	return rows


def getLabeledRows(cur):
	# Execute the SQL query with the specified conditions
	# TODO: Edit the query to include extra columns
	cur.execute("""
	    SELECT posts_id, post_content, classification, justification
	    FROM public.t_posts
	    WHERE justification IS NOT NULL 
	    AND classification IS NOT NULL
	""")

	# Fetch all the rows returned by the query
	rows = cur.fetchall()

	# Loop through the rows and print the values of the columns
	for row in rows:
		posts_id, post_content, classification, justification = row
		# print(row, "\n\n\n")
		print("Post ID: ", posts_id)
		print("\tPost Content: ", post_content)
		print("\tPost Classification: ", classification)
		print("\tPost Justification: ", justification, "\n\n\n")
		if classification == 'n':
			negativeContentDict[post_content] = []
		else:
			positiveContentDict[post_content] = []


def getNRows(cur, numRows):
	try:
		query = 'SELECT post_content, posted_date FROM public.t_posts WHERE post_content ~ \'(http[s]?://)?[' \
						'0-9A-Za-z]*.onion\' ORDER BY posted_date '
		cur.execute(query)
		print("Fetching", numRows, "row(s)")
		records = cur.fetchmany(numRows)

		for row in records:
			print("Post ID:", row[0])
	except(Exception, psycopg2.Error) as error:
		print("Error while fetching data from PostgreSQL", error)


connection = connectDB()
if connection is not None:
	print("Database Connected!")

cursor = connection.cursor()

