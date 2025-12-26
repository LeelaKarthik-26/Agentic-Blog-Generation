from langchain.chat_models import init_chat_model
import os
from dotenv import load_dotenv

class Groqllm:
    def __init__(self):
        load_dotenv()

    def get_llm(self):
        os.environ["GROQ_API_KEY"] = self.groq_api_key = os.getenv("GROQ_API_KEY")
        llm = init_chat_model(model="groq/llama-3.1-8b-instant", api_key= self.groq_api_key)
        return llm