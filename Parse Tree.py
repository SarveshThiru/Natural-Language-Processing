import nltk

def generate_parse_tree(sentence, grammar):
    parser = nltk.ChartParser(grammar)
    tokens = nltk.word_tokenize(sentence)
    parse_trees = list(parser.parse(tokens))
    return parse_trees

simple_grammar = nltk.CFG.fromstring("""
    S -> NP VP
    NP -> Det N
    VP -> V NP
    Det -> 'the' | 'a'
    N -> 'dog' | 'cat'
    V -> 'chased' | 'caught'
""")

sentence = "the dog chased a cat"

parse_trees = generate_parse_tree(sentence, simple_grammar)

for i, tree in enumerate(parse_trees):
    print(f"Parse Tree {i + 1}:")
    tree.pretty_print()
    print()
