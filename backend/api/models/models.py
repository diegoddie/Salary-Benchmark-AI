from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any, Union

class CVAnalysisResponse(BaseModel):
    role: str 
    experience_years: Optional[int] = None
    location: Optional[str] = None
    skills: Union[List[str], Dict[str, List[str]], Dict[str, Any]] = []
    education: Union[List[Dict[str, Any]], Dict[str, Any]] = []
    summary: str = Field(default="Non disponibile")