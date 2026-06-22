# =============================================================================
# VISUALISATION DES DONNÉES – Semaine 2, Jour 4
# Formation IA & Machine Learning – Sira Labs / Developers Institute
# Dataset : Student Mental Health
# =============================================================================

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Style global
plt.rcParams['figure.facecolor'] = 'white'
plt.rcParams['axes.facecolor']   = '#f9f9f9'
plt.rcParams['font.family']      = 'DejaVu Sans'
sns.set_theme(style="whitegrid")

# =============================================================================
# EXERCICE 1 – Importance de la visualisation des données
# =============================================================================

print("=" * 60)
print("  EXERCICE 1 : Importance de la visualisation des données")
print("=" * 60)

print("""
📌 Pourquoi la visualisation est-elle importante ?
──────────────────────────────────────────────────
La visualisation des données permet de :
  • Révéler rapidement des tendances et des patterns
    qu'il serait difficile de détecter dans un tableau brut.
  • Communiquer des résultats complexes de façon intuitive
    et accessible à tous les publics.
  • Identifier des anomalies (outliers) et des valeurs aberrantes.
  • Faciliter la prise de décision grâce à une compréhension
    visuelle immédiate des données.
  • Comparer des distributions, des groupes et des évolutions
    dans le temps en un coup d'œil.

📌 À quoi sert un graphique linéaire ?
──────────────────────────────────────
Un graphique linéaire (line chart) est idéal pour :
  • Représenter l'évolution d'une variable continue dans le temps
    (séries temporelles : températures, ventes, cours boursiers).
  • Montrer des tendances à la hausse, à la baisse ou des cycles.
  • Comparer plusieurs séries sur la même échelle temporelle.
  → En résumé : on l'utilise chaque fois que l'axe X représente
    un ordre continu (temps, distance, étapes).
""")

# =============================================================================
# EXERCICE 2 – Graphique linéaire : variation de température
# =============================================================================

print("=" * 60)
print("  EXERCICE 2 : Graphique linéaire – Températures sur une semaine")
print("=" * 60)

jours         = ['Lun', 'Mar', 'Mer', 'Jeu', 'Ven', 'Sam', 'Dim']
temperatures  = [72, 74, 76, 80, 82, 78, 75]

fig, ax = plt.subplots(figsize=(8, 4))
ax.plot(jours, temperatures,
        marker='o', color='steelblue', linewidth=2.5,
        markersize=8, markerfacecolor='white', markeredgewidth=2)

# Annotation de chaque point
for i, (j, t) in enumerate(zip(jours, temperatures)):
    ax.annotate(f'{t}°F', xy=(i, t), xytext=(0, 10),
                textcoords='offset points', ha='center',
                fontsize=9, color='steelblue')

ax.set_xlabel('Jour', fontsize=12)
ax.set_ylabel('Température (°F)', fontsize=12)
ax.set_title('Variation de température sur une semaine', fontsize=14, fontweight='bold')
ax.set_ylim(68, 88)
plt.tight_layout()
plt.savefig('ex2_temperature.png', dpi=120, bbox_inches='tight')
plt.show()
print("✅ Graphique sauvegardé : ex2_temperature.png\n")

# =============================================================================
# EXERCICE 3 – Graphique à barres : ventes mensuelles
# =============================================================================

print("=" * 60)
print("  EXERCICE 3 : Graphique à barres – Ventes mensuelles")
print("=" * 60)

mois   = ['Janvier', 'Février', 'Mars', 'Avril', 'Mai']
ventes = [5000, 5500, 6200, 7000, 7500]
colors = sns.color_palette("Blues_d", len(mois))

fig, ax = plt.subplots(figsize=(8, 4))
bars = ax.bar(mois, ventes, color=colors, edgecolor='white', linewidth=0.8)

# Valeur au-dessus de chaque barre
for bar, v in zip(bars, ventes):
    ax.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 60,
            f'${v:,}', ha='center', va='bottom', fontsize=9, fontweight='bold')

ax.set_xlabel('Mois', fontsize=12)
ax.set_ylabel('Montant des ventes ($)', fontsize=12)
ax.set_title('Ventes mensuelles du magasin de détail', fontsize=14, fontweight='bold')
ax.yaxis.set_major_formatter(plt.FuncFormatter(lambda x, _: f'${x:,.0f}'))
ax.set_ylim(0, 8500)
plt.tight_layout()
plt.savefig('ex3_ventes.png', dpi=120, bbox_inches='tight')
plt.show()
print("✅ Graphique sauvegardé : ex3_ventes.png\n")

# =============================================================================
# CHARGEMENT DU DATASET STUDENT MENTAL HEALTH
# =============================================================================

df = pd.read_csv('Student Mental health.csv')

# Nettoyage minimal
df.columns = df.columns.str.strip()
df['What is your CGPA?'] = df['What is your CGPA?'].str.strip()

print(f"✅ Dataset chargé : {df.shape[0]} étudiants, {df.shape[1]} colonnes\n")

# =============================================================================
# EXERCICE 4 – Histogramme : distribution des CGPA
# =============================================================================

print("=" * 60)
print("  EXERCICE 4 : Histogramme – Distribution des CGPA")
print("=" * 60)

# Ordre logique des catégories CGPA
cgpa_order = ['0 - 1.99', '2.00 - 2.49', '2.50 - 2.99',
              '3.00 - 3.49', '3.50 - 4.00']

# Filtrer les valeurs reconnues
df_cgpa = df[df['What is your CGPA?'].isin(cgpa_order)].copy()

fig, ax = plt.subplots(figsize=(8, 5))
sns.countplot(
    data=df_cgpa,
    x='What is your CGPA?',
    order=cgpa_order,
    color='#4C72B0',
    edgecolor='white',
    linewidth=0.8,
    ax=ax
)

ax.set_xlabel('Catégorie de CGPA', fontsize=12)
ax.set_ylabel("Nombre d'étudiants", fontsize=12)
ax.set_title('Distribution des moyennes cumulatives (CGPA) des étudiants',
             fontsize=14, fontweight='bold')

# Compte sur chaque barre
for p in ax.patches:
    if p.get_height() > 0:
        ax.text(p.get_x() + p.get_width()/2, p.get_height() + 0.3,
                str(int(p.get_height())), ha='center', va='bottom',
                fontsize=10, fontweight='bold')

plt.tight_layout()
plt.savefig('ex4_cgpa_histogramme.png', dpi=120, bbox_inches='tight')
plt.show()
print("✅ Graphique sauvegardé : ex4_cgpa_histogramme.png\n")

# =============================================================================
# EXERCICE 5 – Graphique à barres : anxiété selon le genre
# =============================================================================

print("=" * 60)
print("  EXERCICE 5 : Barres groupées – Anxiété selon le genre")
print("=" * 60)

fig, ax = plt.subplots(figsize=(7, 5))
sns.countplot(
    data=df,
    x='Choose your gender',
    hue='Do you have Anxiety?',
    palette={'Yes': '#E74C3C', 'No': '#2ECC71'},
    edgecolor='white',
    ax=ax
)

ax.set_xlabel('Genre', fontsize=12)
ax.set_ylabel("Nombre d'étudiants", fontsize=12)
ax.set_title("Niveaux d'anxiété selon le genre", fontsize=14, fontweight='bold')
ax.legend(title='Anxiété', title_fontsize=10, labels=['Non', 'Oui'])

# Valeurs sur barres
for p in ax.patches:
    if p.get_height() > 0:
        ax.text(p.get_x() + p.get_width()/2, p.get_height() + 0.2,
                str(int(p.get_height())), ha='center', va='bottom', fontsize=9)

plt.tight_layout()
plt.savefig('ex5_anxiete_genre.png', dpi=120, bbox_inches='tight')
plt.show()

# Statistiques
print("📊 Tableau de répartition :")
print(pd.crosstab(df['Choose your gender'], df['Do you have Anxiety?']))
print("✅ Graphique sauvegardé : ex5_anxiete_genre.png\n")

# =============================================================================
# EXERCICE 6 – Nuage de points : âge vs crises de panique
# =============================================================================

print("=" * 60)
print("  EXERCICE 6 : Scatter plot – Âge et crises de panique")
print("=" * 60)

# Encodage Oui=1 / Non=0
df['Panic_Num'] = df['Do you have Panic attack?'].map({'Yes': 1, 'No': 0})

fig, ax = plt.subplots(figsize=(9, 5))

# Jitter vertical léger pour éviter la superposition
np.random.seed(42)
jitter = np.random.uniform(-0.05, 0.05, size=len(df))

sns.scatterplot(
    data=df,
    x='Age',
    y=df['Panic_Num'] + jitter,
    hue='Do you have Panic attack?',
    palette={'Yes': '#E74C3C', 'No': '#3498DB'},
    alpha=0.7,
    s=70,
    edgecolor='white',
    ax=ax
)

ax.set_xlabel('Âge (années)', fontsize=12)
ax.set_ylabel('Crise de panique (0 = Non, 1 = Oui)', fontsize=12)
ax.set_title('Relation entre l\'âge et les crises de panique', fontsize=14, fontweight='bold')
ax.set_yticks([0, 1])
ax.set_yticklabels(['Non (0)', 'Oui (1)'])
ax.legend(title='Crise de panique', title_fontsize=10)

# Ligne de proportion par âge
age_prop = df.groupby('Age')['Panic_Num'].mean()
ax2 = ax.twinx()
ax2.plot(age_prop.index, age_prop.values,
         color='orange', linewidth=2, linestyle='--',
         marker='D', markersize=4, alpha=0.8, label='Proportion (%)')
ax2.set_ylabel('Proportion avec crises (%)', color='orange', fontsize=10)
ax2.tick_params(axis='y', labelcolor='orange')
ax2.set_ylim(-0.2, 1.4)

plt.tight_layout()
plt.savefig('ex6_age_paniques.png', dpi=120, bbox_inches='tight')
plt.show()

print("📊 Statistiques par âge :")
print(df.groupby('Age')['Panic_Num'].agg(['sum', 'count', 'mean'])
        .rename(columns={'sum':'Avec crises', 'count':'Total', 'mean':'Proportion'})
        .round(2))
print("✅ Graphique sauvegardé : ex6_age_paniques.png\n")

# =============================================================================
# RÉCAPITULATIF
# =============================================================================

print("=" * 60)
print("  RÉCAPITULATIF DES EXERCICES")
print("=" * 60)
print("""
  ✅ Ex 1 – Explication théorique (visualisation + graphique linéaire)
  ✅ Ex 2 – Graphique linéaire : températures sur une semaine
  ✅ Ex 3 – Graphique à barres : ventes mensuelles
  ✅ Ex 4 – Histogramme Seaborn : distribution CGPA (dataset)
  ✅ Ex 5 – Countplot Seaborn : anxiété selon le genre (dataset)
  ✅ Ex 6 – Scatter plot Seaborn : âge vs crises de panique (dataset)

  Fichiers générés :
    ex2_temperature.png
    ex3_ventes.png
    ex4_cgpa_histogramme.png
    ex5_anxiete_genre.png
    ex6_age_paniques.png
""")
