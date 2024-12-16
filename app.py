import streamlit as st
from textblob import TextBlob
import random

# Función para analizar el estado de ánimo del usuario usando TextBlob
def analizar_estado_de_animo(texto_usuario):
    # Crear un objeto TextBlob
    blob = TextBlob(texto_usuario)
    
    # Realizar el análisis de sentimientos
    sentimiento = blob.sentiment.polarity  # Valor entre -1 y 1
    
    # Si la polaridad es positiva, lo consideramos como "POSITIVO"
    if sentimiento > 0:
        estado = "POSITIVE"
    elif sentimiento < 0:
        estado = "NEGATIVE"
    else:
        estado = "NEUTRAL"
    
    # La puntuación de confianza es simplemente la polaridad en este caso
    puntuacion = abs(sentimiento)  # La puntuación debe ser un valor entre 0 y 1
    return estado, puntuacion

# Función para generar recomendaciones sobre cómo hablarle al usuario
def recomendaciones_para_manejo(estado, puntuacion):
    # Definir posibles respuestas dependiendo del estado de ánimo
    if estado == 'POSITIVE':
        recomendaciones = [
            "Mantén el tono positivo y motivador.",
            "Refuerza la confianza y da espacio para compartir más.",
            "Utiliza palabras de ánimo y apoyo."
        ]
        tono = "Puedes hablarle con entusiasmo, manteniendo la conversación ligera y optimista."
    elif estado == 'NEGATIVE':
        recomendaciones = [
            "Escucha activamente sin interrumpir.",
            "Utiliza un tono calmado y tranquilizador.",
            "Evita ser agresivo o presionante."
        ]
        tono = "Es importante ser empático y paciente, mostrándote comprensivo."
    else:
        recomendaciones = [
            "Mantén un tono neutral y amable.",
            "Haz preguntas abiertas para entender mejor la situación.",
            "Evita forzar una respuesta emocional."
        ]
        tono = "Usa un tono calmado y sin presión, tratando de comprender más a fondo la situación."

    # Selecciona una recomendación aleatoria para no ser repetitivo
    recomendacion = random.choice(recomendaciones)

    return tono, recomendacion

# Interfaz de Streamlit
def app():
    st.title("Análisis de Estado de Ánimo del Usuario")

    # Entrada de texto para el usuario
    mensaje_usuario = st.text_area("Escribe un mensaje para analizar su estado de ánimo:")

    if st.button('Analizar Estado de Ánimo'):
        if mensaje_usuario:
            # Analiza el estado de ánimo del texto ingresado
            estado, puntuacion = analizar_estado_de_animo(mensaje_usuario)

            # Muestra el estado de ánimo detectado y la puntuación
            st.write(f"**Estado de ánimo detectado:** {estado} (Puntuación: {puntuacion:.2f})")

            # Obtiene las recomendaciones para manejar la conversación
            tono, recomendacion = recomendaciones_para_manejo(estado, puntuacion)

            # Muestra las recomendaciones
            st.write(f"**Tono recomendado para hablar con el usuario:** {tono}")
            st.write(f"**Recomendación para manejar la conversación:** {recomendacion}")
        else:
            st.warning("Por favor ingresa un mensaje para analizar su estado de ánimo.")

if __name__ == "__main__":
    app()
