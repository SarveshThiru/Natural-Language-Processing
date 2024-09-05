import re

# Step 1: Naive Tagging
def naive_tagger(sentence):
    words = sentence.split()
    tagged_sentence = [(word, 'NN') for word in words]  # Tag every word as a noun initially (NN)
    return tagged_sentence

# Step 2: Define Transformation Rules
# Format: (condition_pattern, current_tag, new_tag)
rules = [
    (r'^the$', 'NN', 'DT'),           # 'the' should be tagged as a determiner (DT)
    (r'^(run|jumps?|running)$', 'NN', 'VB'),  # Words related to 'run' should be tagged as verbs (VB)
    (r'.*ly$', 'NN', 'RB'),           # Words ending with 'ly' are usually adverbs (RB)
    (r'^[A-Z][a-z]+$', 'NN', 'NNP'),  # Words starting with a capital letter should be proper nouns (NNP)
]

# Step 3: Apply Transformation Rules
def apply_transformation_rules(tagged_sentence, rules):
    for i, (word, tag) in enumerate(tagged_sentence):
        for pattern, current_tag, new_tag in rules:
            if re.match(pattern, word) and tag == current_tag:
                tagged_sentence[i] = (word, new_tag)
                break  # Stop after the first matching rule is applied
    return tagged_sentence

# Function to perform transformation-based tagging
def transformation_based_tagger(sentence):
    # Initial naive tagging
    tagged_sentence = naive_tagger(sentence)
    print("Initial Tagged:", tagged_sentence)
    
    # Apply transformation rules iteratively
    tagged_sentence = apply_transformation_rules(tagged_sentence, rules)
    return tagged_sentence

# Test the transformation-based tagger
test_sentence = "The quick brown Fox jumps over the lazy dog running swiftly."
result = transformation_based_tagger(test_sentence)

# Print the results
print("Sentence:", test_sentence)
print("Transformed Tagged:", result)
