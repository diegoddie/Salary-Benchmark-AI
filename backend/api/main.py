from fastapi import FastAPI, UploadFile, File, HTTPException
from fastapi.middleware.cors import CORSMiddleware
import os
import tempfile
from functions.openai_integration import analyze_cv_with_openai
from models.models import CVAnalysisResponse
from functions.text_processing import preprocess_text
from functions.file_extraction import extract_text_from_file, is_valid_file

# Inizializza l'app FastAPI
app = FastAPI(title="Salary Benchmark API")

# Configurazione CORS per permettere le richieste dal frontend
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],  
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/cv/analyze", response_model=CVAnalysisResponse)
async def analyze_cv(file: UploadFile = File(...)):
    """Analizza un CV caricato dall'utente utilizzando AI."""
    
    if not is_valid_file(file.filename, file.content_type):
        raise HTTPException(status_code=400, detail="Formato non supportato. Usa PDF o DOCX.")
    
    try:
        content = await file.read()
        suffix = os.path.splitext(file.filename)[1] if file.filename else ".tmp"
        
        with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as temp:
            temp.write(content)
            temp_file_path = temp.name
            
            extracted_text = extract_text_from_file(temp_file_path, file.content_type)
            cleaned_text = preprocess_text(extracted_text)
            
            return analyze_cv_with_openai(cleaned_text)

    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Errore durante l'analisi del CV: {str(e)}")
    
    finally:
        if temp_file_path:
            os.remove(temp_file_path)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000) 