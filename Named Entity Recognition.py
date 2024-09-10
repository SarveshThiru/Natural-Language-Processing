import spacy

def perform_ner(text):
    nlp = spacy.load("en_core_web_sm")

    doc = nlp(text)

    entities = [(ent.text, ent.label_) for ent in doc.ents]

    return entities

sample_text = "Apple Inc. is a technology company headquartered in Cupertino, California. Steve Jobs co-founded Apple in 1976."

named_entities = perform_ner(sample_text)

print("Named Entities:")
for entity, label in named_entities:
    print(f"{entity} - {label}")
