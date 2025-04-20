import streamlit as st
import pandas as pd
import plotly.express as px
import seaborn as sns

st.set_page_config(page_title="📊 Tableau de bord - GreenBoost", layout="wide")

# Chargement des données
df = sns.load_dataset("tips")

# Sidebar - Filtres
st.sidebar.header("🔎 Filtres")
selected_day = st.sidebar.multiselect("Jour", options=df["day"].unique(), default=df["day"].unique())
selected_sex = st.sidebar.multiselect("Sexe", options=df["sex"].unique(), default=df["sex"].unique())
selected_time = st.sidebar.radio("Heure", options=df["time"].unique(), index=0)

# Filtrage des données
filtered_df = df[
    (df["day"].isin(selected_day)) &
    (df["sex"].isin(selected_sex)) &
    (df["time"] == selected_time)
]

# En-tête
st.title("📊 Tableau de bord interactif GreenBoost")
st.markdown("Analyse dynamique des pourboires selon le sexe, le jour, et le moment.")

# Layout : 3 colonnes KPIs
col1, col2, col3 = st.columns(3)
col1.metric("💵 Pourboire moyen", f"{filtered_df['tip'].mean():.2f} $")
col2.metric("📦 Total des commandes", f"{len(filtered_df)}")
col3.metric("🧾 Facture moyenne", f"{filtered_df['total_bill'].mean():.2f} $")

# Layout : visualisation
st.markdown("### 📈 Répartition des pourboires")
col4, col5 = st.columns([2, 1])

with col4:
    fig1 = px.histogram(filtered_df, x="tip", color="sex", nbins=20, title="Distribution des pourboires")
    st.plotly_chart(fig1, use_container_width=True)

with col5:
    fig2 = px.box(filtered_df, x="sex", y="tip", color="sex", title="Pourboires par genre")
    st.plotly_chart(fig2, use_container_width=True)

# Graph final
st.markdown("### 💡 Corrélation entre le total de la facture et les pourboires")
fig3 = px.scatter(
    filtered_df,
    x="total_bill",
    y="tip",
    color="sex",
    size="size",
    hover_data=["day", "time"],
    title="Pourboires selon le total de la facture"
)
st.plotly_chart(fig3, use_container_width=True)
