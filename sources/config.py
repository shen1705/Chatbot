import os
from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding

def setup_llm():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY")
    llm_model = os.getenv("LLM_MODEL", "models/gemini-2.0-flash")
    embed_model_name = os.getenv("EMBEDDING_MODEL", "sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")
    
    # AI model cấu hình temperature thấp để tránh ảo giác
    Settings.llm = GoogleGenAI(
        model=llm_model,
        api_key=api_key,
        temperature=0.1,  
    )
    # Embedding model đa ngôn ngữ chạy local (hoặc cấu hình model SOTA như BAAI/bge-m3)
    Settings.embed_model = HuggingFaceEmbedding(
        model_name=embed_model_name
    )

PERSIST_DIR = "./storage"
DATA_DIR = "./data"