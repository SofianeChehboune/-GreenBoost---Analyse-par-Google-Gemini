# 🔋 GreenBoost Gemini App

Bienvenue sur **GreenBoost Gemini**, une application Streamlit interactive propulsée par **Google Gemini**. Cette application vous permet de générer des résumés, extraire des mots-clés, et explorer du contenu enrichi à partir de vos propres textes.

---

## 🚀 Fonctionnalités / Features

- ✅ Résumés intelligents de texte / Smart Text Summaries  
- ✅ Extraction de mots-clés / Keyword Extraction  
- ✅ Génération de prompts liés / Related Prompt Generation  
- ✅ Personnalisation via un thème élégant (voir `config.toml`) / Customization with an elegant theme (see `config.toml`)  
- ✅ Clé API sécurisée avec `.env` / Secure API Key with `.env`  

---

## 🛠️ Technologies / Technologies

- `Streamlit`  
- `Google Generative AI (Gemini)`  
- `Pandas`  
- `Pillow`  
- `python-dotenv`  

---

## 🔧 Installation locale / Local Installation

1. **Clonez le projet / Clone the project:**

```bash
git clone https://github.com/votre-utilisateur/greenboost-gemini-app.git
cd greenboost-gemini-app
```

2. **Créez un environnement virtuel et activez-le / Create a virtual environment and activate it:**

```bash
python -m venv venv
source venv/bin/activate  # or venv\Scripts\activate on Windows
```

3. **Installez les dépendances / Install the dependencies:**

```bash
pip install -r requirements.txt
```

4. **Ajoutez votre clé API dans un fichier `.env` / Add your API key in a `.env` file:**

```
GOOGLE_API_KEY=VOTRE_CLE_API_ICI / YOUR_API_KEY_HERE
```

5. **Lancez l'application / Run the app:**

```bash
streamlit run streamlit_app.py
```

---

## 📁 Arborescence du projet / Project Directory Structure

```
greenboost-gemini-app/
│
├── streamlit_app.py
├── requirements.txt
├── .env (non partagé / not shared)
├── config.toml
├── modules/
│   ├── gemini_utils.py
│   ├── prompt_templates.py
│   ├── analysis_tools.py
│   └── ui_components.py
└── assets/
    └── (images ou autres ressources / images or other resources)
```

---

## 🌐 Déploiement / Deployment

Pour publier votre app sur [Streamlit Cloud](https://streamlit.io/cloud), veillez à / To deploy your app on [Streamlit Cloud](https://streamlit.io/cloud), make sure to:

- Ajouter `requirements.txt` et `config.toml` / Add `requirements.txt` and `config.toml`
- Configurer votre variable `GOOGLE_API_KEY` dans l’onglet **".env"** / Set your `GOOGLE_API_KEY` in the **".env"** tab
- Définir `streamlit_app.py` comme script principal / Set `streamlit_app.py` as the main script

🎯 App en ligne : [GreenBoost sur Streamlit](https://dtgqb6h4k3yiubmghjsqdp.streamlit.app/)  
🎯 Online App: [GreenBoost on Streamlit](https://dtgqb6h4k3yiubmghjsqdp.streamlit.app/)

---

## 👤 Auteur / Author

**Sofiane Chehboune**  
📧 Contact :  
🔗 [LinkedIn – Sofiane Chehboune](https://www.linkedin.com/in/sofiane-chehboune-5b243766/)  
🔗 [Bluesky](https://bsky.app/profile/sofianepython.bsky.social)  
🔗 [Kaggle](https://www.kaggle.com/sofianechehboune)
