import nltk
from nltk.tokenize import sent_tokenize
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
def preprocess_text(text):
    stop_words = set(stopwords.words('english'))
    ps = PorterStemmer()
    sentences = sent_tokenize(text)
    preprocessed_sentences = []
    for sentence in sentences:
        words = word_tokenize(sentence)
        filtered_words = [ps.stem(word.lower()) for word in words if word.isalnum() and word.lower() not in stop_words]
        preprocessed_sentences.append(' '.join(filtered_words))
    return preprocessed_sentences
def evaluate_coherence(text):
    preprocessed_sentences = preprocess_text(text)
    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(preprocessed_sentences)
    similarity_matrix = cosine_similarity(vectors, vectors)
    print("\nCoherence Matrix:")
    print(similarity_matrix)
def main():
    text = input("Enter a text: ")
    evaluate_coherence(text)
if __name__ == "__main__":
    main()
