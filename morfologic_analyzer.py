import spacy

# Importamos el modelo en español de spacy (debe haberse instalado previamente)
nlp = spacy.load("es_core_news_sm") 

# Ejercicio 1: Tokenización y Análisis Morfológico 
# Separar un texto en palabras y analizar su estructura gramatical. 
# Librerías necesarias: nltk, spaCy 

def tokenize_with_spacy(text):
    processed_text = nlp(text) # Tokeniza el texto y analiza morfológicamente

    print("Tokenización y análisis morfológico con spaCy:\n")

    for token in processed_text:
        print(f"Palabra: {token.text}") # Imprime el texto original del token
        print(f"  - Lemma: {token.lemma_}") # Devuelve la forma base de la palabra ej: Escribo -> Escribir
        print(f"  - Categoría gramatical (POS): {token.pos_}") # Part of Speech (POS) indica la categoría gramatical
        print(f"  - Etiqueta detallada: {token.tag_}")
        print(f"  - Dependencia sintáctica: {token.dep_}")
        print()

text_to_test = "El procesamiento del lenguaje natural es una rama de la inteligencia artificial."

tokenize_with_spacy(text_to_test)