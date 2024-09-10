import nltk
from nltk import pos_tag, word_tokenize
from nltk.chunk import RegexpParser

def extract_noun_phrases(sentence):
    # Tokenize and POS tagging
    words = word_tokenize(sentence)
    tagged_words = pos_tag(words)
    
    # Define a chunk grammar for noun phrases
    chunk_grammar = """
    NP: {<DT>?<JJ>*<NN.*>+}
    """
    chunk_parser = RegexpParser(chunk_grammar)
    
    # Parse the tagged words into chunks
    chunk_tree = chunk_parser.parse(tagged_words)
    
    # Extract noun phrases from the chunked tree
    noun_phrases = []
    for subtree in chunk_tree.subtrees(filter=lambda t: t.label() == 'NP'):
        noun_phrase = " ".join(word for word, tag in subtree.leaves())
        noun_phrases.append(noun_phrase)
    
    return noun_phrases

def main():
    sentence = input("Enter a sentence: ")
    noun_phrases = extract_noun_phrases(sentence)
    print("\nNoun Phrases:")
    for phrase in noun_phrases:
        print("-", phrase)

if __name__ == "__main__":
    main()
