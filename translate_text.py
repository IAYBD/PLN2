from googletrans import Translator

# Ejercicio 4: Traducción Automática 
# Traducir un texto del español al inglés. 
# Librerías necesarias: googletrans 

def translate_from(text, language_origin, language_dest):

    # Crear traductor
    translator = Translator()

    # Traducir a inglés
    translation = translator.translate(text, src=language_origin, dest=language_dest)

    return translation.text

text = "El aprendizaje profundo está revolucionando el procesamiento del lenguaje natural."

transalted_text = translate_from(text, language_origin='es', language_dest='en')

print(transalted_text)