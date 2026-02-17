import speech_recognition as sr

# Ejercicio 5: Reconocimiento de Voz 
# Convertir audio a texto usando reconocimiento de voz. 
# Librerías necesarias: SpeechRecognition 


# Crear el reconocedor
r = sr.Recognizer()

# Ruta del archivo de audio
audio_file = "Audio.wav"   # Cambia por el nombre de tu archivo


with sr.AudioFile(audio_file) as source:
    audio = r.record(source)  # Lee todo el archivo

try:
    text = r.recognize_google(audio, language="es-ES")
    print("Texto reconocido:")
    print(text)

except sr.UnknownValueError:
    print("No se pudo entender el audio")

except sr.RequestError as e:
    print(f"Error en el servicio: {e}")
