import os
from pathlib import Path
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

class Config:
    # Project root directory
    ROOT_DIR = Path(__file__).parent.parent
    DATA_DIR = ROOT_DIR / "data"
    
    # API Keys
    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    NGROK_AUTH_TOKEN = os.getenv('NGROK_AUTH_TOKEN')
    
    # Model Settings
    LLM_MODEL = "gemini-1.5-flash"
    LLM_TEMPERATURE = 0
    EMBEDDING_MODEL = "models/embedding-001"
    HUGGINGFACE_EMBEDDING_MODEL = "hkunlp/instructor-xl"
    
    # Text Splitting Settings
    CHUNK_SIZE = 400
    CHUNK_OVERLAP = 50
    
    # Flask Settings
    FLASK_PORT = int(os.getenv('FLASK_PORT', 5000))
    FLASK_DEBUG = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    # PDF Paths (using relative paths from project root)
    PDF_PATHS = {
        'ranil': str(DATA_DIR / 'manifesto-ranil.pdf'),
        'anura': str(DATA_DIR / 'manifesto-anura.pdf'),
        'sajith': str(DATA_DIR / 'manifesto-sajith.pdf'),
        'polls': str(DATA_DIR / 'Polls.pdf'),
        'elections': str(DATA_DIR / 'general_election_questions.pdf')
    }
    
    @classmethod
    def validate_config(cls):
        """Validate that all required configuration is present"""
        if not cls.GOOGLE_API_KEY:
            raise ValueError("GOOGLE_API_KEY environment variable is required")
        
        if not cls.NGROK_AUTH_TOKEN:
            raise ValueError("NGROK_AUTH_TOKEN environment variable is required")
        
        # Check if PDF files exist
        missing_files = []
        for name, path in cls.PDF_PATHS.items():
            if not os.path.exists(path):
                missing_files.append(f"{name}: {path}")
        
        if missing_files:
            raise FileNotFoundError(f"Missing PDF files:\n" + "\n".join(missing_files))