# Right Vote

# Manifesto Comparator with RAG Chatbot and Vector Store

This project aims to create a manifesto comparator with a chatbot using a Retrieval-Augmented Generation (RAG) model and a vector store. The system allows users to query political manifestos and retrieve relevant information. The backend is built using Flask and FAISS, and the frontend is built using Flutter.

## Features

- **Chatbot with FAISS vector store**: Provides fast and relevant document retrieval from stored vectors using Hugging Face embeddings.
- **Flutter Web App**: Allows users to query manifestos and view retrieved information in an interactive UI.
- **Flask API**: Handles queries from the frontend, retrieves relevant documents from the FAISS vector store, and returns results.

## Tech Stack

- **Backend**: Python, Flask, Hugging Face
- **Frontend**: Flutter
- **Hosting**: Google Colab (for testing) and cloud platforms (for deployment)

## Prerequisites

- Python 3.x
- Google Colab (for testing)
- Flutter installed on your machine
- `ngrok` for exposing the Flask API in Google Colab
