import nest_asyncio
nest_asyncio.apply()

from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from sources.engine import ChatEngine
import uvicorn

app = FastAPI(title="LlamaIndex RAG API")

# Engine start
try:
    print("--- Loading ChatEngine ---")
    bot = ChatEngine()
    print("--- ChatEngine READY ---")
except Exception as e:
    print(f"CRITICAL ERROR: {e}")
    bot = None

class ChatRequest(BaseModel):
    message: str

@app.post("/chat")
async def chat_endpoint(request: ChatRequest):
    if bot is None:
        raise HTTPException(status_code=500, detail="Engine not initialized")
    
    try:
        response = await bot.query_engine.aquery(request.message)
        
        return {
            "reply": str(response),
            "status": "success"
        }
    except Exception as e:
        import traceback
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)