import google.generativeai as genai
import os
from dotenv import load_dotenv

# Charger les variables d'environnement depuis le fichier .env
load_dotenv()

# Lire la clé API depuis la variable d'environnement
api_key = os.getenv("GOOGLE_API_KEY")

# Configuration de l'API avec la clé
genai.configure(api_key=api_key)

# Initialisation du modèle
model = genai.GenerativeModel(
    model_name="gemini-1.5-flash-latest",
    generation_config={
        "temperature": 0.7,
        "top_p": 1,
        "top_k": 1,
        "max_output_tokens": 2048,
    }
)

def get_gemini_response(prompt):
    """Générer une réponse à partir du modèle Google Gemini pour un prompt donné."""
    
    # Vérification que le prompt n'est pas vide
    if not prompt.strip():  # Vérifie si le prompt est vide ou contient uniquement des espaces
        raise ValueError("Le prompt ne peut pas être vide.")

    try:
        response = model.generate_content(prompt)
        return response.text
    except Exception as e:
        raise RuntimeError(f"Erreur lors de la génération de la réponse: {e}")
