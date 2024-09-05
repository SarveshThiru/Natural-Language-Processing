import numpy as np

# Define a small corpus with some manually labeled data
training_data = [
    ("the", "DT"), ("dog", "NN"), ("barks", "VB"),
    ("a", "DT"), ("cat", "NN"), ("meows", "VB"),
    ("the", "DT"), ("cat", "NN"), ("sleeps", "VB"),
    ("a", "DT"), ("dog", "NN"), ("runs", "VB")
]

# Get unique tags and words from training data
tags = list(set(tag for _, tag in training_data))
words = list(set(word for word, _ in training_data))

# Create a tag-to-index and word-to-index mapping
tag_index = {tag: i for i, tag in enumerate(tags)}
word_index = {word: i for i, word in enumerate(words)}

# Initialize transition and emission probability matrices
transition_prob = np.zeros((len(tags), len(tags)))
emission_prob = np.zeros((len(tags), len(words)))

# Calculate transition probabilities
for i in range(1, len(training_data)):
    prev_tag = training_data[i - 1][1]
    current_tag = training_data[i][1]
    transition_prob[tag_index[prev_tag], tag_index[current_tag]] += 1

# Normalize transition probabilities
transition_prob = (transition_prob.T / transition_prob.sum(axis=1)).T

# Calculate emission probabilities
for word, tag in training_data:
    emission_prob[tag_index[tag], word_index[word]] += 1

# Normalize emission probabilities
emission_prob = (emission_prob.T / emission_prob.sum(axis=1)).T

# Define a function to perform Viterbi algorithm for POS tagging
def viterbi_algorithm(sentence, tags, transition_prob, emission_prob):
    n = len(sentence)
    m = len(tags)
    
    # Initialize Viterbi matrix and backpointer
    viterbi = np.zeros((m, n))
    backpointer = np.zeros((m, n), dtype=int)
    
    # Initialize the first column of the Viterbi matrix
    for tag in tags:
        tag_id = tag_index[tag]
        word_id = word_index.get(sentence[0], -1)
        if word_id != -1:
            viterbi[tag_id, 0] = emission_prob[tag_id, word_id]
    
    # Fill the Viterbi matrix
    for t in range(1, n):
        word_id = word_index.get(sentence[t], -1)
        for tag_id in range(m):
            if word_id != -1:
                # Calculate the maximum probability for each state
                max_prob, max_state = max(
                    (viterbi[prev_tag, t-1] * transition_prob[prev_tag, tag_id] * emission_prob[tag_id, word_id], prev_tag)
                    for prev_tag in range(m)
                )
                viterbi[tag_id, t] = max_prob
                backpointer[tag_id, t] = max_state

    # Backtrack to find the most likely tag sequence
    best_path = []
    best_last_tag = np.argmax(viterbi[:, -1])
    for t in range(n-1, -1, -1):
        best_path.append(tags[best_last_tag])
        best_last_tag = backpointer[best_last_tag, t]
    best_path.reverse()

    return best_path

# Test the Viterbi algorithm with a new sentence
test_sentence = ["the", "cat", "runs"]
result_tags = viterbi_algorithm(test_sentence, tags, transition_prob, emission_prob)
print(f"Sentence: {' '.join(test_sentence)}")
print(f"Predicted POS tags: {' '.join(result_tags)}")
