import os 
from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.core import Settings
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
def setup_llm():
    load_dotenv()
    api_key = os.getenv("GOOGLE_API_KEY") # get gemini api 
    # AI model
    Settings.llm = GoogleGenAI(model="models/gemini-3.1-flash-lite-preview",api_key=api_key)
    # Embedding model
    Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2")

    Settings.chunk_size = 1024 
    Settings.chunk_overlap = 100

PERSIST_DIR = "./storage" # data storage direction
DATA_DIR = "./data"