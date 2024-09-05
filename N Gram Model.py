import nltk
from collections import Counter

def generate_text(ngram_model, start_word, num_words):

  generated_text = [start_word]
  for _ in range(num_words - 1):
    last_word = generated_text[-1]
    possible_next_words = ngram_model.get(tuple(last_word), [])  # Use tuple as key
    if possible_next_words:
      next_word = random.choice(possible_next_words)
      generated_text.append(next_word)
    else:
      break  # If no possible next words, stop generating

  return ' '.join(generated_text)

def build_ngram_model(text, n):
  tokens = nltk.word_tokenize(text)
  ngrams = [tuple(tokens[i:i+n]) for i in range(len(tokens)-n+1)]  # Use tuple for ngram
  ngram_counts = Counter(ngrams)
  return ngram_counts

# Example usage
text = "The quick brown fox jumps over the lazy dog."
ngram_model = build_ngram_model(text, 2)  # Bigram model
start_word = "The"
generated_text = generate_text(ngram_model, start_word, 10)
print(generated_text)
