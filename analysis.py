import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import PlaintextCorpusReader
from nltk.corpus import reuters
#from sklearn.feature_extraction.text import TfidfVectorizer
import string
#import gensim import corpora
from nltk.corpus import wordnet



path = r"C:\Users\Burhan\Desktop\NLP ÖDEV\makale"
text = PlaintextCorpusReader(path, '.*txt')

text.fileids()
#MAKALE UZUNLUĞU YANİ KAÇ KARAKTERDEN OLUŞTUĞUNU BULMA
print("Makale uzunluğu:")
print(len(text.words()))


print("\n")
print("***********************************************************")
#İLK 50 KELİMEYİ EKRANA YAZDIRMA
makale=text.words()[:50]
print(makale)

print("\n")
print("***********************************************************")

#POS-TAGGER İŞLEMİ
b=nltk.pos_tag(makale,tagset='universal')
print(b)


print("\n")
print("***********************************************************")

#MAKALE İÇİNDE KELİME ARATMA
a = nltk.Text(makale)
a.concordance('Akciğer')

print("\n")
print("***********************************************************")


#KELİME SIKLIĞI ANALİZİ

fd = nltk.FreqDist(makale)
print(fd.most_common(10))#METİNDE EN ÇOK KULLANILAN BİLEŞENLERİ GÖRMEK İÇİN



print("\n")
print("***********************************************************")

#NOKTALAMA İŞARETLERİNİ KALDIRMA
p=set(string.punctuation)
sw = set(nltk.corpus.stopwords.words('turkish')) #stopwords kelimeler
makale_filter = [w for w in makale if w.lower() not in sw and w.lower() not in p]
fd = nltk.FreqDist(makale_filter)
print(fd.most_common(10))


print("\n")
print("***********************************************************")


#BİGRAM FONKSİYONU

bgrms = nltk.FreqDist(nltk.bigrams(makale_filter))
print(bgrms.most_common())

print("\n")
print("***********************************************************")

#TRİGRAM FONKSİYONU

tgrms = nltk.FreqDist(nltk.trigrams(makale_filter))
print(tgrms.most_common())



print("\n")
print("***********************************************************")

#SIMILARITY

first_text = wordnet.synsets("sentence")
second_text = wordnet.synsets("word")


first = first_text[0]
second = second_text[0]


print(first)
print(second)


print(first.wup_similarity(second))
print(first.path_similarity(second))
print(first.path_similarity(first))










# #tfidf = TfidfVectorizer()
# tf_idf = text
# for doc in tfidf[text]:
#     print([[dictionary[id], np.around(freq, decimals=2)] for id, freq in doc])



# # tfidf.fit([text.raw(file_id) for file_id in text.fileids()])
# # x = tfidf.transform([text.raw('C:\\Users\\Burhan\\Desktop\\NLP ÖDEV\\makale\\akciğer')])
# # print([x[0,tfidf.vocabulary_['akciğer']]])