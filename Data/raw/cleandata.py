import pandas as pd
import os

# Directory contenente i file CSV da pulire
csv_folder = "Data\extracted_csv"

# Ottenere la lista di tutti i file CSV nella directory
csv_files = [file for file in os.listdir(csv_folder) if file.lower().endswith(".csv")]

# Esempio di operazioni di pulizia:
for csv_file in csv_files:
    # Crea il percorso completo del file CSV
    csv_file_path = os.path.join(csv_folder, csv_file)
    
    # Leggi il file CSV in un DataFrame
    df = pd.read_csv(csv_file_path)

    # Esempio di operazioni di pulizia:
    # Rimuovere righe duplicate
    df.drop_duplicates(inplace=True)

    # Gestire i valori mancanti (NaN) se necessario
    df.dropna(inplace=True)

    # Rinominare colonne se necessario
    # df.rename(columns={"vecchio_nome": "nuovo_nome"}, inplace=True)

    # Esegui altre operazioni di pulizia a seconda delle tue esigenze

    # Salva il DataFrame pulito nel file originale sovrascrivendolo
    df.to_csv(csv_file_path, index=False)

    print(f"Dati puliti salvati in {csv_file}")

print("Pulizia dei file CSV completata.")
