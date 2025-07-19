"""Flask web server for the chatbot API"""
from flask import Flask, request, jsonify
import threading
from pyngrok import ngrok
from flask_cors import CORS
from .config import Config

class WebServer:
    def __init__(self, agent_manager):
        self.agent_manager = agent_manager
        self.app = self._create_app()
        self._setup_ngrok()
    
    def _create_app(self):
        """Create and configure Flask app"""
        app = Flask(__name__)
        CORS(app)
        
        @app.route('/ask', methods=['POST'])
        def ask():
            try:
                user_input = request.json.get("question")
                if not user_input:
                    return jsonify({"error": "No question provided"}), 400

                response = self.agent_manager.query(user_input)
                return jsonify({"answer": response})

            except Exception as e:
                return jsonify({"error": str(e)}), 500
        
        @app.route('/health', methods=['GET'])
        def health():
            return jsonify({"status": "healthy"})
        
        return app
    
    def _setup_ngrok(self):
        """Setup ngrok for public URL"""
        if Config.NGROK_AUTH_TOKEN:
            ngrok.set_auth_token(Config.NGROK_AUTH_TOKEN)
    
    def _run_flask(self):
        """Run Flask app"""
        self.app.run(host='0.0.0.0', port=Config.FLASK_PORT, debug=Config.FLASK_DEBUG)
    
    def start_server(self, use_ngrok=True):
        """Start the web server with optional ngrok"""
        # Run Flask app in a separate thread
        flask_thread = threading.Thread(target=self._run_flask)
        flask_thread.daemon = True
        flask_thread.start()

        if use_ngrok and Config.NGROK_AUTH_TOKEN:
            try:
                # Expose the Flask app using ngrok
                public_url = ngrok.connect(Config.FLASK_PORT).public_url
                print(f"Public URL: {public_url}")
                return public_url
            except Exception as e:
                print(f"Failed to setup ngrok: {e}")
                print(f"Server running locally at: http://localhost:{Config.FLASK_PORT}")
                return f"http://localhost:{Config.FLASK_PORT}"
        else:
            print(f"Server running at: http://localhost:{Config.FLASK_PORT}")
            return f"http://localhost:{Config.FLASK_PORT}"