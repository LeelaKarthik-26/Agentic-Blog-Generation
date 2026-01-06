from langchain.chat_models import init_chat_model
import os 
from dotenv import load_dotenv

class GroqLLM:
    def __init__(self):
        load_dotenv()
        
    def get_llm(self):
        try:
            self.groq_api_key = os.getenv("GROQ_API_KEY")
            if not self.groq_api_key:
                raise ValueError("GROQ_API_KEY is missing from environment")

            llm = init_chat_model(
                model="llama-3.1-8b-instant",
                model_provider="groq",
                api_key=self.groq_api_key,
            )
            return llm
        except Exception as e:
            raise ValueError(f"Error occured with execution: {e}")
