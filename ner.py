import spacy

# Importamos el modelo en español de spacy (debe haberse instalado previamente)
nlp = spacy.load("es_core_news_sm") 

# Ejercicio 2: Reconocimiento de Entidades Nombradas (NER) 
# Identificar nombres de personas, lugares y organizaciones en un texto. 
# Librerías necesarias: spaCy 

# Identifica a Tesla como persona, quizá por el inventor Nikola Tesla
text = "El fundador de Tesla, Elon Musk, ha invertido en inteligencia artificial."

def named_entity_recognition(text, nlp_model):

    processed_text = nlp_model(text)

    for ent in processed_text.ents: # ents devuelve una tupla de las entidades
        print(f"Texto: {ent.text}")
        print(f"  - Tipo: {ent.label_}")  # Persona (PER), lugar (LOC), organización (ORG), etc.
        print(f"  - Inicio token: {ent.start}, Fin token: {ent.end}")
        print()

named_entity_recognition(text=text, nlp_model=nlp)