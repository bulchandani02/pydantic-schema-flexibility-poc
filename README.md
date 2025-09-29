# Dynamic vs Static Pydantic Schema Management – FastAPI PoC

A hands-on proof-of-concept comparing **static Pydantic**, **dynamic (YAML/JSON) schema loading**, and a **schema registry endpoint** for API-driven document processing. Instantly see which schema strategy fits stable, changing, or client-adaptive scenarios!

## 🚦 What’s Inside

- **Static Pydantic:** Strong typing and built-in FastAPI docs. Great for stable APIs.
- **Dynamic Pydantic:** Load schema from YAML/JSON at runtime. Agility for frequent changes, demo code included.
- **Schema Registry:** `/schemas` endpoint so clients can discover and adapt to the latest schema instantly.

## 💡 Use Cases

- APIs that rarely change → use static models for safety and auto-docs.
- High-change environments → use dynamic schemas for flexibility.
- Partnership and product scale → add schema registry for fast client onboarding.

## 🛠️ Demo

- Upload any PDF in the Streamlit app.
- Instantly extract text and process via both static/dynamic endpoints.
- See side-by-side results and schema registry returns.
- Try out the LLM-powered endpoint for advanced extraction.

## 🚀 How To Run

git clone https://github.com/bulchandani02/pydantic-schema-flexibility-poc.git
cd repo-name
pip install -r requirements.txt
uvicorn app.main:app --reload
streamlit run streamlit_app.py




Set up `.env` with your Google Gemini API key for LLM extraction.

## 📦 Folder Structure

- `/app`: FastAPI endpoints and models  
- `/schemas`: YAML/JSON sample schemas  
- `/tests`: Basic test scripts  
- `streamlit_app.py`: Live, visual demo interface

## 🔍 Code Highlights

- Identical output logic for static and dynamic endpoints
- Registry endpoint for real-time client schema adaptation
- Easily extensible for new document types

## 📊 Results & Findings

| Approach  | Pros                       | Cons                   | Best Use      |
|-----------|----------------------------|------------------------|---------------|
| Static    | Safe, docs, IDE            | Redeploy for change    | Stable APIs   |
| Dynamic   | No redeploy, flexible      | Weak docs, runtime risk| Fast-changing |
| Registry  | Adaptive, client-friendly  | Extra setup            | Ecosystem scale|



---

**Created by [Jyotsna Bulchandani](https://linkedin.com/in/jyotsna-bulchandani)**  
**Feedback welcome!**

---
