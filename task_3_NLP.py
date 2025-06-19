# Task 3: NLP with spaCy – Named Entity Recognition & Sentiment # Task 3: NLP with spaCy



# Named Entity Recognition (NER) and Sentiment Analysis

import spacy
import en_core_web_sm
from collections import Counter
import pandas as pd

# Sample Amazon Product Reviews
reviews = [
    "I love the sound quality of these Bose headphones! They’re worth every cent.",
    "The Samsung Galaxy phone arrived on time and works perfectly.",
    "I had a terrible experience with the HP printer. It keeps jamming and the ink runs out too fast.",
    "Apple MacBook Pro is fast and reliable—an excellent product for designers.",
    "This Adidas running shoe feels cheap and started falling apart after a week."
]

# Load spaCy model
nlp = en_core_web_sm.load()

# Named Entity Recognition
print("Named Entities Found:\n")
for review in reviews:
    doc = nlp(review)
    print(f"Review: {review}")
    for ent in doc.ents:
        print(f" - Entity: {ent.text}, Label: {ent.label_}")
    print()

# Rule-Based Sentiment Analysis
positive_keywords = ["love", "great", "excellent", "fast", "perfect", "reliable", "worth"]
negative_keywords = ["terrible", "bad", "poor", "cheap", "jamming", "slow", "falling"]

def simple_sentiment_analysis(text):
    text_lower = text.lower()
    if any(word in text_lower for word in positive_keywords):
        return "Positive"
    elif any(word in text_lower for word in negative_keywords):
        return "Negative"
    else:
        return "Neutral"

print("Sentiment Analysis:\n")
for review in reviews:
    sentiment = simple_sentiment_analysis(review)
    print(f"Sentiment: {sentiment} | Review: {review}")
