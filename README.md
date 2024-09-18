# Right Vote

# Manifesto Comparator with RAG Chatbot and Win Predictor for the 2024 Presidential Election in Sri Lanka

This project aims to create a manifesto comparator for each leading candidates in presidential election with a chatbot using a Retrieval-Augmented Generation (RAG) model and Win Predictor model using Official Poll data and social media sentiments. The system allows users to query political manifestos and retrieve relevant information of each candidate and ask the general information on the election as well. The backend is built using Flask, Firebase and the frontend is built using Flutter.

## Features

- **Chatbot using LangChain**: Provides fast and relevant document retrieval related to the Sri Lanka's President Election 2024 from vectorstores using Hugging Face embedding model and Gemini-1.5-flash LLM.
- **Flutter Web App**: Allows users to query manifestos and view retrieved information in an interactive UI.
- **Flask API**: Handles queries from the frontend, retrieves relevant documents from the FAISS vector store, and returns results.

## Tech Stack
- **ChatBot**: Python, LangChain, Chroma, Hugging Face, Gemini-1.5-flash
- **Backend**: Python, Flask, FireBase
- **Frontend**: Flutter
- **Hosting**: Google Colab (for testing) and cloud platforms (for deployment)

## Prerequisites

- Python 3.x
- Google Colab (for testing)
- Flutter installed on your machine
- `ngrok` for exposing the Flask API in Google Colab
