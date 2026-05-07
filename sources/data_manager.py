import os
from llama_index.core import VectorStoreIndex, SimpleDirectoryReader, StorageContext, load_index_from_storage
from llama_index.core.node_parser import SentenceSplitter
from llama_parse import LlamaParse
from .config import PERSIST_DIR, DATA_DIR

def data_ingest():
    llamaparse_api_key = os.getenv("llamaparse_api_key")
    
    parser = LlamaParse(
        api_key=llamaparse_api_key,
        result_type="markdown",            
        verbose=True
    )
    
    file_extractor = {".pdf": parser}
    print(f"[INFO] Processing documents: {DATA_DIR}")
    
    reader = SimpleDirectoryReader(
        DATA_DIR, 
        file_extractor=file_extractor,
        recursive=True
    )
    
    documents = reader.load_data()
    
    splitter = SentenceSplitter(
        chunk_size=1024, 
        chunk_overlap=100,
        separator="\n" 
    )
    
    nodes = splitter.get_nodes_from_documents(documents)
    index = VectorStoreIndex(nodes, show_progress=True)
    
    if not os.path.exists(PERSIST_DIR):
        os.makedirs(PERSIST_DIR)
        
    index.storage_context.persist(persist_dir=PERSIST_DIR)
    print(f"[SUCCESS] Data is saved to {PERSIST_DIR}")
    return index

def data_load():
    if not os.path.exists(PERSIST_DIR):
        print("[WARNING] No storage found, ingesting new data")
        return data_ingest()
        
    print(f"[INFO] Loading from {PERSIST_DIR}...")
    storage_context = StorageContext.from_defaults(persist_dir=PERSIST_DIR)
    return load_index_from_storage(storage_context)