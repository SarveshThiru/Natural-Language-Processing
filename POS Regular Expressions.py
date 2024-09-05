import re

# Define some simple rules for POS tagging using regular expressions
rules = [
    (r'.*ing$', 'VBG'),  # Gerunds: ending with 'ing'
    (r'.*ed$', 'VBD'),   # Past tense verbs: ending with 'ed'
    (r'.*es$', 'VBZ'),   # Present tense verbs: ending with 'es'
    (r'.*s$', 'NNS'),    # Plural nouns: ending with 's'
    (r'^-?[0-9]+(.[0-9]+)?$', 'CD'),  # Cardinal numbers
    (r'.*able$', 'JJ'),  # Adjectives: ending with 'able'
    (r'.*ful$', 'JJ'),   # Adjectives: ending with 'ful'
    (r'.*ly$', 'RB'),    # Adverbs: ending with 'ly'
    (r'.*', 'NN')        # Default rule: Noun (NN)
]

# Define a function for rule-based POS tagging
def rule_based_pos_tagger(sentence):
    words = sentence.split()
    tagged_sentence = []
    
    for word in words:
        # Check each rule against the word
        for pattern, tag in rules:
            if re.match(pattern, word):
                tagged_sentence.append((word, tag))
                break

    return tagged_sentence

# Test the rule-based POS tagger
test_sentence = "The quick brown fox jumps over the lazy dog running swiftly."
result = rule_based_pos_tagger(test_sentence)

# Print the results
print("Sentence:", test_sentence)
print("Tagged:", result)
