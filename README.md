# Analyse BI des Offres d'Emploi au Cameroun
Projet BI collaboratif analysant plus de 12 000 offres d'emploi via Power BI.

## Architecture
Format : Power BI Project (.pbip) avec stockage TMDL (modèle) et PBIR (rapport) pour un versioning propre.

Données : data/merged_cm_jobs.csv.

## Installation Rapide
Cloner : git clone https://github.com/lionel-tlb/Analyse_BI_offres_emploi.git.

Ouvrir : Lancer Rapport.pbip.

Configurer : Dans Power BI, modifier le paramètre CheminProjet avec votre chemin local (ex: C:\Users\Lionel\Documents\Projet).

## Workflow de l'équipe
Branches : Créez une branche par tâche (git checkout -b feature-nom).

Sync : Enregistrez dans PBI avant de commit pour mettre à jour les fichiers texte.

Merge : Pull avant de Push pour éviter les conflits.
