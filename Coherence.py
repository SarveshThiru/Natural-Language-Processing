from textblob import TextBlob
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def preprocess_text(text):
    """
    Preprocess the text.
    """
    return TextBlob(text.lower()).words

def compute_coherence_score(text):
    """
    Compute coherence score using TF-IDF and cosine similarity.
    """
    sentences = [str(sentence) for sentence in TextBlob(text).sentences]
    tokens = [preprocess_text(sentence) for sentence in sentences]

    vectorizer = TfidfVectorizer(stop_words='english', tokenizer=lambda x: x)
    tfidf_matrix = vectorizer.fit_transform(tokens)

    similarity_matrix = cosine_similarity(tfidf_matrix, tfidf_matrix)

    num_sentences = len(sentences)
    coherence_score = sum(similarity_matrix[i][j] for i in range(num_sentences) for j in range(i+1, num_sentences))
    coherence_score /= (num_sentences * (num_sentences - 1) / 2)  # Normalize by total number of sentence pairs

    return coherence_score

def main():
    text = """
    Topic modeling is a powerful tool for discovering the underlying themes or topics in a collection of text documents.
    It can be used to summarize large document collections, identify key themes, or even perform document clustering.
    Latent Dirichlet Allocation (LDA) is one of the most popular techniques for topic modeling.
    It assumes that each document is a mixture of topics and that each word in the document is attributable to one of the document's topics.
    LDA models are widely used in various applications such as text mining, information retrieval, and natural language processing.
    """

    coherence_score = compute_coherence_score(text)
    print("Coherence Score:", coherence_score)

if __name__ == "__main__":
    main()
