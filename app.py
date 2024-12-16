import streamlit as st
from transformers import pipeline
import random

# Cargar un modelo más pequeño para análisis de sentimientos (DistilBERT)
sentiment_analyzer = pipeline('sentiment-analysis', model='distilbert-base-uncased-finetuned-sst-2-english')

# Función para analizar el estado de ánimo del usuario
def analizar_estado_de_animo(texto_usuario):
    # Realiza el análisis de sentimientos
    resultado = sentiment_analyzer(texto_usuario)[0]
    etiqueta = resultado['label']
    puntuacion = resultado['score']
    return etiqueta, puntuacion

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
          
