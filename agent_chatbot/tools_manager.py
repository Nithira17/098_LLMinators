from langchain_community.tools import DuckDuckGoSearchRun
from .document_processor import DocumentProcessor
from .config import Config

class ToolsManager:
    def __init__(self, models):
        self.models = models
        self.document_processor = DocumentProcessor(
            models.embedding_model_2, 
            models.llm
        )
        self.tools = self._initialize_tools()
    
    def _initialize_search_tool(self):
        """Initialize DuckDuckGo search tool"""
        return DuckDuckGoSearchRun()
    
    def _initialize_document_tools(self):
        """Initialize all document-based RAG tools"""
        tools = []
        
        # Ranil manifesto tool
        rw_tool = self.document_processor.process_document(
            Config.PDF_PATHS['ranil'],
            "Ranil Wickramasinghe Manifesto Tool",
            "Use when the user asks about Ranil Wickremesinghe's manifesto and policies. Also use when user asks to compare his policies with another candidate"
        )
        tools.append(rw_tool)
        
        # Anura manifesto tool
        akd_tool = self.document_processor.process_document(
            Config.PDF_PATHS['anura'],
            "Anura Kumara Dissanayake Manifesto Tool",
            "Use when the user asks about Anura Kumara Dissanayake's or NPP's manifesto and policies. Also use when user asks to compare his policies with another candidate"
        )
        tools.append(akd_tool)
        
        # Sajith manifesto tool
        sp_tool = self.document_processor.process_document(
            Config.PDF_PATHS['sajith'],
            "Sajith Premadasa Manifesto Tool",
            "Use when the user asks about Sajith Premadasa's or SJB's manifesto and policies. Also use when user asks to compare his policies with another candidate"
        )
        tools.append(sp_tool)
        
        # Polls/predictions tool
        poll_tool = self.document_processor.process_document(
            Config.PDF_PATHS['polls'],
            "Pre-election polls and prediction Tool",
            "Use when the user asks about polls and surveys done and their predictions"
        )
        tools.append(poll_tool)
        
        # General elections tool
        election_tool = self.document_processor.process_document(
            Config.PDF_PATHS['elections'],
            "General election data Tool",
            "Use when the user asks questions about election"
        )
        tools.append(election_tool)
        
        return tools
    
    def _initialize_tools(self):
        """Initialize all tools"""
        tools = []
        
        # Add search tool
        search_tool = self._initialize_search_tool()
        tools.append(search_tool)
        
        # Add document tools
        document_tools = self._initialize_document_tools()
        tools.extend(document_tools)
        
        return tools
    
    def get_tools(self):
        """Get all initialized tools"""
        return self.tools