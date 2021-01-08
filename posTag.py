import nltk
from nltk.util import ngrams
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk import pos_tag


text = "The quick brown fox jumps over the lazy dog."
text2 = "The brown fox runs quick to the dog."

w = word_tokenize(text)
s = word_tokenize(text2)

print(w)
print(pos_tag(w))
print(pos_tag(w,tagset='universal'))
print("*******************************************************************")
print(s)
print(pos_tag(s,tagset='universal'))

print("*******************************************************************")




#1. text için bigrams,trigrams
bigrm = nltk.FreqDist(nltk.bigrams(w))
trigrm = nltk.FreqDist(nltk.trigrams(w))
print(*map(' '.join, bigrm), sep=', ')
print("Text1 Bigram",len(bigrm))
print("********************************************************************")
print("Text1 Trigram",len(trigrm))
print(*map(' '.join, trigrm), sep=', ')
print("********************************************************************")


#2. text için bigrams,trigrams
bigrm = nltk.FreqDist(nltk.bigrams(s))
trigrm = nltk.FreqDist(nltk.trigrams(s))
print(*map(' '.join, bigrm), sep=', ')
print("Text2 Bigram",len(bigrm))
print("*********************************************************************")
print("Text2 Trigram",len(trigrm))
print(*map(' '.join, trigrm), sep=', ')
print("*********************************************************************")







