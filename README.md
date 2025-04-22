# 🔋 GreenBoost Gemini App

Bienvenue sur **GreenBoost Gemini**, une application Streamlit interactive propulsée par **Google Gemini**. Cette application vous permet de générer des résumés, extraire des mots-clés, et explorer du contenu enrichi à partir de vos propres textes.

---

## 🚀 Fonctionnalités

- ✅ Résumés intelligents de texte  
- ✅ Extraction de mots-clés  
- ✅ Génération de prompts liés  
- ✅ Personnalisation via un thème élégant (voir `config.toml`)  
- ✅ Clé API sécurisée avec `.env`  

---

## 🛠️ Technologies

- `Streamlit`  
- `Google Generative AI (Gemini)`  
- `Pandas`  
- `Pillow`  
- `python-dotenv`  

---

## 🔧 Installation locale

1. **Clonez le projet :**

```bash
git clone https://github.com/votre-utilisateur/greenboost-gemini-app.git
cd greenboost-gemini-app
```

2. **Créez un environnement virtuel et activez-le :**

```bash
python -m venv venv
source venv/bin/activate  # ou venv\Scripts\activate sur Windows
```

3. **Installez les dépendances :**

```bash
pip install -r requirements.txt
```

4. **Ajoutez votre clé API dans un fichier `.env` :**

```
GOOGLE_API_KEY=VOTRE_CLE_API_ICI
```

5. **Lancez l'application :**

```bash
streamlit run streamlit_app.py
```

---

## 📁 Arborescence du projet

```
greenboost-gemini-app/
│
├── streamlit_app.py
├── requirements.txt
├── .env (non partagé)
├── config.toml
├── modules/
│   ├── gemini_utils.py
│   ├── prompt_templates.py
│   ├── analysis_tools.py
│   └── ui_components.py
└── assets/
    └── (images ou autres ressources)
```

---

## 🌐 Déploiement

Pour publier votre app sur [Streamlit Cloud](https://streamlit.io/cloud), veillez à :

- Ajouter `requirements.txt` et `config.toml`
- Configurer votre variable `GOOGLE_API_KEY` dans l’onglet **".env"**
- Définir `streamlit_app.py` comme script principal

🎯 App en ligne : [GreenBoost sur Streamlit](https://dtgqb6h4k3yiubmghjsqdp.streamlit.app/)

---

## 👤 Auteur

**Sofiane Chehboune**  
📧 Contact :
🔗 [LinkedIn – Sofiane Chehboune](https://www.linkedin.com/in/sofiane-chehboune-5b243766/)   
🔗 [Bluesky](https://bsky.app/profile/sofianepython.bsky.social)
🔗[kaggle](https://www.kaggle.com/sofianechehboune)
 
