import nltk

from nltk.corpus import wordnet

def explore_word_meanings(word):
    synsets = wordnet.synsets(word)

    if not synsets:
        print(f"No synsets found for '{word}'.")
    else:
        print(f"Synsets for '{word}':")
        for synset in synsets:
            print(f" - {synset.name()} ({synset.pos()})")
            print(f"   Definition: {synset.definition()}")
            print(f"   Examples: {synset.examples()}")
            print()

word_to_explore = "python"

explore_word_meanings(word_to_explore)
