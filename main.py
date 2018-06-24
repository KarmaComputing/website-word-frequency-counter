# 'i' is a word
# 'j' is the document
# Fij is the frequency (number of occurrences) of the term (word) i 
# in document j.

# Term frequency is: TFij = Fij/max k Fkj

#Find number of occurrences of each word in the document

from __future__ import division
from math import log
import sys

words = []

count = {'word': 0} # number of times 'word' appears accross whole set

doctermcount = {'word': 0} # number of documents containing the word


stopwords = ['\n', 'and','to', 'because',
             'so', 'the', 'a', 'when', 
             'is', 'how', 'then',
" ",
" ",
"a",
"about",
"above",
"after",
"again",
"against",
"all",
"also",
"am",
"an",
"and",
"another",
"any",
"are",
"aren't",
"as",
"at",
"be",
"because",
"been",
"before",
"being",
"below",
"between",
"both",
"but",
"by",
"can",
"can't",
"cannot",
"could",
"couldn't",
"did",
"didn't",
"do",
"does",
"doesn't",
"doing",
"don't",
"down",
"during",
"each",
"few",
"for",
"from",
"further",
"had",
"hadn't",
"has",
"hasn't",
"have",
"haven't",
"having",
"he",
"he'd",
"he'll",
"he's",
"her",
"here",
"here's",
"hers",
"herself",
"him",
"himself",
"his",
"how",
"how's",
"i",
"i'd",
"i'll",
"i'm",
"i've",
"if",
"in",
"into",
"is",
"isn't",
"it",
"it's",
"its",
"itself",
"let's",
"me",
"more",
"most",
"mustn't",
"my",
"myself",
"no",
"nor",
"not",
"of",
"off",
"on",
"once",
"only",
"or",
"other",
"ought",
"our",
"ours",
"this",
"their",
"that",
"than",
"we",
"with",
"will",
"which",
"you",
"your",
]


# Append stop words from argv
try:
    stopwords.extend(sys.argv[2].split(','))    
except IndexError:
    pass

def wordcountDoc(doc):
    print "wordcountdoc"
    for word in doc.split(' '):
        if word.lower() in stopwords or not word.isalnum():
            continue
        if word not in words:
            words.append(word)
            count[word] = 1
        else:
            count[word] += 1

def mostusedword():
    maxcount = max(count.values())
    for word, countvalue in count.iteritems():
        if countvalue == maxcount:
            return word

def calculateTermFrequency(term):
    ''' the term frequency of term i in document j is 
        fij normalized by dividing it by the maximum 
        number of occurrences of any term. '''
    termCount = count[term] # get term count 
    maxcount = max(count.values())

    termFrequency = termCount / maxcount
    return termFrequency

def normalizeTermFrequence():
    for word, countvalue in count.iteritems():
        termFrequency = calculateTermFrequency(word)
        count[word] = termFrequency

def getInverseDocumentFrequency(term):
    '''Returns measure of how much information the word provides
       that is, whether the term is common or rare across all documents in the
       set.

       Obtained by dividing the total number of documents by the number of
       documents containing the term, and then taking the logarithm of that
       quotient
    '''
    quotient = numDocuments // 1 + numDocsContainingTerm(term) # double "/" is (floored) quotient of x and y
    return log(quotient)


def calctfidf():
    for word in words:
        termFrequency = calculateTermFrequency(word)
        inverseDocFrequency = getInverseDocumentFrequency(word)
        tfidf = termFrequency * inverseDocFrequency
        #update words in count dict with tfidf value
        count[word] = tfidf

def numDocsContainingTerm(term):
    try:
        return doctermcount[term]
    except KeyError:
        return 0

def calcnumDocsContainingTerm(doc):
    for word in words:
        if word not in doctermcount:
            doctermcount[word] = 0
        if word in doc:
            doctermcount[word] += 1

# Get filename(s) from argv
try:
    filenames = sys.argv[1].split(',')
except IndexError:
    filenames = ['text.txt']

numDocuments = len(filenames)
docChanged = True
for filename in filenames:
    with open(filename) as fp:
        doc = fp.read()
        wordcountDoc(doc)
        calcnumDocsContainingTerm(doc)

normalizeTermFrequence()

calctfidf()

def compare(a,b):
    if a > b:
        return 1
    else:
        return -1

words = count.keys()
topWords = sorted(words, cmp=compare, key=count.__getitem__)
topWords.reverse()

print "This website is mostly about:"
print topWords[0]
print topWords[1]
print topWords[2]
print "####### Rest of the words #######"
print "Mostly this document set is about:"
print topWords[0:20]
