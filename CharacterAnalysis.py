from nltk.corpus import stopwords
import nltk

import numpy as np
import networkx as nx
import pylab as plt
from networkx.algorithms import bipartite
import matplotlib.pyplot as plt
from operator import itemgetter

# opens the dataset

filen = open('Ramayan.txt')
raw = filen.read()
rwords =nltk.word_tokenize(raw)

#rwords : the word tokens from our dataset

rset = set(w.lower() for w in rwords if w in stopwords.words('english'))

#creates a set of word-tokens converted to english if the words belong to the english corpus
# who, sun, whose....



#placeswords: has the tokenised list of places in ancient times from the places.txt corpus

placesfile = open('places.txt')
raw1 = placesfile.read()
placeswords=nltk.word_tokenize(raw1)


#import regular expressions
import re

#do a search for all words containing "tra" as suffix in the word tokens from dataset and placesWithTra stores them
#placesWithTra = [w for w in rwords if re.search('tra$',w)]

#print set(placesWithTra) .... ??????? ---- > redundant not a good check Chitra is a name

#stores the words having in "..." or at"...."
placesInAt = []
i = 0
for w in rwords:
    i = i+1
    if w in ['in', 'at']:
        placesInAt.append(rwords[i])

#deb fix

#have all the words without the . in the end in stopcleared
notreq2 = [w for w in rwords if w.endswith(".")]
stopcleared = []
for x in notreq2:
   lim = len(x)-1
   myString = x[0:lim]
   stopcleared.append(myString)
#print stopcleared
wordlist = nltk.corpus.words.words()

# if the word is TitleCase and the word is not in the english corpus and length of the word is greater than 3
#  and the word is not in Wordlist(nltk dictionary)
# Then the word is likely a Propernoun
pnoun1=set([w for w in rwords and stopcleared if w.istitle() and w.lower() not in rset and len(w) > 3 and w.lower() not in wordlist])
notreq1=[w for w in pnoun1 if w.startswith("'")]
propnoun=[w for w in pnoun1 if w not in notreq1]

#cleaned proper noun set
#print propnoun

#compares proper noun set and removes names from places list
placeremove = [a for a in propnoun if a in propnoun and a not in placeswords]
#print placeremove
# was originally a not in and a not in

pos = nltk.pos_tag(propnoun)
taggedword = [a for (a, b) in pos if a in propnoun and b == 'NNP']
#print names2

NameTagSet = [a for a in placeremove if a in taggedword]
#print NameTagSet
#  ---> final set
#print len(NameTagSet) #... comes out as 166

#"""doing stemming"""
#Wht is the point of stemming ???
#--------------------Redundant code --- > Confirm deletion
#porter = nltk.PorterStemmer()
#stemmed1 = [porter.stem(t) for t in NameTagSet]
#print stemmed1
#names5a=[w for w in stemmed1 if w.lower() not in wordlist]
#names6a=set(names5a)

#names5b=[w for w in stemmed2 if w.lower() not in wordlist]  #482
#names6b=set(names5b)  #464
#print names6b
#print len(names4)

#Why ???
l = len(NameTagSet)
print l

#----------------Creation of RelationShip Adjacency Matrix--------------------------------#


r = [[0 for y in range(l)] for x in range(l)]

for i in range(l):
	for j in range(l):
		if(i==j):
			r[i][j]=0

#graph code

G = nx.Graph()
H = nx.Graph()

#the code for the adjacency matrix
#every 25 words is a page
pages = len(rwords) / 500
if len(rwords) % 500 != 0:
   pages += 1
for p in range(0,pages,500):
    for s in NameTagSet:
        i=NameTagSet.index(s)
        j=i
        for x in rwords:
            if x in NameTagSet and x !=s:
                j=NameTagSet.index(x)
                r[i][j]+=1
                G.add_edge(s,x,weight=r[i][j])
                r[j][i]+=1
                G.add_edge(x,s,weight=r[j][i])

for i in range(l):
    print r[i]

print G
#write weighted edge list into a file so that U can draw graph separately

#this should be end of the 1st program

nx.write_weighted_edgelist(G, 'trial.weighted.edgelist')

#read weighted edge list from the file now and do the work
#this will be the 2nd program

#H=nx.read_weighted_edgelist('trial.weighted.edgelist')
#nx.draw_networkx(H)
#plt.show()
#print H.edges()
#print H.degree()
#print H.adjacency_list()
#print G.number_of_nodes()
#print G.number_of_edges()
#deg=nx.degree(H)
#print min(deg.values())
#print max(deg.values())
#print nx.is_connected(H)

#print G.is_multigraph()
#cl = list( nx.find_cliques(H) )
#print cl
#dc=nx.degree_centrality(H)
#print sorted(dc.items(), key=itemgetter(1), reverse=True)
#bc = nx.betweenness_centrality(H)
#print sorted(bc.items(), key=itemgetter(1), reverse=True)
#ec = nx.eigenvector_centrality(H)
#print sorted(ec.items(), key=itemgetter(1), reverse=True)

#old code
#H=nx.read_weighted_edgelist('trial.weighted.edgelist')
#nx.draw_networkx(H)

#Add these lines




