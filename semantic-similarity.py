import nltk
from nltk.tokenize import word_tokenize
import numpy as np
from gensim.models.doc2vec import Doc2Vec, TaggedDocument

sentences = ["I need money", "I went to the bank", "He buy a car",
             "I have to pay"]
tokenized_sent = []
for s in sentences:
    tokenized_sent.append(word_tokenize(s.lower()))
print(tokenized_sent)

print("*******************************************************************\n")

tagged_data = [TaggedDocument(d, [i]) for i, d in enumerate(tokenized_sent)]
print(tagged_data)

print("*******************************************************************\n")

model = Doc2Vec(tagged_data, vector_size = 20, window = 2, min_count = 1, epochs = 100)
print(model.wv.vocab)

print("*******************************************************************\n")

test_doc = word_tokenize(
    "I went to the bank to deposit money because I have a payment".lower())
test_doc_vector = model.infer_vector(test_doc)

print(model.docvecs.most_similar(positive = [test_doc_vector]))
