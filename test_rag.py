import os
import warnings
from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI 
from llama_index.embeddings.huggingface import HuggingFaceEmbedding
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, Settings, StorageContext, load_index_from_storage
from llama_index.readers.file import PyMuPDFReader #pdf reader


warnings.filterwarnings("ignore")
os.environ["TOKENIZERS_PARALLELISM"] = "false"

load_dotenv()
api_key = os.getenv("GOOGLE_API_KEY")#API key


Settings.llm = GoogleGenAI(model="models/gemini-3.1-flash-lite-preview", api_key=api_key)# AI model

Settings.embed_model = HuggingFaceEmbedding(model_name="sentence-transformers/paraphrase-multilingual-MiniLM-L12-v2") #embedding model


Settings.chunk_size = 1024 #chunk size 
Settings.chunk_overlap = 100

PERSIST_DIR = "./storage" # data

def run_rag():                                                          
    
    file_extractor = {".pdf": PyMuPDFReader()} #pdf file extract 

    if os.path.exists(PERSIST_DIR):#load data embed neu ton tai roi
        print("1.data loading")
        storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
        index = load_index_from_storage(storage_context)
    else:
        print("2. indexing")#embed data roi luu 
        reader = SimpleDirectoryReader("./data", file_extractor=file_extractor)
        documents = reader.load_data()
        
        index = VectorStoreIndex.from_documents(documents, show_progress=True) 
        index.storage_context.persist(persist_dir=PERSIST_DIR)
        print(f"Save to {PERSIST_DIR}")


    query_engine = index.as_query_engine(similarity_top_k=10)#query config 
    
    question = "Trong dự án ATM (PBL1), hai sinh viên thực hiện là ai và cấu trúc dữ liệu cốt lõi được sử dụng là gì?"
    print(f"\n--- Query: {question} ---")
    
    response = query_engine.query(question) # thuc hien query voi AI 
    print(f"\n GEMINI: {response}")

    print("\n" + "="*50)
    print(" [DEBUG] NỘI DUNG THỰC TẾ AI ĐÃ ĐỌC:")
    for i, node in enumerate(response.source_nodes):
        file_name = node.metadata.get('file_name', 'Không rõ')
        print(f"\nĐoạn {i+1} (File: {file_name}):")
        print(node.node.text[:200].strip().replace('\n', ' ') + "...")
    print("="*50)

if __name__ == "__main__":

    if not os.path.exists(PERSIST_DIR):
        pass 
    else:
        print("Cảnh báo: Bạn nên xóa thư mục ./storage để hệ thống cập nhật dữ liệu PDF mới sạch hơn.")
    
    run_rag()