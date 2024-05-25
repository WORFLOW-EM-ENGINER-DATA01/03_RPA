import re
from pypdf import PdfReader

class Facture:
    def __init__(self, numero, date, montant_ht, montant_ttc):
        self.numero = numero
        self.date = date
        self.montant_ht = montant_ht
        self.montant_ttc = montant_ttc

    def __repr__(self):
        return f"Facture(n°{self.numero}, Date: {self.date}, HT: {self.montant_ht}, TTC: {self.montant_ttc})"

    def __eq__(self, other):
        return (self.numero == other.numero and 
                self.date == other.date and 
                self.montant_ht == other.montant_ht and 
                self.montant_ttc == other.montant_ttc)

    def __add__(self, other):
        total_ht = self.montant_ht + other.montant_ht
        total_ttc = self.montant_ttc + other.montant_ttc
        return Facture(f"{self.numero} + {other.numero}", "N/A", total_ht, total_ttc)


## fichier PDF

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        reader = PdfReader(file)
        text = ""
        for page_num in range(reader.get_num_pages()):
            page = reader.get_page(page_num)
            text += page.extract_text()
    return text

def parse_facture(text):
    numero_pattern = r"Facture\s*n°(\d+)"
    date_pattern = r"Date\s*:\s*(\d{2}/\d{2}/\d{4})"
    montant_ht_pattern = r"Montant\s*Total\s*HT\s*:\s*(\d+\.\d{2})"
    montant_ttc_pattern = r"Montant\s*Total\s*TTC\s*:\s*(\d+\.\d{2})"
    
    numero = re.search(numero_pattern, text).group(1)
    date = re.search(date_pattern, text).group(1)
    montant_ht = float(re.search(montant_ht_pattern, text).group(1))
    montant_ttc = float(re.search(montant_ttc_pattern, text).group(1))
    
    return Facture(numero, date, montant_ht, montant_ttc)


pdf_path = "../Data/Facture_001.pdf"
text = extract_text_from_pdf(pdf_path)
# print(text)
facture = parse_facture(text)

print(facture)
