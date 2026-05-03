# ============================================================
# 💾 SAUVEGARDE DES DONNÉES NETTOYÉES EN CSV
# Ajouter ces cellules à la fin de la section "Nettoyage"
# ============================================================

import os

# Dossier de sortie
output_dir = "data_clean"
os.makedirs(output_dir, exist_ok=True)

# Sauvegarde de chaque DataFrame nettoyé
results_clean.to_csv(f"{output_dir}/results_clean.csv", index=False)
shootouts_clean.to_csv(f"{output_dir}/shootouts_clean.csv", index=False)
goalscorers_clean.to_csv(f"{output_dir}/goalscorers_clean.csv", index=False)
former_names.to_csv(f"{output_dir}/former_names.csv", index=False)

# Sauvegarde des données EDA déjà calculées
results_domicile.to_csv(f"{output_dir}/results_domicile.csv", index=False)
taux_par_decennie.to_csv(f"{output_dir}/taux_par_decennie.csv", index=False)

print("✅ CSV sauvegardés dans le dossier 'data_clean/' :")
for f in os.listdir(output_dir):
    taille = os.path.getsize(f"{output_dir}/{f}") / 1024
    print(f"  📄 {f}  ({taille:.1f} KB)")
