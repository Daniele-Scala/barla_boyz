import zipfile
import csv
import os

# Percorso completo del file ZIP da cui estrarre i CSV
zip_file_path = r"C:\Users\loren\OneDrive - unige.it\Desktop\BarlaBoyz\Data\raw\archive.zip"

# Cartella di destinazione per i CSV estratti
extracted_folder = "extracted_csv"

# Assicurati che la cartella di destinazione esista o creala se non esiste
if not os.path.exists(extracted_folder):
    os.mkdir(extracted_folder)

# Apri il file ZIP in modalità lettura
with zipfile.ZipFile(zip_file_path, "r") as zip_file:
    # Estrai tutti i file nel file ZIP
    zip_file.extractall(extracted_folder)

# Trova tutti i file CSV nella cartella estratta
csv_files = [file for file in os.listdir(extracted_folder) if file.lower().endswith(".csv")]

# Ora puoi lavorare con i file CSV estratti
for csv_file in csv_files:
    csv_file_path = os.path.join(extracted_folder, csv_file)
    
    # Esempio di come puoi aprire e leggere il contenuto di un file CSV
    with open(csv_file_path, "r", newline="") as file:
        csv_reader = csv.reader(file)
        for row in csv_reader:
            print(row)
