import nltk, xml.dom.minidom
from xml.dom.minidom import Node

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
print(tokens)