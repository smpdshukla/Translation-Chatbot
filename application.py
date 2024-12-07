from flask import Flask, request, jsonify, render_template
import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
from googletrans import Translator
from langdetect import detect


# Initialize NLTK
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')

app = Flask(__name__)

# Language details dictionary for all international languages
language_info = {
    'en': {"name": "English", "region": "Worldwide"},
    'es': {"name": "Spanish", "region": "Spain, Latin America"},
    'fr': {"name": "French", "region": "France, Africa"},
    'de': {"name": "German", "region": "Germany, Austria, Switzerland"},
    'zh': {"name": "Chinese", "region": "China, Taiwan"},
    'ar': {"name": "Arabic", "region": "Middle East, North Africa"},
    'pt': {"name": "Portuguese", "region": "Portugal, Brazil"},
    'ru': {"name": "Russian", "region": "Russia, Central Asia"},
    'ja': {"name": "Japanese", "region": "Japan"},
    'ko': {"name": "Korean", "region": "South Korea, North Korea"},
    'it': {"name": "Italian", "region": "Italy, Switzerland"},
    'nl': {"name": "Dutch", "region": "Netherlands, Belgium"},
    'tr': {"name": "Turkish", "region": "Turkey, Cyprus"},
    'sv': {"name": "Swedish", "region": "Sweden, Finland"},
    'pl': {"name": "Polish", "region": "Poland"},
    'ro': {"name": "Romanian", "region": "Romania, Moldova"},
    'el': {"name": "Greek", "region": "Greece, Cyprus"},
    'th': {"name": "Thai", "region": "Thailand"},
    'vi': {"name": "Vietnamese", "region": "Vietnam"},
    'pa': {"name": "Punjabi", "region": "India, Pakistan"},
    'ta': {"name": "Tamil", "region": "India, Sri Lanka, Singapore"},
    'bn': {"name": "Bengali", "region": "India, Bangladesh"},
    'mr': {"name": "Marathi", "region": "India"},
    'te': {"name": "Telugu", "region": "India"},
    'gu': {"name": "Gujarati", "region": "India"},
    'kn': {"name": "Kannada", "region": "India"},
    'ml': {"name": "Malayalam", "region": "India"},
    'or': {"name": "Odia", "region": "India"},
    'ur': {"name": "Urdu", "region": "Pakistan, India"},
}

# Tokenization function
def tokenize_input(user_input):
    tokens = word_tokenize(user_input)
    stop_words = set(stopwords.words('english'))
    filtered_tokens = [t for t in tokens if t.lower() not in stop_words]
    lemmatizer = WordNetLemmatizer()
    lemmatized_tokens = [lemmatizer.lemmatize(t) for t in filtered_tokens]
    return lemmatized_tokens

# Sentence translation function
def translate_sentence(user_input, target_lang='en'):
    translator = Translator()
    try:
        # Translate the entire sentence to the specified language
        translated = translator.translate(user_input, src='auto', dest=target_lang)
        return translated.text
    except Exception as e:
        # Log and return error message
        print(f"Translation Error: {str(e)}")
        return f"Error: Unable to translate due to {str(e)}"

# Language detection function using langdetect
def detect_language(user_input):
    lang_code = detect(user_input)
    if lang_code in language_info:
        return language_info[lang_code]
    else:
        return {"name": "Unknown", "region": "Unknown"}

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')  # Get user input from request
    target_language = request.json.get('language', 'en')  # Get target language (default is English)

    print(f"User Input: {user_input}")  # Debugging input

    # Tokenize user input
    tokens = tokenize_input(user_input)
    print(f"Tokens: {tokens}")  # Debugging tokens

    # Translate the sentence
    sentence_translation = translate_sentence(user_input, target_language)
    print(f"Translated Sentence: {sentence_translation}")  # Debugging translation

    # Detect language of translated sentence
    translated_lang_info = detect_language(sentence_translation)
    print(f"Translated Language Info: {translated_lang_info}")  # Debugging translated language info

    # Return response with correct translated language info
    return jsonify({
        "tokens": tokens,
        "sentence_translation": sentence_translation,
        "language_info": translated_lang_info  # Provide language info of translated sentence
    })
    
if __name__ == '__main__':
    app.run(debug=True)
