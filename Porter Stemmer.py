import nltk
from nltk.stem import PorterStemmer

# Create a list of words
words = ["running", "runs", "ran", "run", "runner"]

# Create a PorterStemmer object
stemmer = PorterStemmer()

# Stem each word in the list
stemmed_words = [stemmer.stem(word) for word in words]

# Print the original words and their stemmed versions
for word, stemmed_word in zip(words, stemmed_words):
    print(f"{word} -> {stemmed_word}")
