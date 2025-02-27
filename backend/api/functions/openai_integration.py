import os
from openai import OpenAI
from dotenv import load_dotenv
import json
from models.models import CVAnalysisResponse

# Carica le variabili d'ambiente dal file .env
load_dotenv()

# Inizializza il client OpenAI con la API key
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def analyze_cv_with_openai(cv_text: str) -> CVAnalysisResponse:
    """
    Analizza il testo del CV utilizzando OpenAI per estrarre informazioni rilevanti.
    
    Args:
        cv_text: Testo pulito e preprocessato del CV
        
    Returns:
        Un'istanza di CVAnalysisResponse con i dati estratti dal CV
        
    Raises:
        Exception: Se l'analisi con OpenAI fallisce
    """
    # Definiamo il prompt per l'API
    prompt = f"""
    Analizza il seguente CV e estrai le informazioni chiave in formato JSON.
    
    Curriculum Vitae:
    {cv_text}
    
    Estrai le seguenti informazioni in formato JSON:
    - role: Ruolo principale della persona (es. "Frontend Developer", "Data Scientist")
    - experience_years: Stima degli anni di esperienza professionale (numero intero)
    - location: Località attuale o preferita della persona
    - skills: Competenze tecniche e personali. Puoi strutturarle come:
       * Una lista semplice di stringhe: ["JavaScript", "Python", "Leadership"]
       * O un dizionario di categorie: {"Frontend": ["HTML", "CSS"], "Backend": ["Python", "Flask"]} 
    - education: Formazione, come lista di oggetti con campi degree, institution e year
    - summary: Breve sintesi professionale (2-3 frasi)
    
    Rispondi SOLO con il JSON, senza altri commenti. Se un'informazione non è presente, lascia il campo come array vuoto o null.
    """
    
    try:
        # Chiamata all'API di OpenAI
        response = client.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "Sei un assistente specializzato nell'analisi di CV. Estrai informazioni strutturate dai curriculum in modo accurato e organizzato."},
                {"role": "user", "content": prompt}
            ],
            response_format={"type": "json_object"},
            temperature=0.1,  # Temperatura bassa per risposte più precise
        )
        
        # Estrai la risposta
        result = response.choices[0].message.content
        
        # Converte la stringa JSON in dizionario Python
        analysis_data = json.loads(result)
        
        # Crea e restituisce un'istanza di CVAnalysisResponse
        return CVAnalysisResponse(**analysis_data)
        
    except Exception as e:
        print(f"Errore durante l'analisi del CV con OpenAI: {str(e)}")
        
        # Se l'errore è relativo alla validazione del modello Pydantic
        if "validation error" in str(e).lower():
            print(f"Errore di validazione con i dati ricevuti da OpenAI: {str(e)}")
            raise Exception(f"I dati ricevuti da OpenAI non corrispondono al formato atteso: {str(e)}")
        
        # Se l'errore è legato alla quota, forniamo un messaggio più specifico
        if "quota" in str(e) or "exceeded" in str(e) or "insufficient" in str(e):
            raise Exception("La quota OpenAI è stata superata. Aggiorna il tuo piano OpenAI o imposta DEMO_MODE=true nel file .env.")
            
        # Altri errori
        raise Exception("Non è stato possibile consultare OpenAI per analizzare questo CV. Controlla che le chiavi API siano valide.")
