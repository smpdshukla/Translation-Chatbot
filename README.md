# Translation-Chatbot
The Translation Chatbot is a natural language processing (NLP) based application designed to assist users in translating text between multiple languages and detecting the language of the input text. The chatbot also provides insights into tokenized input, filtering out unnecessary words (stopwords) and lemmatizing them for better text understanding. This project demonstrates a combination of Flask for backend support, Google Translate API for translations, and language detection for robust multilingual communication.The Translation Chatbot makes it easy to communicate across languages by accurately translating text into multiple supported languages. It can also detect the language of the input text automatically, saving users the effort of specifying it. Beyond translation, the chatbot enhances text analysis by breaking sentences into tokens, filtering out common words, and simplifying words to their root form. 
How It Works:
1.Users send input text via API requests.
2.The app processes the text to:
 Tokenize the input.
 Detect the source language.
 Translate the text to the target language.
3.The response includes:
 Tokenized and lemmatized words.
 Translated text.
 Information about the detected language.
 Technologies used:
1.Python(Core language)
2.Flask(Backend Framework)
3.NLTK (Natural Language Toolkit)
4.Googletrans: For translation services, enabling multi-language support.
5.Langdetect: For automatic language detection of input text.
