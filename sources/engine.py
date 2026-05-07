from llama_index.core import PromptTemplate
from .config import setup_llm
from .data_manager import data_load
from .prompts import RAG_PROMPT_TEMPLATE

class ChatEngine:
    def __init__(self):
        setup_llm()
        self.index = data_load()
        
        # Thiết lập template Few-shot
        self.qa_prompt = PromptTemplate(RAG_PROMPT_TEMPLATE)
        
        self.query_engine = self.index.as_query_engine(
            similarity_top_k=5,
            text_qa_template=self.qa_prompt
        )

    def get_response(self, user_query: str):
        return self.query_engine.query(user_query)