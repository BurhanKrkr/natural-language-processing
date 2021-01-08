from nltk.tokenize import sent_tokenize, word_tokenize


example_text = "Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum."

print(sent_tokenize(example_text))

print("------------------------------------------------------------------")


print(word_tokenize(example_text))

print("--------------------------------------------------------------------")

ex2_text = "Merhaba benim adım Burhan. Şu an Python ile tokenize örneği yapıyorum."
print(sent_tokenize(ex2_text))


print("----------------------------------------------------------------------------")


print(word_tokenize(ex2_text))


print("YENİ DENEME************")

text = "And now for something completely different"
a = word_tokenize(text)
print(nltk.pos_tag(a))
