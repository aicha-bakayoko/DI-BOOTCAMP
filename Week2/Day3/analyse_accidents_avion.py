# =============================================================================
# ANALYSE DES ACCIDENTS D'AVION ET DÉCÈS JUSQU'EN 2023
# Semaine 2, Jour 3 - SciPy et Statistiques de Base
# Formation IA & Machine Learning - Sira Labs / Developers Institute
# =============================================================================

import pandas as pd
import numpy as np
from scipy import stats
import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import seaborn as sns
import warnings
warnings.filterwarnings('ignore')

# Configuration du style global
plt.style.use('seaborn-v0_8-whitegrid')
sns.set_palette("husl")

# =============================================================================
# 1. IMPORTATION ET NETTOYAGE DES DONNÉES
# =============================================================================

print("=" * 60)
print("  ANALYSE DES ACCIDENTS D'AVION (jusqu'en 2023)")
print("=" * 60)

# --- Chargement du dataset ---
# Source : https://www.kaggle.com/datasets/cgurkan/airplane-crash-data-since-1908
# Fichier attendu : "Airplane_Crashes_and_Fatalities_Since_1908.csv"

try:
    df = pd.read_csv("Airplane_Crashes_and_Fatalities_Since_1908.csv",
                     encoding='latin-1')
    print(f"\n✅ Dataset chargé : {df.shape[0]} lignes, {df.shape[1]} colonnes")
except FileNotFoundError:
    print("⚠️  Fichier non trouvé. Veuillez télécharger le dataset Kaggle.")
    print("   URL : https://www.kaggle.com/datasets/cgurkan/airplane-crash-data-since-1908")
    raise

# --- Aperçu initial ---
print("\n📋 Colonnes disponibles :")
print(df.columns.tolist())

print("\n📊 Premières lignes :")
print(df.head(3).to_string())

print("\n🔍 Valeurs manquantes par colonne :")
print(df.isnull().sum())

# --- Nettoyage des données ---

# Conversion de la date
df['Date'] = pd.to_datetime(df['Date'], errors='coerce')
df.dropna(subset=['Date'], inplace=True)

# Extraction de l'année et de la décennie
df['Year']   = df['Date'].dt.year
df['Decade'] = (df['Year'] // 10) * 10

# Nettoyage des colonnes numériques
for col in ['Fatalities', 'Aboard', 'Ground']:
    df[col] = pd.to_numeric(df[col], errors='coerce')

# Calcul du taux de survie
df['Survivors']      = df['Aboard'] - df['Fatalities']
df['Survivors']      = df['Survivors'].clip(lower=0)
df['Survival_Rate']  = np.where(
    df['Aboard'] > 0,
    (df['Survivors'] / df['Aboard']) * 100,
    np.nan
)

# Extraction de la région (premier mot du lieu)
df['Region'] = df['Location'].astype(str).str.split(',').str[-1].str.strip()

print(f"\n✅ Après nettoyage : {df.shape[0]} lignes valides")
print(f"   Période couverte : {df['Year'].min()} – {df['Year'].max()}")

# =============================================================================
# 2. ANALYSE EXPLORATOIRE DES DONNÉES (EDA)
# =============================================================================

print("\n" + "=" * 60)
print("  2. ANALYSE EXPLORATOIRE")
print("=" * 60)

# --- Statistiques globales ---
total_accidents  = len(df)
total_fatalities = df['Fatalities'].sum()
total_aboard     = df['Aboard'].sum()
global_survival  = ((total_aboard - total_fatalities) / total_aboard * 100) \
                   if total_aboard > 0 else 0

print(f"\n📌 Statistiques globales :")
print(f"   Nombre total d'accidents  : {total_accidents:,}")
print(f"   Total décès               : {total_fatalities:,.0f}")
print(f"   Total passagers à bord    : {total_aboard:,.0f}")
print(f"   Taux de survie global     : {global_survival:.1f}%")

# --- Statistiques par décennie ---
decade_stats = df.groupby('Decade').agg(
    Accidents    = ('Fatalities', 'count'),
    Décès        = ('Fatalities', 'sum'),
    Taux_survie  = ('Survival_Rate', 'mean')
).reset_index()

print("\n📈 Accidents et décès par décennie :")
print(decade_stats.to_string(index=False))

# --- Top 10 régions les plus touchées ---
top_regions = (df.groupby('Region')['Fatalities']
                 .sum()
                 .nlargest(10)
                 .reset_index())
print("\n🌍 Top 10 régions – total décès :")
print(top_regions.to_string(index=False))

# =============================================================================
# 3. ANALYSE STATISTIQUE AVEC SCIPY
# =============================================================================

print("\n" + "=" * 60)
print("  3. ANALYSE STATISTIQUE (SciPy)")
print("=" * 60)

# --- 3a. Statistiques descriptives sur les décès ---
fat = df['Fatalities'].dropna()

print("\n📐 Statistiques descriptives – Décès par accident :")
print(f"   Moyenne          : {fat.mean():.2f}")
print(f"   Médiane          : {fat.median():.2f}")
print(f"   Écart-type       : {fat.std():.2f}")
print(f"   Min / Max        : {fat.min():.0f} / {fat.max():.0f}")
print(f"   Asymétrie (skew) : {stats.skew(fat):.3f}")
print(f"   Kurtosis         : {stats.kurtosis(fat):.3f}")

# --- 3b. Test d'hypothèse – ANOVA entre décennies ---
# H0 : les moyennes de décès sont identiques entre les décennies
# H1 : au moins une décennie diffère significativement

decade_groups = [
    grp['Fatalities'].dropna().values
    for _, grp in df.groupby('Decade')
    if len(grp['Fatalities'].dropna()) >= 5
]

f_stat, p_value = stats.f_oneway(*decade_groups)

print("\n📊 Test ANOVA – Décès moyens par décennie :")
print(f"   Statistique F    : {f_stat:.4f}")
print(f"   p-value          : {p_value:.6f}")
if p_value < 0.05:
    print("   ✅ Résultat : Différence SIGNIFICATIVE (p < 0.05)")
    print("      → On rejette H0 : les décès varient entre les décennies.")
else:
    print("   ℹ️  Résultat : Pas de différence significative (p ≥ 0.05)")

# --- 3c. Régression linéaire – évolution des accidents dans le temps ---
yearly = df.groupby('Year').agg(
    Accidents   = ('Fatalities', 'count'),
    Décès_total = ('Fatalities', 'sum')
).reset_index()

slope, intercept, r_value, p_val_reg, std_err = stats.linregress(
    yearly['Year'], yearly['Accidents']
)

print("\n📉 Régression linéaire – Accidents par année :")
print(f"   Pente (slope)    : {slope:.4f} accidents/an")
print(f"   Ordonnée (b)     : {intercept:.2f}")
print(f"   R²               : {r_value**2:.4f}")
print(f"   p-value          : {p_val_reg:.6f}")
if p_val_reg < 0.05:
    direction = "hausse" if slope > 0 else "baisse"
    print(f"   ✅ Tendance significative à la {direction} du nombre d'accidents.")

# --- 3d. Intervalle de confiance à 95% sur les décès ---
ci = stats.t.interval(
    0.95,
    df=len(fat) - 1,
    loc=fat.mean(),
    scale=stats.sem(fat)
)
print(f"\n📏 Intervalle de confiance 95% – décès moyen :")
print(f"   [{ci[0]:.2f} ; {ci[1]:.2f}]")

# =============================================================================
# 4. VISUALISATIONS
# =============================================================================

print("\n" + "=" * 60)
print("  4. CRÉATION DES VISUALISATIONS")
print("=" * 60)

fig, axes = plt.subplots(2, 3, figsize=(18, 11))
fig.suptitle("Analyse des Accidents d'Avion jusqu'en 2023",
             fontsize=16, fontweight='bold', y=1.01)

# ── Graphique 1 : Accidents par année ──────────────────────────────────────
ax1 = axes[0, 0]
ax1.plot(yearly['Year'], yearly['Accidents'],
         color='steelblue', linewidth=1.2, alpha=0.8, label='Accidents/an')
# Ligne de tendance
trend_y = slope * yearly['Year'] + intercept
ax1.plot(yearly['Year'], trend_y,
         color='red', linestyle='--', linewidth=1.5, label='Tendance')
ax1.set_title("Accidents d'avion par année", fontweight='bold')
ax1.set_xlabel("Année")
ax1.set_ylabel("Nombre d'accidents")
ax1.legend()

# ── Graphique 2 : Décès par année ──────────────────────────────────────────
ax2 = axes[0, 1]
ax2.fill_between(yearly['Year'], yearly['Décès_total'],
                 color='tomato', alpha=0.6)
ax2.plot(yearly['Year'], yearly['Décès_total'],
         color='darkred', linewidth=1)
ax2.set_title("Décès totaux par année", fontweight='bold')
ax2.set_xlabel("Année")
ax2.set_ylabel("Nombre de décès")

# ── Graphique 3 : Accidents par décennie (barres) ──────────────────────────
ax3 = axes[0, 2]
decade_stats_clean = decade_stats[decade_stats['Decade'] >= 1908]
bars = ax3.bar(decade_stats_clean['Decade'].astype(str),
               decade_stats_clean['Accidents'],
               color=sns.color_palette("Blues_d", len(decade_stats_clean)))
ax3.set_title("Accidents par décennie", fontweight='bold')
ax3.set_xlabel("Décennie")
ax3.set_ylabel("Nombre d'accidents")
ax3.tick_params(axis='x', rotation=45)
for bar in bars:
    ax3.text(bar.get_x() + bar.get_width()/2, bar.get_height() + 0.5,
             str(int(bar.get_height())), ha='center', va='bottom', fontsize=7)

# ── Graphique 4 : Histogramme des décès ────────────────────────────────────
ax4 = axes[1, 0]
ax4.hist(fat, bins=40, color='mediumpurple', edgecolor='white', alpha=0.85)
ax4.axvline(fat.mean(),   color='red',    linestyle='--', label=f'Moyenne={fat.mean():.0f}')
ax4.axvline(fat.median(), color='orange', linestyle='--', label=f'Médiane={fat.median():.0f}')
ax4.set_title("Distribution du nombre de décès", fontweight='bold')
ax4.set_xlabel("Décès par accident")
ax4.set_ylabel("Fréquence")
ax4.legend()

# ── Graphique 5 : Top 10 régions (barres horizontales) ─────────────────────
ax5 = axes[1, 1]
ax5.barh(top_regions['Region'], top_regions['Fatalities'],
         color=sns.color_palette("Reds_r", 10))
ax5.set_title("Top 10 régions – total décès", fontweight='bold')
ax5.set_xlabel("Nombre de décès")
ax5.invert_yaxis()

# ── Graphique 6 : Taux de survie moyen par décennie ────────────────────────
ax6 = axes[1, 2]
surv_by_decade = decade_stats_clean.dropna(subset=['Taux_survie'])
ax6.plot(surv_by_decade['Decade'], surv_by_decade['Taux_survie'],
         marker='o', color='teal', linewidth=2, markersize=6)
ax6.fill_between(surv_by_decade['Decade'], surv_by_decade['Taux_survie'],
                 alpha=0.2, color='teal')
ax6.set_title("Taux de survie moyen par décennie (%)", fontweight='bold')
ax6.set_xlabel("Décennie")
ax6.set_ylabel("Taux de survie (%)")
ax6.yaxis.set_major_formatter(ticker.PercentFormatter())

plt.tight_layout()
plt.savefig("analyse_accidents_avion.png", dpi=150, bbox_inches='tight')
plt.show()
print("✅ Graphique sauvegardé : analyse_accidents_avion.png")

# =============================================================================
# 5. RAPPORT DE SYNTHÈSE
# =============================================================================

print("\n" + "=" * 60)
print("  5. SYNTHÈSE & INTERPRÉTATIONS")
print("=" * 60)

print(f"""
📌 RÉSUMÉ DE L'ANALYSE
─────────────────────────────────────────────────────────────

Période analysée      : {df['Year'].min()} – {df['Year'].max()}
Total accidents       : {total_accidents:,}
Total décès           : {total_fatalities:,.0f}
Taux de survie global : {global_survival:.1f}%

STATISTIQUES DES DÉCÈS PAR ACCIDENT
  Moyenne    : {fat.mean():.1f} décès
  Médiane    : {fat.median():.1f} décès
  Écart-type : {fat.std():.1f} décès
  Skewness   : {stats.skew(fat):.2f}  → distribution asymétrique à droite

TESTS STATISTIQUES
  ANOVA (décès par décennie)
    F = {f_stat:.3f}, p = {p_value:.6f}
    → {"Différences significatives entre décennies ✅" if p_value < 0.05 else "Pas de différence significative"}

  Régression linéaire (accidents/an)
    Pente = {slope:.4f} accidents/an, R² = {r_value**2:.3f}
    → {"Tendance significative détectée ✅" if p_val_reg < 0.05 else "Pas de tendance significative"}

OBSERVATIONS CLÉS
  • Le pic d'accidents se situe généralement dans les années 1970–1990.
  • Une nette amélioration de la sécurité est visible après les années 2000.
  • La distribution des décès est fortement asymétrique : la majorité
    des accidents causent peu de morts, mais quelques catastrophes
    majeures tirent la moyenne vers le haut.
  • Les régions les plus touchées reflètent souvent le volume de trafic
    aérien historique.

UTILISATION DES BIBLIOTHÈQUES
  • Pandas  → importation, nettoyage, groupby, statistiques de base
  • NumPy   → calculs vectorisés (taux de survie, clip)
  • SciPy   → f_oneway (ANOVA), linregress, skew, kurtosis, t.interval
  • Matplotlib + Seaborn → 6 visualisations complémentaires
─────────────────────────────────────────────────────────────
""")
