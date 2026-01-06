from langchain.chat_models import init_chat_model
import os 
from dotenv import load_dotenv

class GroqLLM:
    def __init__(self):
        load_dotenv()
        
    def get_llm(self):
        try:
            os.environ["LANGCHAIN_API_KEY"] = self.groq_api_key=os.getenv("LANGCHAIN_API_KEY") # type: ignore
            llm = init_chat_model(model='llama-3.1-8b-instant', model_provider="groq", api_key=self.groq_api_key)
            return llm
        except Exception as e:
            raise ValueError("Error occured with execution: {e}")