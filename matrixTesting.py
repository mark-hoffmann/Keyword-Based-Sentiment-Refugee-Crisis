import csv
import gensim
import nltk
import re
import string
from anew_module import anew
import sys, os
from HoffmannSentiment.Classes import *
import pprint


dir = os.path.dirname(__file__)
fn = os.path.join(os.path.dirname(__file__), 'TextFiles/Independence 2.txt')

with open(fn, 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='|', quotechar=',')
	count = 0
	doc = []
	orderCheck = 0
	for row in spamreader:
		count += 1
		
		if count < 2:
			print row
		try:
			
			for index in row:
				if index == "Independent " and orderCheck == 0:
					#print "got in here"
					print index
					orderCheck = 1
				elif index[3] == '/' and orderCheck == 1:
					#print "got in here"
					print index
					orderCheck = 2
				elif len(index) > 50 and orderCheck == 2:
					#print "last"
					orderCheck = 0
					story = index
					print story[0:10]
					print "|||||||||||||||||||||||||||||||||||||||||||"
					if story > 70:
						doc.append(story)
			
			
			
		except:
			pass

fnn = os.path.join(os.path.dirname(__file__), 'TextFiles/Aljazeera.txt')

with open(fnn, 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='+', quotechar=',')
	#count = 0
	orderCheck = 0
	for row in spamreader:
		count += 1
		
		if count < 2:
			print row
		try:
			
			for index in row:
				if index == "Al Jazeera " and orderCheck == 0:
					#print "got in here"
					print index
					orderCheck = 1
				elif index[-3] == 'G' and orderCheck == 1:
					#print "got in here"
					print index
					orderCheck = 2
				elif len(index) > 50 and orderCheck == 2:
					#print "last"
					orderCheck = 0
					story = index
					print story[0:10]
					print "~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~"
					if story > 70:
						doc.append(story)
			
			
			
		except:
			pass

fnn = os.path.join(os.path.dirname(__file__), 'TextFiles/Lexis.txt')

with open(fnn, 'rb') as csvfile:
	spamreader = csv.reader(csvfile, delimiter='+', quotechar=',')
	#count = 0
	orderCheck = 0
	for row in spamreader:
		count += 1
		
		if count < 2:
			print row
		try:
			
			for index in row:
				if index == "Lexis" and orderCheck == 0:
					#print "got in here"
					print index
					orderCheck = 1
				elif index == 'Story' and orderCheck == 1:
					#print "got in here"
					print index
					orderCheck = 2
				elif len(index) > 50 and orderCheck == 2:
					#print "last"
					orderCheck = 0
					story = index
					print story[0:10]
					print "{}{}{}{}{}{}{}{}{}{}{}{}{}{}{}"
					if story > 70:
						doc.append(story)
			
			
			
		except:
			pass


punc = re.compile( '[%s]' % re.escape( string.punctuation ) )
term_vec = [ ]
print ' '			
print "Import from text file complete."
print "Number of articles: " + str(len(doc))
print "Moving on to processing"
print ' '

count = 0
tracking = 0
#print 'Removing Punctuation: 0%'

#______________________________________________________________________________________________

#REMOVE PUNCTUATION FOR WORD BASED TERM VECTOR
'''
for d in doc:
	count += 1
	if round(float(count)/len(doc),2)*100 % 10 == 0 and round(float(count)/len(doc),2)*100  != tracking:
		print 'Removing Punctuation: ' + str(int(round(float(count)/len(doc),2)*100)) + '%'
		tracking = round(float(count)/len(doc),2)*100 
	d = d.decode('utf-8').lower()
	d = punc.sub( '', d )
	term_vec.append( nltk.word_tokenize( d ) )
		
for vec in term_vec:
	print vec
'''
#______________________________________________________________________________________________
#BREAKING DOWN TO SENTANCE LEVEL
tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')
sentence_sep = []
for d in doc:
	data = d.decode('utf-8') 
	sentence_sep.append(tokenizer.tokenize(data))

singleSentences = []
for sentenceSection in sentence_sep:
	for sentence in range(0,len(sentenceSection)):
		singleSentences.append(sentenceSection[sentence])
		
#for sentence in range(0,5):
	#print singleSentences[sentence]
	#print '||||||||||||||||||'

term_vec = singleSentences


countryCounts = {\
'Albania':[],'Andorra':[],'Armenia':[],'Austria':[],'Azerbaijan':[],\
'Belarus':[],'Belgium':[],'Bosnia':[], 'Herzegovina':[],'Bulgaria':[],\
'Croatia':[],'Cyprus':[],'Czech Republic':[],'Denmark':[],'Estonia':[],\
'Finland':[],'France':[],'Georgia':[],'Germany':[],'Greece':[],'Hungary':[],\
'Iceland':[],'Ireland':[],'Italy':[],'Kazakhstan':[],'Kosovo':[],'Latvia':[],\
'Liechtenstein':[],'Lithuania':[],'Luxembourg':[],'Macedonia':[],'Malta':[],\
'Moldova':[],'Monaco':[],'Montenegro':[],'Netherlands':[],'Norway':[],\
'Poland':[],'Portugal':[],'Romania':[],'Russia':[],'San Marino':[],'Serbia':[],\
'Slovakia':[],'Slovenia':[],'Spain':[],'Sweden':[],'Switzerland':[],'Turkey':[],'Ukraine':[],'United Kingdom':[],\
'Lebanon':[],'Australia':[],'Egypt':[],'Jordan':[],'United States':[],'Syria':[],\
'UK':[],'Britain':[],'US':[]}
sentimentTotal = countryCounts
#______________________________________________________________________________________________

for sentence in range(0, len(term_vec)):
	for country, value in countryCounts.iteritems():
		if country in term_vec[sentence]:
			countryCounts[country].append(term_vec[sentence])
			#print term_vec[sentence]
			
for item in countryCounts['US']:
	countryCounts['United States'].append(item)
for item in countryCounts['UK']:
	countryCounts['Britain'].append(item)

del countryCounts['US']
del countryCounts['UK']
'''  R CODE FORMAT FOR EDGELIST TO MAKE ARCDIAGRAM
lab = rbind(c("Emilia", "Kirk"), c("Emilia", "Yong"), c("Filipe", "Matteo"),
c("Filipe", "Tyler"), c("Matteo", "Filipe"), c("Matteo", "Tyler"), c("Mehmet",
"Rori"), c("Rori", "Kirk"), c("Rori", "Vitor"), c("Anna", "Mehmet"),
c("Anna", "Yong"))
'''

'''
edgeList = 'rbind('
alreadyChecked = []
edgeTrue = 0
docsSame = 0
# lists to get associated weights with the edges
edge1 = []
edge2 = []
similar = []
for country1, value1 in countryCounts.iteritems():
	print country1
	alreadyChecked.append(country1)
	for country2, value2 in countryCounts.iteritems():
		if country2 not in alreadyChecked:
			for v1 in value1:
				for v2 in value2:
					if v1 == v2:
						docsSame += 1
						edgeTrue = 1
		if edgeTrue == 1:
			edgeList += 'c("' + country1 + '", "' + country2 + '"), '
			edge1.append(country1)
			edge2.append(country2)
			similar.append(docsSame)
		docsSame = 0
		edgeTrue = 0
						
print edgeList
print edge1
print '__________'
print edge2
print '___________'
print similar
						
edgeList = edgeList[:-1] #get ride of last comma
'''
						
#the sentences are v!!!!

for key, value in countryCounts.iteritems():
	totalSentiment = 0
	for v in value:
		
		#print v
		#print ' '
		splitter = Splitter()
		postagger = POSTagger()
		splitted_sentences = splitter.split(v)
		pos_tagged_sentences = postagger.pos_tag(splitted_sentences)
		
		dicttagger = DictionaryTagger([ 'dicts/positive.yml', 'dicts/negative.yml', 'dicts/inc.yml', 'dicts/dec.yml', 'dicts/inv.yml'])
		dict_tagged_sentences = dicttagger.tag(pos_tagged_sentences)
		totalSentiment += sentiment_score(dict_tagged_sentences)
	sentimentTotal[key] = totalSentiment
	
	print key, len(value), ': ', sentimentTotal[key]






'''
count = 0
tracking = 0
print 'Removing Stop Words: 0%'
stop_words = nltk.corpus.stopwords.words( 'english' )
for i in range( 0, len( term_vec ) ):
	count += 1
	if round(float(count)/len(term_vec),2)*100 % 10 == 0 and round(float(count)/len(term_vec),2)*100  != tracking:
		print 'Removing Stop Words: ' + str(int(round(float(count)/len(term_vec),2)*100)) + '%'
		tracking = round(float(count)/len(term_vec),2)*100 
	term_list = [ ]

	for term in term_vec[ i ]:
		
		if term not in stop_words:
			term_list.append( term )
	
	term_vec[ i ] = term_list
'''
'''
print "--------Stop words removed--------"

count = 0
tracking = 0
print 'Removing Stems: 0%'
porter = nltk.stem.porter.PorterStemmer()
for i in range( 0, len( term_vec ) ):
	count += 1
	if round(float(count)/len(term_vec),2)*100 % 10 == 0 and round(float(count)/len(term_vec),2)*100  != tracking:
		print 'Removing Stems: ' + str(int(round(float(count)/len(term_vec),2)*100)) + '%'
		tracking = round(float(count)/len(term_vec),2)*100 
	
	for j in range( 0, len( term_vec[ i ] ) ):
		term_vec[ i ][ j ] = porter.stem( term_vec[ i ][ j ] )
		
print "--------Words successfully had stems removed--------"
'''
'''
for vec in term_vec:
	print vec
'''



	
	
	
	
	
	