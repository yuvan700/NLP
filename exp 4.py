import re
from nltk.stem import PorterStemmer

text = "Natural Language Processing is an interesting field of Artificial Intelligence!"

# Convert to lowercase
text = text.lower()

# Tokenization using regex (NO punkt needed)
tokens = re.findall(r'\b[a-z]+\b', text)

# Manual stopwords (offline)
stop_words = {
    'is', 'an', 'the', 'of', 'and', 'to', 'in', 'a'
}

tokens = [word for word in tokens if word not in stop_words]

# Stemming
stemmer = PorterStemmer()
stemmed_words = [stemmer.stem(word) for word in tokens]

print("Tokens:", tokens)
print("Stemmed Words:", stemmed_words)
