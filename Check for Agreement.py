import nltk

def check_agreement(sentence, grammar):
    parser = nltk.ChartParser(grammar)
    tokens = nltk.word_tokenize(sentence)
    
    try:
        parse_tree = next(parser.parse(tokens))
        return True
    except StopIteration:
        return False

agreement_grammar = nltk.CFG.fromstring("""
    S -> NP_SG VP_SG | NP_PL VP_PL
    NP_SG -> Det_SG N_SG
    NP_PL -> Det_PL N_PL
    VP_SG -> V_SG
    VP_PL -> V_PL
    Det_SG -> 'the'
    Det_PL -> 'the'
    N_SG -> 'cat'
    N_PL -> 'cats'
    V_SG -> 'chases'
    V_PL -> 'chase'
""")

sentence1 = "the cat chases"
sentence2 = "the cats chases"

result1 = check_agreement(sentence1, agreement_grammar)
result2 = check_agreement(sentence2, agreement_grammar)

print(f"Sentence 1 Agreement: {'Yes' if result1 else 'No'}")
print(f"Sentence 2 Agreement: {'Yes' if result2 else 'No'}")
