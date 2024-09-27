import nltk
nltk.download('punkt_tab')
from nltk.tokenize import sent_tokenize

text = "This is a sentence. Here is another sentence."
sentences = sent_tokenize(text)
print(sentences)

