import spacy
def recognize_dialog_acts(conversation):
    nlp = spacy.load("en_core_web_sm")
    doc = nlp(conversation)
    dialog_acts = []
    for sent in doc.sents:
        if "?" in sent.text:
            dialog_act = "Question"
        else:
            dialog_act = "Statement"
        dialog_acts.append((sent.text, dialog_act))
    return dialog_acts
if __name__ == "__main__":
    conversation = "User: How are you? Bot: I'm doing well. User: What's the weather like today?"
    dialog_acts = recognize_dialog_acts(conversation)
    for sentence, dialog_act in dialog_acts:
        print(f"{dialog_act}: {sentence}")

