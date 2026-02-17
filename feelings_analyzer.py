from textblob import TextBlob
from googletrans import Translator

# Ejercicio 3: Análisis de Sentimiento
# Determinar si un texto tiene un sentimiento positivo, negativo o neutral. 
# Librerías necesarias: textblob-es 

# Advertencia, para solucionar el problema de la traducción he tenido que emplear una librería que necesita conexión a internet

# Texto de prueba
text = "Me encanta aprender sobre inteligencia artificial, es fascinante."

def translate_from(text, language_origin, language_dest):

    # Crear traductor
    translator = Translator()

    # Traducir a inglés
    translation = translator.translate(text, src=language_origin, dest=language_dest)

    return translation.text

def analyse_feelings(text_to_analyse):

    # Analizar sentimiento con TextBlob en inglés
    blob = TextBlob(text_en)
    feeling = blob.sentiment # Extraemos solo los datos del sentimiento

    print("Polaridad:", feeling.polarity)        # -1 a 1
    print("Subjetividad:", feeling.subjectivity)  # 0 a 1

    # Clasificación simple
    if feeling.polarity > 0:
        print("Sentimiento general: Positivo")
    elif feeling.polarity < 0:
        print("Sentimiento general: Negativo")
    else:
        print("Sentimiento general: Neutral")


text_en = translate_from(text=text, language_origin='es', language_dest='en')
analyse_feelings(text_en)
