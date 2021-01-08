from nltk.wsd import lesk
from nltk.tokenize import word_tokenize
#from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import wordnet as wn

for ss in wn.synsets('bass'):
    print(ss, ss.definition())

text = "I went fishing for some sea bass."

word = word_tokenize(text)
print("*********************************************")
print(word)
print(lesk(word, 'bass'))

text2 = "The bass line of the song is too weak"

word2 = word_tokenize(text2)
print("*********************************************")
print(word2)
print(lesk(word2, 'bass'))












