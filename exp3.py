
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer

nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

# Offline Tokenization + Stopword Removal + Lemmatization (Simple)

text = "Stopword removal and lemmatization are important preprocessing steps in NLP"

# 1. Tokenization (simple split – exam safe)
tokens = text.lower().split()

# 2. Stopwords (manual – konjam nariya)
stop_words = {
    "and", "are", "is", "in", "the", "a", "an", "to", "of", "for", "on", "with"
}

filtered_tokens = [word for word in tokens if word not in stop_words]

# 3. Simple Lemmatization (rule based)
lemmatized_tokens = []
for word in filtered_tokens:
    if word.endswith("ing"):
        lemmatized_tokens.append(word[:-4])
    else:
        lemmatized_tokens.append(word)

print("Original Text:")
print(text)

print("\nTokens after Stopword Removal:")
print(filtered_tokens)

print("\nTokens after Lemmatization:")
print(lemmatized_tokens)


