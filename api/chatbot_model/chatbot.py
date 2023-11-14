import random
import json
import pickle
import numpy as np
import os

import nltk
from nltk.stem import WordNetLemmatizer

from keras.models import load_model

def setup_nltk():
    nltk.download('punkt')
    nltk.download('wordnet')
#Importamos los archivos generados en el código anterior

#Pasamos las palabras de oración a su forma raíz
def clean_up_sentence(sentence):
    lemmatizer = WordNetLemmatizer()
    sentence_words = nltk.word_tokenize(sentence)
    sentence_words = [lemmatizer.lemmatize(word) for word in sentence_words]
    return sentence_words

#Convertimos la información a unos y ceros según si están presentes en los patrones
def bag_of_words(sentence):
    words = pickle.load(open(f'{os.path.dirname(os.path.abspath(__file__))}/words.pkl', 'rb'))
    sentence_words = clean_up_sentence(sentence)
    bag = [0]*len(words)
    for w in sentence_words:
        for i, word in enumerate(words):
            if word == w:
                bag[i]=1
    return np.array(bag)

#Predecimos la categoría a la que pertenece la oración
def predict_class(sentence):
    classes = pickle.load(open(f'{os.path.dirname(os.path.abspath(__file__))}/classes.pkl', 'rb'))
    model = load_model(f'{os.path.dirname(os.path.abspath(__file__))}/chatbot_model.keras')
    bow = bag_of_words(sentence)
    res = model.predict(np.array([bow]))[0]
    max_index = np.where(res ==np.max(res))[0][0]
    category = classes[max_index]
    return category

#Obtenemos una respuesta aleatoria
def get_response(tag, intents_json):
    list_of_intents = intents_json['intents']
    result = ""
    for i in list_of_intents:
        if i["tag"]==tag:
            result = random.choice(i['responses'])
            break
    return result

def ai_chat(message):
    os.environ['CUDA_VISIBLE_DEVICES'] = '-1'
    setup_nltk()
    intents = json.loads(open(f'{os.path.dirname(os.path.abspath(__file__))}/intents.json').read())
    
    
    
    ints=predict_class(message)
    res=get_response(ints, intents)
    return res