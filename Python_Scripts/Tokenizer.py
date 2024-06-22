import nltk

"""NLTK (Natural Language Toolkit): NLTK is a popular open-source Python library used for natural language processing 
(NLP) tasks. It provides a wide range of tools and resources for text processing, tokenization, parsing, 
semantic reasoning, and feature extraction.

Key Features:

Tokenization: NLTK provides various tokenization methods to split text into individual words or tokens.
Part-of-Speech Tagging (POS): NLTK includes several POS taggers that identify the part of speech (e.g., noun, verb"""

# Get the input prompt from the terminal
input_text = input("Please enter your prompt:").strip()
# Implement a security layer later...

# Tokenize the input text
nltk.download('punkt')  # use the punkt tokenizer
tokens = nltk.word_tokenize(input_text)

#  Perform part-of-speech tagging
nltk.download('averaged_perceptron_tagger')
position_tags = nltk.pos_tag(tokens)
