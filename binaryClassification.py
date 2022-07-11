import csv
import re
import urllib.request
import bs4 as bs


def get_corpus():
    # request = urllib.request.urlopen('https://en.wikipedia.org/wiki/Animal_Crossing:_New_Horizons')
    # request = urllib.request.urlopen('https://en.wikipedia.org/wiki/Security_hacker')
    # request = urllib.request.urlopen('https://en.wikipedia.org/wiki/Kirby_and_the_Forgotten_Land')
    request = urllib.request.urlopen('https://en.wikipedia.org/wiki/Hacker')
    raw_html = request.read()

    article_html = bs.BeautifulSoup(raw_html, 'html.parser')
    article_paragraphs = article_html.find_all('p')

    article_text = ''
    for paragraph in article_paragraphs:
        article_text += paragraph.text

    article_text = re.sub(r'\n', '', article_text)
    article_text = re.sub(r'\[\d+', '', article_text)

    return article_text


# corpus = get_corpus()
#
# sentence_list = corpus.split('.')
# sentence_list = [[sentence.strip(), 1] for sentence in sentence_list if len(sentence.strip()) >= 3]
# print(sentence_list)
#
# # header = ['sentence', 'label']
# with open('sentences.csv', 'a+', encoding='utf-8', newline='') as csv_file:
#     csvwriter = csv.writer(csv_file)
#     # csvwriter.writerow(header)
#     csvwriter.writerows(sentence_list)
