import streamlit as st
import pandas as pd

# Titre personnalisé
st.title("Dashboard Analyse Taxis - Suz")

# Chargement des données depuis l'URL Seaborn
url = "https://raw.githubusercontent.com/mwaskom/seaborn-data/master/taxis.csv"
df = pd.read_csv(url)

# Menu déroulant pour choisir un quartier de prise en charge
quartiers = sorted(df["pickup_borough"].dropna().unique())
quartier_choisi = st.selectbox("Choisissez un quartier de prise en charge :", quartiers)

# Filtrage du dataframe selon le quartier choisi
df_filtre = df[df["pickup_borough"] == quartier_choisi]

# Affichage des 5 premières lignes filtrées
st.dataframe(df_filtre.head(5))

# Métrique : nombre total de courses dans ce quartier
st.metric("Nombre total de courses", len(df_filtre))