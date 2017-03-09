import nltk, xml.dom.minidom
from xml.dom.minidom import Node
from nltk.corpus import stopwords
from nltk.stem import *

#read file
dom = xml.dom.minidom.parse("RodrigoDuterte.xml")
Topic = dom.getElementsByTagName('article')

raw = ""

for node in Topic:
	alist = node.getElementsByTagName('body')
	for a in alist:
		para = a.getElementsByTagName('p')
		for p in para:
			article = p.firstChild.data
			raw = raw + article

#tokenize

tokens = nltk.word_tokenize(raw)
#stem

roots = ""
stemmer = PorterStemmer()
for token in tokens:
	roots = roots + stemmer.stem(token)
print(' '.join(roots))
#roots = [stemmer.stem(tokens) for token in tokens]
#filtered = [root for root in roots if root not in stopwords.words('english')]
#print(' '.join(roots))