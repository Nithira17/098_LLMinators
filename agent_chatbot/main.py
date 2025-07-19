from .models import Models
from .tools_manager import ToolsManager
from .agent_manager import AgentManager
from .web_server import WebServer
from .config import Config

class AgentChatBot:
    def __init__(self):
        # Validate configuration first
        Config.validate_config()
        
        print("Initializing models...")
        self.models = Models()
        
        print("Setting up tools...")
        self.tools_manager = ToolsManager(self.models)
        
        print("Creating agent...")
        self.agent_manager = AgentManager(
            self.models, 
            self.tools_manager.get_tools()
        )
        
        print("Setting up web server...")
        self.web_server = WebServer(self.agent_manager)
    
    def test_agent(self):
        """Test the agent with sample queries"""
        print("\n=== Testing Agent ===")
        
        # Test 1
        print("\nTest 1: Poll prediction in August")
        try:
            response1 = self.agent_manager.query("What is the Poll prediction in month august")
            print(f"Response: {response1}")
        except Exception as e:
            print(f"Error in test 1: {e}")
        
        # Test 2
        print("\nTest 2: Ranil's education policies")
        try:
            response2 = self.agent_manager.query("How about education policies of Ranil?")
            print(f"Response: {response2}")
        except Exception as e:
            print(f"Error in test 2: {e}")
    
    def start_web_server(self, use_ngrok=True):
        """Start the web server"""
        print("\n=== Starting Web Server ===")
        public_url = self.web_server.start_server(use_ngrok=use_ngrok)
        return public_url
    
    def run(self, test_mode=False, use_ngrok=True):
        """Run the complete application"""
        if test_mode:
            # Test the agent
            self.test_agent()
        
        # Start web server
        public_url = self.start_web_server(use_ngrok=use_ngrok)
        
        print(f"\nAgent ChatBot is running!")
        print(f"API endpoint: {public_url}/ask")
        print(f"Health check: {public_url}/health")
        print("\nSend POST requests to /ask with JSON: {'question': 'your question here'}")
        
        return public_url