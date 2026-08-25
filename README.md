# Mon Projet Streamlit — Dashboard d'Analyse de Données

Application web interactive développée avec Streamlit dans le cadre du brief *"Développement et déploiement d'une application Web Data avec Streamlit"* — Formation Data Analyst, Simplon Lyon.

**Contexte** : l'entreprise fictive **DataInsight Solutions** souhaite moderniser la restitution de ses travaux d'analyse via une interface web interactive, versionnée avec Git et hébergée dans le cloud.

## Démo en ligne

- 🚀 **Dashboard commun (projet d'équipe)** : [datainsight-suz-zohair.streamlit.app](https://datainsight-suz-zohair.streamlit.app/)
- 📊 **Application individuelle sécurisée** : [mon-projetapp-suz2026.streamlit.app](https://mon-projetapp-suz2026.streamlit.app/)

## Fonctionnalités

- 🔐 Authentification sécurisée via fichier CSV (`accounts.csv`)
- ✈️ Visualisation interactive du dataset `flights` (Seaborn) : mise en cache des données, filtres dynamiques (plage d'années, mois)
- 📈 Indicateurs clés (KPI) : total de passagers, moyenne mensuelle, mois le plus chargé
- 📊 Graphiques interactifs (évolution annuelle, moyenne par mois) et heatmap Seaborn (répartition mois × année)
- 🖼️ Galerie d'images en disposition 3 colonnes
- 📋 Menu latéral de navigation (`streamlit-option-menu`)

**Note** : `app_taxis.py` contient une exploration additionnelle sur le dataset `taxis`, indépendante de l'application principale déployée.

## Structure du projet

```
mon-projetstreamlit/
├── app.py              # Première application Streamlit (Guide 3)
├── app_taxis.py         # Analyse du dataset taxis (exercice Guide 3)
├── app_dataviz.py        # Visualisations interactives dataset flights (Guide 4)
├── app_securisee.py       # Version avec authentification, navigation et galerie (Guide 5)
├── app_dashboard.py        # Dashboard complet : auth + filtres + KPI + graphiques + galerie (Guide 6)
├── accounts.csv           # Identifiants utilisateurs (démo pédagogique)
├── requirements.txt         # Dépendances Python
└── .gitignore              # Fichiers exclus du dépôt (venv, cache...)
```

## Installation et lancement en local

**Prérequis** : Python 3.10 à 3.12

```bash
# 1. Cloner le dépôt
git clone https://github.com/suzy5670/mon-projetstreamlit.git
cd mon-projetstreamlit

# 2. Créer et activer l'environnement virtuel
python -m venv venv

# Sous Windows (PowerShell) :
.\venv\Scripts\Activate.ps1
# Sous macOS/Linux :
source venv/bin/activate

# 3. Installer les dépendances
python -m pip install -r requirements.txt

# 4. Lancer l'application
python -m streamlit run app_securisee.py
```

L'application s'ouvre automatiquement dans le navigateur à l'adresse `http://localhost:8501`.

**Identifiants de démonstration** : `admin` / `admin123` ou `utilisateur` / `mdp123`.

## Auteure

**Suz Didolène Massamouna** — Data Analyst
🌐 [Portfolio](https://suzy5670.github.io/) · 🔗 [LinkedIn](https://www.linkedin.com/in/suz-didolene-massamouna/) · 💻 [GitHub](https://github.com/suzy5670)

Projet réalisé en binôme avec **Zohair Nazhaoui** — [Portfolio](https://zohair69.github.io/) · [GitHub](https://github.com/Zohair69)
