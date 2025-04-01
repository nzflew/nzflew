print("Starting the program...")

import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

# Function to load FAQ data from a CSV
def load_faq(csv_file):
    print(f"Loading FAQ data from: {csv_file}")
    df = pd.read_csv(csv_file)
    return df

# Function to get the best matching answer
def get_best_match(user_input, df):
    print(f"User Input: {user_input}")
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(df['question'].tolist() + [user_input])
    similarity_scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])
    best_match_index = similarity_scores.argmax()
    return df.iloc[best_match_index]['answer']

# Main chat function
def chat(csv_file):
    print("Starting chat...")
    df = load_faq(csv_file)
    print("AI Chatbot: Ask me anything! Type 'exit' to end.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == 'exit':
            print("AI Chatbot: Goodbye!")
            break
        response = get_best_match(user_input, df)
        print(f"AI Chatbot: {response}")

if __name__ == "__main__":
    print("Starting the chat program...")
    csv_file = "faq.csv"  # Change to your CSV file path
    chat(csv_file)
