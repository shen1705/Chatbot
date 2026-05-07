import os
from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def setup_llm():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    
    # AI model cấu hình temperature thấp để tránh ảo giác
    Settings.llm = GoogleGenAI(
        model="models/gemini-3.1-flash-lite-preview",
        api_key=api_key,
        temperature=0.1,  
    )
    # Embedding model đa ngôn ngữ chạy local
    Settings.embed_model = HuggingFaceEmbedding(
        model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2"
    )

PERSIST_DIR = "./storage"
DATA_DIR = "./data"