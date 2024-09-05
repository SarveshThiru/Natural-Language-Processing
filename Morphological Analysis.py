import nltk
from nltk.stem import PorterStemmer, WordNetLemmatizer

# Download required NLTK data (if not already downloaded)
nltk.download('punkt_tab')
nltk.download('wordnet')

# Sample text
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text into words
tokens = nltk.word_tokenize(text)

# Stemming using PorterStemmer
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokens]
print("Stemmed words:", stemmed_words)

# Lemmatization using WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
lemmatized_words = [lemmatizer.lemmatize(word) for word in tokens]
print("Lemmatized words:", lemmatized_words)
