import nltk
from nltk.tokenize import word_tokenize
from nltk.tag import pos_tag
nltk.download('averaged_perceptron_tagger_eng')

# Sample text
text = "The quick brown fox jumps over the lazy dog."

# Tokenize the text into words
tokens = word_tokenize(text)

# Perform part-of-speech tagging
tagged_text = pos_tag(tokens)

# Print the tagged text
print(tagged_text)
