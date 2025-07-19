import sys
import os

# Add the project root to the Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from agent_chatbot.main import AgentChatBot

if __name__ == "__main__":
    try:
        # Initialize and run the chatbot
        chatbot = AgentChatBot()
        
        # Run with testing enabled and ngrok
        chatbot.run(test_mode=True, use_ngrok=True)
        
        # Keep the main thread alive
        input("Press Enter to stop the server...")
        
    except KeyboardInterrupt:
        print("\nShutting down...")
    except Exception as e:
        print(f"Error: {e}")