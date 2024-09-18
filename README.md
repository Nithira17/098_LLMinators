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


## Win Predictor using LSTM

This project focuses on analyzing pre-election poll data and predicting final election results using an LSTM (Long Short-Term Memory) neural network model. The project also simulates the redistribution of second-preference votes based on pre-defined assumptions and calculates the final vote counts for the election.

### 1. Web Scraping Poll Results
We extract the latest poll data from a specified URL using `BeautifulSoup` to scrape the necessary information, including support percentages for the candidates. This information is then used to train a model and make predictions.

### 2. Data Analysis and Preprocessing
A sample dataset of election polls from 2024 is created and preprocessed for analysis. The data is one-hot encoded, and relevant features like candidate support and demographics (age group, education level) are considered. The model also uses historical data from the 2019 election for comparison.

### 3. LSTM Model for Prediction
The model is trained using poll data across several months (April 2024 to September 2024). A scaled and reshaped dataset is fed into an LSTM model to predict the potential election outcome. The model outputs predicted percentages for each candidate.

### 4. Second Preference Redistribution
In cases where no candidate crosses the 50% mark, we simulate the redistribution of second-preference votes based on a predefined redistribution model. The final vote shares are recalculated to determine the election outcome.

### 5. Final Vote Calculation
After determining the final percentages, the total vote count is adjusted based on the estimated population size (17.1 million). This provides a clearer understanding of the number of votes each candidate is expected to receive.

## Features

- **Web Scraping:** Automatically retrieves election poll data from a website.
- **LSTM Model:** Utilizes Long Short-Term Memory for time-series prediction based on poll data.
- **Second-Preference Voting System:** Simulates second-round voting if no candidate achieves a majority in the first round.
- **Final Vote Estimation:** Converts percentage predictions into actual vote counts based on a given population size.

## Requirements

- Python 3.x
- `BeautifulSoup` for web scraping
- `pandas` and `numpy` for data handling
- `sklearn` for preprocessing
- `tensorflow` and `keras` for building the LSTM model

