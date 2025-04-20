# ✅ Configuration de la page Streamlit (doit être la première commande)
import streamlit as st
st.set_page_config(page_title="GreenBoost Gemini App", layout="wide", page_icon="🔋")

# Importations des modules
import pandas as pd
from PIL import Image
from modules.gemini_utils import get_gemini_response
from modules.prompt_templates import get_templates, generate_related_prompts
from modules.analysis_tools import summarize_text, extract_keywords
from modules.ui_components import show_footer

# ✅ Affichage de l'image de bannière (une seule fois)
banner_path = "assets/Kaggle.png"
if 'banner_shown' not in st.session_state:
    try:
        banner_image = Image.open(banner_path)
        st.image(banner_image, use_container_width=True)
        st.session_state.banner_shown = True
    except Exception as e:
        st.warning(f"❌ Impossible d'afficher l'image : {e}")

# ✅ Chargement du style CSS
st.markdown("<style>" + open("style.css").read() + "</style>", unsafe_allow_html=True)

# ✅ Menu latéral
st.sidebar.image("assets/logo.png", use_container_width=True)  # Logo de ton app si tu en as un

st.sidebar.markdown("## 🧭 Navigation")
section = st.sidebar.radio("Choisissez une section :", (
    "🏠 Accueil",
    "🎯 Analyse personnalisée",
    "💡 Suggestions génériques",
    "📁 Analyse d’un fichier CSV",
    "ℹ️ À propos"
))

st.sidebar.markdown("---")
st.sidebar.markdown("🧪 *Propulsé par Google Gemini*")
st.sidebar.markdown("🔋 **GreenBoost** - Data x IA")
st.sidebar.markdown("[📎 Mon profil LinkedIn](https://www.linkedin.com/in/sofiane-chehboune-5b243766/)")

# ✅ Affichage conditionnel selon la section
if section == "🏠 Accueil":
    st.title("🔋 GreenBoost - Analyse par Google Gemini")
    st.markdown("Explorez le marché des **boissons énergétiques bio** grâce à l’intelligence artificielle.")

    st.markdown("""
    ## 🧠 Formation Google x Kaggle – GenAI Intensive

    Cette application est le fruit de ma participation à la formation intensive **GenAI** organisée par **Google Cloud** et **Kaggle**.
    
    Pendant 5 jours, j’ai développé un projet autour de l’analyse du marché des boissons énergétiques bio avec **Google Gemini** et des outils avancés de la data science.
    """)





    # 🔗 Liens utiles
    st.markdown("### 🔗 Liens utiles")
    st.markdown("- 📘 [Notebook Kaggle du projet](https://www.kaggle.com/code/sofianechehboune/project-data-genai-2025q1-with-google-gemini)")
    st.markdown("- 🏁 [Compétition Capstone Kaggle](https://www.kaggle.com/competitions/gen-ai-intensive-course-capstone-2025q1)")

    # 📄 Bouton de téléchargement du PDF
    pdf_path = "assets/formation_google_kaggle_genai.pdf"
    try:
        with open(pdf_path, "rb") as pdf_file:
            st.download_button(
                label="📄 Télécharger le résumé PDF",
                data=pdf_file,
                file_name="Formation_Google_GenAI.pdf",
                mime="application/pdf"
            )
    except FileNotFoundError:
        st.info("📎 Le fichier PDF de résumé sera bientôt disponible.")

    st.success("🚀 Commencez à interagir avec l’IA depuis le menu à gauche.")

    
elif section == "🎯 Analyse personnalisée":
    st.markdown("## 🎯 Analyse personnalisée")
    prompt = st.text_area("✍️ Saisissez votre prompt :", height=200)

    if st.button("Lancer l'analyse"):
        with st.spinner("Analyse en cours..."):
            output = get_gemini_response(prompt)
            st.subheader("🧠 Résultat de l'IA")
            st.markdown(output)

            st.markdown("### 🤖 Suggestions basées sur votre sujet")
            suggestions = generate_related_prompts(prompt)

            for i, suggestion in enumerate(suggestions):
                if st.button(f"Suggestion {i+1} : {suggestion}"):
                    with st.spinner("Analyse enrichie en cours..."):
                        suggestion_output = get_gemini_response(suggestion)
                        st.subheader(f"📌 Analyse enrichie pour : {suggestion}")
                        st.markdown(suggestion_output)

                        col1, col2 = st.columns(2)
                        with col1:
                            st.markdown("### 📌 Résumé")
                            st.markdown(summarize_text(suggestion_output))
                        with col2:
                            st.markdown("### 🔑 Mots-clés")
                            st.markdown(", ".join(extract_keywords(suggestion_output)))

elif section == "💡 Suggestions génériques":
    st.markdown("## 💡 Suggestions génériques")
    templates = get_templates()
    option = st.selectbox("Choisissez un type d'analyse :", list(templates.keys()))
    auto_prompt = templates[option]

    if st.button("Lancer l'analyse enrichie (suggestion générique)"):
        with st.spinner("Analyse enrichie avec IA..."):
            auto_output = get_gemini_response(auto_prompt)
            st.subheader("🧠 Résultat enrichi de l'IA")
            st.markdown(auto_output)

            st.markdown("### 📌 Résumé")
            st.markdown(summarize_text(auto_output))
            st.markdown("### 🔑 Mots-clés")
            st.markdown(", ".join(extract_keywords(auto_output)))

elif section == "📁 Analyse d’un fichier CSV":
    st.markdown("## 📁 Téléversement d'un fichier CSV")
    fichier_televerse = st.file_uploader("Sélectionnez un fichier au format .csv", type=["csv"])
    df_fichier = None

    if fichier_televerse is not None:
        df_fichier = pd.read_csv(fichier_televerse)
        st.markdown("### 📄 Aperçu du fichier CSV")
        st.dataframe(df_fichier.head())

        st.markdown("### ℹ️ Informations sur le fichier")
        st.write(df_fichier.info())

        st.markdown("### 📊 Statistiques descriptives")
        st.write(df_fichier.describe())

        if st.button("Lancer l’analyse statistique"):
            with st.spinner("Analyse en cours..."):
                st.markdown("### 🔢 Analyse statistique de base")
                df_fichier_numeric = df_fichier.select_dtypes(include=['number'])
                moyenne = df_fichier_numeric.mean()
                ecart_type = df_fichier_numeric.std()

                st.markdown("#### Moyenne des colonnes numériques")
                st.write(moyenne)

                st.markdown("#### Écart-type des colonnes numériques")
                st.write(ecart_type)

elif section == "ℹ️ À propos":
    st.markdown("## ℹ️ À propos de cette application")
    st.markdown("""
    **GreenBoost** est une application conçue pour explorer le marché des boissons énergétiques bio à l’aide de l’IA.
    
    🔍 Utilisez Google Gemini pour générer des insights et résumés pertinents.  
    📁 Analysez vos propres fichiers CSV.  
    🤖 Obtenez des suggestions intelligentes à partir d’un prompt ou d’un modèle.  
    
    **Développée par Sofiane Chehboune**  
    👉 [LinkedIn](https://www.linkedin.com/in/sofiane-chehboune-5b243766/)
    """)

# ✅ Pied de page
if 'footer_shown' not in st.session_state:
    show_footer()
    st.session_state.footer_shown = True
