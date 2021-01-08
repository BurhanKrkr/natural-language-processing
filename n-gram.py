import nltk
from nltk.util import ngrams
 
def extract_ngrams(data, num):
    n_grams = ngrams(nltk.word_tokenize(data), num)
    return [ ' '.join(grams) for grams in n_grams]
 
data = 'Python ile nltk kütüphanesi kullanıyorum.'
 
print("1-gram: ", extract_ngrams(data, 1))
print("2-gram: ", extract_ngrams(data, 2))
print("3-gram: ", extract_ngrams(data, 3))
print("4-gram: ", extract_ngrams(data, 4))
print("********************************************************")



import nltk
from nltk.tokenize import word_tokenize
text = "Merhaba bugün hava çok güzel."
tokens = nltk.word_tokenize(text)
bigrm = nltk.bigrams(tokens)
print(*map(' '.join, bigrm), sep=', ')
print("********************************************************")

import nltk
from nltk import word_tokenize
from nltk.util import ngrams
text = "Merhaba nasılsın ?"
token=nltk.word_tokenize(text)
bigrams=ngrams(token,2)
trigrams=ngrams(token,3)
print(*map(' '.join, bigrams), sep=', ')
print("********************************************************")
print(*map(' '.join, trigrams), sep=', ')

print("********************************************************")






