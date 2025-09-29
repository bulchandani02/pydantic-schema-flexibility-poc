import streamlit as st
import requests
import json
import PyPDF2

API_BASE = "http://127.0.0.1:8000"

# Default payload structure
default_payload = {
    "document_id": "abc123",
    "title": "Streamlit Demo Document",
    "content": "This is a test document processed via Streamlit.",
    "author": "Streamlit User",
    "created_at": "2025-09-24" 
}

st.title("Dynamic & Static Pydantic PoC Demo")

# PDF Upload and Extraction
uploaded_file = st.file_uploader("Upload PDF document (to extract content)", type="pdf")
if uploaded_file:
    reader = PyPDF2.PdfReader(uploaded_file)
    pdf_text = "\n".join(page.extract_text() for page in reader.pages if page.extract_text())
    st.text_area("Extracted Text from PDF", pdf_text, height=150)
    default_payload["content"] = pdf_text[:10000]  # Limit content size if needed

# Endpoint selection
endpoint = st.selectbox(
    "Select Endpoint",
    ["/process_document (Static)", "/process_document_dynamic (Dynamic)", "/extract_with_gemini (LLM)"]
)
endpoint_map = {
    "/process_document (Static)": "/process_document",
    "/process_document_dynamic (Dynamic)": "/process_document_dynamic",
    "/extract_with_gemini (LLM)": "/extract_with_gemini"
}
selected_endpoint = endpoint_map[endpoint]

# JSON input
payload = st.text_area("Request JSON", value=json.dumps(default_payload, indent=2), height=150)

if st.button("Send Request"):
    try:
        resp = requests.post(API_BASE + selected_endpoint, json=json.loads(payload))
        st.write("Response Status:", resp.status_code)
        st.json(resp.json())
    except Exception as e:
        st.error(str(e))

st.divider()

# Schema Registry Viewer
st.header("View Schema Registry")
col1, col2 = st.columns(2)
with col1:
    if st.button("Show Static Schema"):
        resp = requests.get(API_BASE + "/schemas?registry_type=static")
        st.subheader("Static Schema")
        st.json(resp.json())
with col2:
    if st.button("Show Dynamic Schema"):
        resp = requests.get(API_BASE + "/schemas?registry_type=dynamic")
        st.subheader("Dynamic Schema")
        st.json(resp.json())
