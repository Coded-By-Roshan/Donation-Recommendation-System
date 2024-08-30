from sklearn.feature_extraction.text import CountVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_similarity(paragraph1, paragraph2):
    # Tokenize and vectorize the paragraphs
    vectorizer = CountVectorizer().fit_transform([paragraph1, paragraph2])
    vectors = vectorizer.toarray()

    # Calculate the cosine similarity between the vectors
    similarity = cosine_similarity(vectors)

    return similarity[0][1]

if __name__ == "__main__":
    # List of tuples containing (ID, paragraph)
    paragraphs = [
        (1, "Natural language processing (NLP) is a subfield of linguistics, computer science, and artificial intelligence."),
        (2, "NLP is a branch of artificial intelligence that helps computers understand, interpret, and generate human language."),
        (3, "Machine learning is a subset of artificial intelligence."),
        (4, "Deep learning is a subset of machine learning that focuses on neural networks.")
    ]

    # Prompt user to input a paragraph
    user_paragraph = input("Enter your paragraph: ")

    # Convert user input to lowercase
    user_paragraph = user_paragraph.lower()

    # Calculate similarity between user paragraph and each paragraph in the list
    similarity_scores = [(id, calculate_similarity(user_paragraph, para.lower())) for id, para in paragraphs]

    # Sort the list of tuples based on similarity scores
    sorted_scores = sorted(similarity_scores, key=lambda x: x[1], reverse=True)
    print(sorted_scores)
    # Print array of IDs and similarity scores in sorted order
    print("Array of IDs and Similarity Scores in sorted order:")
    # for id, score in sorted_scores:
    #     print(f"ID: {id}, Similarity Score: {score:.4f}")
