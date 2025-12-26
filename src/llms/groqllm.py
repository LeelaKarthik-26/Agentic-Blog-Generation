from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

class Groqllm:
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        try:
            os.environ["GROQ_API_KEY"] = self.groq_api_key = os.getenv("GROQ_API_KEY")
            llm = init_chat_model(model="llama-3.1-8b-instant", model_provider="groq", api_key= self.groq_api_key)
            return llm
        except Exception as e:
            raise ValueError(f"Error occured with exception: {e}")