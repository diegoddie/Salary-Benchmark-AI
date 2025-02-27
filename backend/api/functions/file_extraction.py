import PyPDF2  
import docx     
import os

ALLOWED_FILE_TYPES = {
    ".pdf": "application/pdf",
    ".docx": "application/vnd.openxmlformats-officedocument.wordprocessingml.document"
}

def is_valid_file(filename: str, content_type: str) -> bool:
    ext = os.path.splitext(filename)[1].lower()
    return ext in ALLOWED_FILE_TYPES and ALLOWED_FILE_TYPES[ext] == content_type

def extract_text_from_pdf(file_path: str) -> str:
    print("Estrazione testo dal PDF")
    try:
        # Apriamo il file PDF in modalità binaria di lettura
        with open(file_path, 'rb') as pdf_file:
            # Creiamo un oggetto PdfReader per leggere il PDF
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            print("PDF letto")
            # Inizializziamo una stringa vuota per contenere tutto il testo
            text = ""
            print("Inizializzazione stringa vuota")
            for page in pdf_reader.pages:
                text += page.extract_text()
            print(text)
            return text
    except Exception as e:
        # Se si verifica un errore, lo logghiamo e lo solleviamo
        print(f"Errore durante l'estrazione del testo dal PDF: {str(e)}")
        raise Exception(f"Errore durante l'estrazione del testo dal PDF: {str(e)}")

def extract_text_from_docx(file_path: str) -> str:
    try:
        doc = docx.Document(file_path)
        return "\n".join(paragraph.text for paragraph in doc.paragraphs)
    except Exception as e:
        print(f"Errore durante l'estrazione del testo dal DOCX: {str(e)}")
        raise Exception("Errore durante l'estrazione del testo dal DOCX.")
    
def extract_text_from_file(file_path: str, content_type: str) -> str:
    if content_type == "application/pdf":
        return extract_text_from_pdf(file_path)
    elif content_type == "application/vnd.openxmlformats-officedocument.wordprocessingml.document":
        return extract_text_from_docx(file_path)
    else:
        raise ValueError("Formato di file non supportato.")