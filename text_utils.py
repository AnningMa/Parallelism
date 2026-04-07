import nltk
from nltk.tokenize import word_tokenize
from collections import Counter

nltk.download('punkt_tab', quiet=True)


def tokenize(text: str) -> list[str]:
    """Tokenize text into lowercase alphabetic words using NLTK."""
    tokens = word_tokenize(text.lower())
    return [t for t in tokens if t.isalpha()]

def count_words(tokens: list[str]) -> Counter:
    """Count word frequencies from a list of tokens."""
    return Counter(tokens)
