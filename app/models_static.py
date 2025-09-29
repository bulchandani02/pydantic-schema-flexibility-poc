from pydantic import BaseModel
from typing import Optional



class DocumentRequest(BaseModel):
    document_id: str
    title: str
    content: str
    author: Optional[str] = None
    created_at: Optional[str] = None  # <-- Now optional


class DocumentResponse(BaseModel):
    status: str
    message: Optional[str]
    extracted_data: Optional[dict]
