from nltk.stem import WordNetLemmatizer

lemmatizer = WordNetLemmatizer()

print(lemmatizer.lemmatize("cats"))
print(lemmatizer.lemmatize("dogs"))
print(lemmatizer.lemmatize("rocks"))
print(lemmatizer.lemmatize("python"))
print(lemmatizer.lemmatize("java"))
print(lemmatizer.lemmatize("cacti"))
print(lemmatizer.lemmatize("faster"))

print("---------------------------------------")



print(lemmatizer.lemmatize("better"))
print(lemmatizer.lemmatize("better",pos="a"))

print(lemmatizer.lemmatize("best",pos="n"))


