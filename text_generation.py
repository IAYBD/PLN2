# Ejercicio 6: Generación de Texto con un Modelo 

# Preentrenado (GPT-2) 
# Generar texto automáticamente a partir de una entrada inicial. 
# Librerías necesarias: transformers 

from transformers import pipeline

# Crear pipeline de generación de texto
generator = pipeline("text-generation", model="gpt2")

# Texto inicial
prompt = "La inteligencia artificial está transformando el mundo porque"

# Generar texto
resultado = generator(
    prompt,
    max_length=80,
    num_return_sequences=1,
    temperature=0.7
)

# Mostrar resultado
print("Texto generado:\n")
print(resultado[0]["generated_text"])