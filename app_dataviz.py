import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

st.set_page_config(page_title="Dashboard vols - Suz", layout="wide")


@st.cache_data
def load_data():
    url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/flights.csv"
    return pd.read_csv(url)


df = load_data()

st.title("Dashboard trafic aérien - Suz")
st.caption("Données : dataset `flights` (Seaborn Data)")

with st.sidebar:
    st.header("Filtres")
    annee_min, annee_max = int(df["year"].min()), int(df["year"].max())
    plage_annees = st.slider(
        "Plage d'années",
        min_value=annee_min,
        max_value=annee_max,
        value=(annee_min, annee_max),
    )
    mois_liste = ["Tous les mois"] + df["month"].unique().tolist()
    mois_choisi = st.selectbox("Mois", mois_liste)

# Filtrage selon les widgets
df_filtre = df[(df["year"] >= plage_annees[0]) & (df["year"] <= plage_annees[1])]
if mois_choisi != "Tous les mois":
    df_filtre = df_filtre[df_filtre["month"] == mois_choisi]

# KPI
st.metric(
    "Total de passagers sur la période",
    f"{df_filtre['passengers'].sum():,}".replace(",", " "),
    border=True,
)

# Graphique 1 : évolution (natif Streamlit)
with st.container(border=True):
    st.subheader("Évolution du nombre de passagers")
    evolution = df_filtre.groupby("year")["passengers"].sum()
    st.line_chart(evolution)

# Graphique 2 : heatmap Seaborn, sur case à cocher
if st.checkbox("Afficher la heatmap année / mois"):
    with st.container(border=True):
        st.subheader("Répartition des passagers par mois et par année")
        pivot = df_filtre.pivot(index="month", columns="year", values="passengers")
        fig, ax = plt.subplots(figsize=(10, 5))
        sns.heatmap(pivot, cmap="Blues", annot=False, ax=ax)
        st.pyplot(fig)

with st.expander("Voir les données brutes filtrées"):
    st.dataframe(df_filtre, hide_index=True)