# modules/prompt_templates.py

def get_templates():
    return {
        "Analyse du marché": "Analyse le marché des boissons énergétiques bio en France.",
        "Analyse de la concurrence": "Identifie les principaux concurrents dans le secteur des boissons énergétiques bio.",
        "Tendances du marché": "Quelles sont les tendances actuelles dans le marché des boissons énergétiques bio ?",
    }

# 🧠 Génère des suggestions intelligentes basées sur un prompt utilisateur
from modules.gemini_utils import get_gemini_response

def generate_related_prompts(user_prompt):
    instruction = (
        "Tu es un expert en marketing stratégique. "
        "Génère 5 idées de prompts d'analyse similaires à cette demande, "
        "dans le même ton, pour aller plus loin dans l'analyse :\n\n"
        f"{user_prompt}\n\n"
        "Retourne uniquement une liste propre, sans explication."
    )

    response = get_gemini_response(instruction)

    # Nettoyage : une idée par ligne
    prompts = [line.strip("-• \n") for line in response.split("\n") if line.strip()]
    return prompts[:5]  # Limiter à 5 suggestions
from header import display_header
display_header()