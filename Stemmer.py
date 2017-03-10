import re
import nltk, xml.dom.minidom
from xml.dom.minidom import Node
from nltk.corpus import stopwords
from nltk.stem.wordnet import WordNetLemmatizer

#read file
dom = xml.dom.minidom.parse("RodrigoDuterte.xml")
Topic = dom.getElementsByTagName('article')

articleCol = []
articles = ""
for node in Topic:
	alist = node.getElementsByTagName('body')
	for a in alist:
		para = a.getElementsByTagName('p')
		for p in para:
			article = p.firstChild.data
			articles = articles + article
			articleCol.insert(0, article)

time = []
for node in Topic:
	alist = node.getElementsByTagName('timePub')
	for a in alist: 
		timepub = a.firstChild.data
		time.insert(0, timepub)

print(time)

#tokenize

#tokens = []
#for article in articles:
#	tokens.extend(nltk.word_tokenize(article))

tokens = re.findall(r"\w+",articles)

#stem

roots = []
lmtzr = WordNetLemmatizer()
for i in range(0, len(tokens)):
	roots.append(lmtzr.lemmatize(tokens[i]))

filtered = [root for root in roots if root not in stopwords.words('english')]
#print(' '.join(filtered))