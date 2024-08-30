"""preprocessing the headline text"""
import re
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import PorterStemmer
from nltk.tokenize import regexp_tokenize
from textblob import TextBlob
# Initialize
stop_words = set(stopwords.words('english'))
stemmer = PorterStemmer()

nltk.download('stopwords')
nltk.download('punkt')
nltk.download('punkt_tab')

def preprocess_text(text):
    """Preprocess text: lowercase, remove punctuation, tokenize, remove stopwords, and apply stemming"""
    # Convert to lowercase
    text = text.lower()
    # Remove punctuation
    text = re.sub(r'[^\w\s]', '', text)
    # Tokenize
    tokens = word_tokenize(text)
    # Remove stop words and apply stemming
    tokens = [stemmer.stem(word) for word in tokens if word not in stop_words]
    return ' '.join(tokens)

def get_sentiment(text):
    """Get sentiment of text"""
    analysis = TextBlob(text)
    # Get polarity and classify sentiment
    polarity = analysis.sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'