#import chromadb #database
import os
from dotenv import load_dotenv
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext,load_index_from_storage
from llama_index.readers.file import PyMuPDFReader #pdf reader
from .config import Settings, PERSIST_DIR , DATA_DIR

load_dotenv()
DB_API_KEY = os.getenv("DB_API_KEY")
def data_ingest(persist_dir=PERSIST_DIR):
    file_extractor = {".pdf": PyMuPDFReader()}#pdf file extract 
    print("[INFO] Processing")
    reader = SimpleDirectoryReader("./data",file_extractor=file_extractor)
    documents = reader.load_data()
    print("[INFO]Saving to storage")
    index = VectorStoreIndex.from_documents(documents,show_progress = True)
    index.storage_context.persist(persist_dir = persist_dir)
    print(f"[INFO]Saved to {persist_dir}")
    return index

def data_load(persist_dir=PERSIST_DIR):
    #data load from storage
    print("Data is loading from storage")
    storage_context = StorageContext.from_defaults(persist_dir=persist_dir)
    index = load_index_from_storage(storage_context)
    return index


#chroma database
#client = chromadb.CloudClient(
 # api_key= DB_API_KEY
  #tenant='ead776a0-cb65-42c8-b959-a448fc1ee6ff',
  #database='ChatbotAnxx'
#)