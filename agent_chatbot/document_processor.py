from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_chroma import Chroma
from langchain.chains import RetrievalQA
from langchain.agents import Tool
from .config import Config
import os

class DocumentProcessor:
    def __init__(self, embedding_model, llm):
        self.embedding_model = embedding_model
        self.llm = llm
        self.text_splitter_instance = RecursiveCharacterTextSplitter(
            chunk_size=Config.CHUNK_SIZE, 
            chunk_overlap=Config.CHUNK_OVERLAP
        )
    
    def load_doc(self, pdf_path):
        """Load the PDF document"""
        if not os.path.exists(pdf_path):
            raise FileNotFoundError(f"PDF file not found: {pdf_path}")
        
        loader = PyPDFLoader(pdf_path)
        docs = loader.load()
        return docs
    
    def text_splitter(self, docs):
        """Split the pdf into chunks"""
        splits = self.text_splitter_instance.split_documents(docs)
        return splits
    
    def vector_store(self, splits):
        """Store the chunks in vectorstore"""
        vectorstore = Chroma.from_documents(documents=splits, embedding=self.embedding_model)
        return vectorstore
    
    def retriever(self, vectorstore):
        """Create retriever function"""
        retriever = vectorstore.as_retriever()
        return retriever
    
    def rag_chain(self, retriever):
        """Create RAG chain"""
        rag_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=retriever
        )
        return rag_chain
    
    def rag_tool(self, rag_chain, tool_name, description):
        """Create RAG tool"""
        rag_tool = Tool(
            tool_name,
            func=rag_chain.run,
            description=description
        )
        return rag_tool
    
    def process_document(self, pdf_path, tool_name, description):
        """Document processing pipeline"""
        print(f"Processing document: {pdf_path}")
        pdf = self.load_doc(pdf_path)
        text_split = self.text_splitter(pdf)
        vectorstore = self.vector_store(text_split)
        retriever_instance = self.retriever(vectorstore)
        ragchain = self.rag_chain(retriever_instance)
        tool = self.rag_tool(ragchain, tool_name, description)
        return tool