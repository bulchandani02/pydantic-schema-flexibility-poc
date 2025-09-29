from fastapi import FastAPI
from app.models_static import DocumentRequest, DocumentResponse

from fastapi import Body
from app.dynamic_loader import load_dynamic_model

from fastapi import Query
from app.registry import get_static_schema, get_dynamic_schema

import google.generativeai as genai
import os
from fastapi import HTTPException
from dotenv import load_dotenv
load_dotenv()


app = FastAPI()

@app.post("/process_document", response_model=DocumentResponse)
async def process_document(request: DocumentRequest):
    extracted_data = {
        "title_length": len(request.title),
        "author": request.author,
        "word_count": len(request.content.split()),
    }
    return {
        "status": "success",
        "message": "Document processed successfully.",
        "extracted_data": extracted_data,
        "mode": "static"
    }





@app.post("/process_document_dynamic")
async def process_document_dynamic(body: dict = Body(...)):
    DynamicModel = load_dynamic_model("schemas/schema_dynamic.yaml")
    data = DynamicModel(**body)
    extracted_data = {
        "title_length": len(data.title),
        "author": getattr(data, "author", None),
        "word_count": len(data.content.split()),
    }
    return {
        "status": "success",
        "message": "Document processed successfully.",
        "extracted_data": extracted_data,
        "mode": "dynamic"
    }





@app.get("/schemas")
async def get_schema(registry_type: str = Query("static", enum=["static", "dynamic"])):
    if registry_type == "static":
        return get_static_schema()
    elif registry_type == "dynamic":
        return get_dynamic_schema()
    else:
        return {"error": "Invalid schema type"}




GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")  # Set this in your .env or as an env var

if GOOGLE_API_KEY:
    genai.configure(api_key=GOOGLE_API_KEY)




@app.post("/extract_with_gemini")
async def extract_with_gemini(body: dict = Body(...)):
    try:
        model = genai.GenerativeModel('models/gemini-2.5-pro')
        prompt = f"Extract key info from this document: {body}"
        response = model.generate_content(prompt)
        return {"output": response.text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


