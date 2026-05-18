import pandas as pd
import re

# 1. Load the data
print("Loading data...")
df = pd.read_csv('data/merged_cm_jobs.csv')

# 2. Extract unique raw job titles
unique_postes = df['poste'].dropna().unique()
print(f"Found {len(unique_postes)} unique raw job titles.")

# 3. Define mapping rules (Keyword -> Standard Name)
# These will be checked in order. The first match wins.
mapping_rules = {
    'développeur|programmeur|software|frontend|backend|fullstack|dev': 'Développeur Logiciel / Web',
    'comptable|accountant|comptabilité|trésorier': 'Comptable / Finance',
    'commercial|vente|sales|vendeur|vendeuse|business developer|business dev': 'Commercial / Vente',
    'marketing|digital|seo|sea|community manager|communication': 'Marketing & Communication',
    'chauffeur|driver|conducteur|livreur': 'Chauffeur / Livreur',
    'assistant|secrétaire|receptionniste|réceptionniste': 'Assistant(e) de direction / Secrétariat',
    'projet|project manager|scrum': 'Gestionnaire de projet',
    'consultant|conseiller': 'Consultant',
    'ressources humaines|rh|recruteur|hr ': 'Ressources Humaines',
    'ingénieur|engineer': 'Ingénieur',
    'technicien|maintenance': 'Technicien / Maintenance',
    'médecin|infirmier|infirmière|santé|medical|clinique': 'Santé & Médical',
    'directeur|manager|chef de département|head of': 'Direction / Top Management',
    'enseignant|professeur|formateur': 'Education & Formation',
    'stagiaire|stage|intern': 'Stagiaire',
    'logistique|supply chain|magasinier': 'Logistique & Supply Chain',
    'design|graphiste|ui|ux': 'Design / Graphisme',
    'data|analyste|analyst': 'Data / Analyste',
    'caissier|caissière': 'Caissier(e)'
}

# 4. Normalization Function
def normalize_title(raw_title):
    raw_lower = str(raw_title).lower()
    
    # If the title is too short or is a known error
    if len(raw_lower) < 4 or "erreur" in raw_lower or "error" in raw_lower:
        return "Poste non défini"
        
    for pattern, clean_name in mapping_rules.items():
        if re.search(pattern, raw_lower):
            return clean_name
            
    return "Autre" # If no rule matches

# 5. Apply the function
print("Normalizing titles...")
mapping_data = []
for raw in unique_postes:
    clean = normalize_title(raw)
    mapping_data.append({'poste_brut': raw, 'poste_clean': clean})

# 6. Create mapping dataframe and save to CSV
df_mapping = pd.DataFrame(mapping_data)

# Show a quick summary of the normalization results
summary = df_mapping['poste_clean'].value_counts()
print("\n--- Summary of Normalization ---")
print(summary)

# Save to CSV
output_file = 'data/mapping_poste.csv'
df_mapping.to_csv(output_file, index=False, encoding='utf-8')
print(f"\nMapping successfully saved to: {output_file}")
print("You can now import this file into Power BI as your D_Poste dimension table!")
