import re

def preprocess_text(text: str) -> str:
    # Rimuove spazi bianchi extra
    text = re.sub(r'\s+', ' ', text)
    
    # Rimuove caratteri non-ASCII (mantiene le lettere accentate)
    text = ''.join(c for c in text if c.isprintable() or c.isspace())
    
    # Rimuove header/footer ripetitivi
    text = re.sub(r'Page \d+ of \d+', '', text)
    
    # Normalizza interruzioni di riga
    text = text.replace('\r', '\n')
    
    return text.strip()