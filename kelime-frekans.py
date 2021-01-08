import re
import unicodedata
import nltk
from nltk.corpus import stopwords
from collections import Counter
import matplotlib.pyplot as plt
from nltk.tokenize import WhitespaceTokenizer 
from nltk.stem import WordNetLemmatizer
from nltk.collocations import *
from strsimpy.jaro_winkler import JaroWinkler

f = open("akcigerhastaligi.txt", encoding="utf8")
df=f.read()
def basic_clean(text):
  wnl = nltk.stem.WordNetLemmatizer()
  stopwords = nltk.corpus.stopwords.words('turkish') 
  words = re.sub(r'[^\w\s]', '', text).split()
  return [wnl.lemmatize(word) for word in words if word not in stopwords]
words = basic_clean(df)
unigrams=nltk.ngrams(words,1)
unigramsFrequency=Counter(unigrams)
valuesOfUnigrams=list(unigramsFrequency.values())
unigramlist=list(unigramsFrequency)

for x in range(0,len(unigramlist)):
    if(valuesOfUnigrams[x]>4):
        print(unigramlist[x],"is used",valuesOfUnigrams[x],"times")

jarowinkler = JaroWinkler()
print(jarowinkler.similarity('öksürük', 'öksürk'))
print(jarowinkler.similarity('akciğer', 'akciğr'))
print(jarowinkler.similarity('kanser', 'akciğr'))
print(jarowinkler.similarity('kanser', 'öksürk'))
print(jarowinkler.similarity('akciğer', 'öksürk'))


print('öksürk     '   'öksürük')
print('akciğr     '   'akciğer')
print('kansr      '   'kanser')