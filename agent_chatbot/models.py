from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain.embeddings import HuggingFaceInstructEmbeddings
from .config import Config

class Models:
    def __init__(self):
        self.llm = self._initialize_llm()
        self.embedding_model = self._initialize_embedding_model()
        self.embedding_model_2 = self._initialize_huggingface_embedding()
    
    def _initialize_llm(self):
        return ChatGoogleGenerativeAI(
            model=Config.LLM_MODEL,
            temperature=Config.LLM_TEMPERATURE,
            api_key=Config.GOOGLE_API_KEY
        )
    
    def _initialize_embedding_model(self):
        return GoogleGenerativeAIEmbeddings(
            model=Config.EMBEDDING_MODEL,
            google_api_key=Config.GOOGLE_API_KEY
        )
    
    def _initialize_huggingface_embedding(self):
        return HuggingFaceInstructEmbeddings(
            model_name=Config.HUGGINGFACE_EMBEDDING_MODEL
        )