import streamlit as st
from PIL import Image

def display_header():
    st.title("🔋 GreenBoost - Analyse par Google Gemini")
    
    # ✅ Image avec chemin correct
    try:
        image = Image.open("assets/Kaggle.png")
        st.image(image, use_container_width=True)
    except Exception as e:
        st.warning(f"Erreur lors de l'ouverture de l'image : {e}")
