from llama_index.core import PromptTemplate
from .config import setup_llm
from .data_manager import data_load
from .prompts import RAG_PROMPT_TEMPLATE, FEW_SHOT_POOL 

class ChatEngine:
    def __init__(self):
        setup_llm()
        self.index = data_load()
        #query engine 
        self.query_engine = self.index.as_query_engine(
            similarity_top_k=5
        )
    #
    def _get_dynamic_few_shots(self, user_query: str, top_k: int = 2) -> str:
        query_lower = user_query.lower()
        scored_examples = []
        
        # check relation
        for ex in FEW_SHOT_POOL:
            score = sum(1 for kw in ex["keywords"] if kw in query_lower)
            scored_examples.append((score, ex))
        
        # take the best k example 
        scored_examples.sort(key=lambda x: x[0], reverse=True)
        selected_examples = [ex for score, ex in scored_examples[:top_k] if score > 0]
        
        if not selected_examples:
            return ""
            
        formatted_str = "--- CÁC VÍ DỤ MẪU ---\n"
        for ex in selected_examples:
            formatted_str += f"Q: {ex['query']}\nA: {ex['answer']}\n\n"
            
        return formatted_str

    def get_response(self, user_query: str):
        #get dynamic fewshot
        dynamic_shots = self._get_dynamic_few_shots(user_query)
        #create prompt 
        final_prompt_str = RAG_PROMPT_TEMPLATE.replace("{dynamic_few_shots}", dynamic_shots)
        #create prompt template
        dynamic_qa_prompt = PromptTemplate(final_prompt_str)
        self.query_engine.update_prompts(
            {"response_synthesizer:text_qa_template": dynamic_qa_prompt}
        )        
        #query
        return self.query_engine.query(user_query)