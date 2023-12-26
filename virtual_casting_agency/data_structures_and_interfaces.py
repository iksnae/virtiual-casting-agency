# Import required libraries for NLP tasks
import nltk
from transformers import AutoTokenizer, AutoModelForQuestionAnswering
import spacy

# Define NlpEngine class
class NlpEngine:
    def __init__(self):
        nltk.download('punkt')  # Download the Punkt tokenizer
        nltk.download('averaged_perceptron_tagger')  # Download the Averaged Perceptron Tagger for POS tagging

        self.tokenizer = nltk.data.load('tokenizers/punkt/english.pickle')  # Load Punkt tokenizer
        self.parser = nltk.pos_tag  # NLTK's part-of-speech (POS) tagger

    def process(self, input):
        tokens = self.tokenizer.word_tokenize(input)  # Tokenize the text
        tagged = self.parser(tokens)  # POS tag the tokens
        return tagged
