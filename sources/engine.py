from .config import setup_llm,PERSIST_DIR
from .data_manager import data_load, data_ingest
import os

class ChatEngine():
    def __init__(self):
        setup_llm()
        
        if os.path.exists(PERSIST_DIR):#co storage
            self.index = data_load()#load data tu storage
        else:
            # chua co storage
            self.index = data_ingest()
        #config query engine
        self.query_engine = self.index.as_query_engine(
            similarity_top_k=5,         # 5 lien quan nhat
            streaming=False            
        )

    def get_response(self,user_query:str):
        if not self.index:
            return "ERROR: Cant load data from storage"
        response = self.query_engine.query(user_query)
        return response