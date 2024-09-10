from transformers import MarianMTModel, MarianTokenizer

def translate_text(input_text, source_lang="en", target_lang="fr"):
    model_name = f'Helsinki-NLP/opus-mt-{source_lang}-{target_lang}'
    model = MarianMTModel.from_pretrained(model_name)
    tokenizer = MarianTokenizer.from_pretrained(model_name)
    input_ids = tokenizer.encode(input_text, return_tensors="pt")
    translation_ids = model.generate(input_ids)
    translated_text = tokenizer.decode(translation_ids[0], skip_special_tokens=True)
    return translated_text

def main():
    input_text = input("Enter English text for translation: ")
    translated_text = translate_text(input_text)
    print("\nTranslated Text (French):")
    print(translated_text)

if __name__ == "__main__":
    main()
