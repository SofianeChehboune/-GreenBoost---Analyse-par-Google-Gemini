import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Visualisations combinées - GreenBoost")

st.title("📊 Visualisations combinées avec Seaborn & Plotly")

df = sns.load_dataset("tips")

st.subheader("🎨 Visualisation statique avec Seaborn")
st.markdown("Boxplot des pourboires selon le genre")

fig, ax = plt.subplots()
sns.boxplot(x="sex", y="tip", data=df, ax=ax)
st.pyplot(fig)

st.subheader("⚡ Visualisation interactive avec Plotly")
st.markdown("Graphique dynamique de la relation entre le total de la facture et le pourboire")

fig_plotly = px.scatter(
    df,
    x="total_bill",
    y="tip",
    color="sex",
    size="size",
    hover_data=["day", "time"],
    title="Relation entre le montant total et les pourboires"
)
st.plotly_chart(fig_plotly, use_container_width=True)
