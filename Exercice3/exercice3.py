from pathlib import Path
from datetime import datetime
import csv

class BatchProcessor:
    def __enter__(self):
        self.csv_path = Path("Exercice3/fichier.csv")
        self.csv_file = self.csv_path.open("r", newline="", encoding="utf-8")
        self.csv_reader = csv.reader(self.csv_file)

        self.log_path = Path("Exercice3/journal.log")
        self.log_file = self.log_path.open("a", encoding="utf-8")

        self.log_file.write(f"[{datetime.now()}] Debut de batch\n")
        return self
    
    def line_processeur(self):
        for line in self.csv_reader:
            try:
                operation = ", ".join(line)
                print(f"Traitement : {operation}")
                self.log_file.write(f"[{datetime.now()}] Traitement : {operation}\n")
            except Exception as e:
                self.log_file.write(f"[{datetime.now()}] Erreur: {line} : {e}\n")

    def __exit__(self, exc_type, exc_value, traceback):
        if exc_type:
            self.log_file.write(f"[{datetime.now()}] Exception: {exc_type.__name__} - {exc_value}\n")
        
        self.log_file.write(f"[{datetime.now()}] Fin du batch\n")
        
        self.csv_file.close()
        self.log_file.close()
        return False
    
