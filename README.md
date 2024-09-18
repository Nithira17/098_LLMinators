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

## Sentiment Analysis
To assess public sentiment towards candidates by analyzing text data from social media and news sources. This helps to understand the emotional tone of public discourse, which can be crucial for interpreting polling data.

### Techniques Used

#### Data Collection & text preprocessing

- **Tool:** Twitter API
- **Process:** 
  - Collected recent tweets mentioning the candidates of interest.
  - Used the `tweepy` library to fetch tweets based on specific search queries related to each candidate.
  - Ensured that the sentiment analysis is not influenced by specific users or external links mentioned in the tweets.

#### Sentiment Analysis Model

- **Tool:** RoBERTa model
- **Process:**
  - **Tokenization:** Converted text into a format suitable for model input using the RoBERTa tokenizer.
  - **Model Inference:** Passed tokenized text through the RoBERTa model to obtain sentiment scores. The model was pre-trained on Twitter data to effectively classify sentiments in social media contexts.
  - **Softmax Function:** Applied the softmax function to the model's output to convert raw scores into probabilities, representing the likelihood of each sentiment class (positive, neutral, negative).

#### Sentiment Classification

- **Objective:** To categorize each tweet into one of three sentiment classes: positive, neutral, or negative.
- **Process:** 
  - Assigned sentiment labels based on the highest probability from the model’s output.


## ChatBot 

This feature is a chatbot that allows users to query the manifestos and policies of prominent Sri Lankan candidates, view pre-election poll results, and get general information on the election. Built with Langchain and RAG (Retrieval-Augmented Generation) architecture, the model uses PDF documents of candidates' manifestos, web search tools, and poll predictions to provide insightful answers.

### 1. Reading Multiple PDFs
We utilized the `pypdf` library in Python to extract text from PDF documents. The chatbot reads manifestos from multiple candidates including Ranil Wickremesinghe, Anura Kumara Dissanayake, and Sajith Premadasa, as well as pre-election poll data and general election questions.

### 2.Embedding the Text and Storing in a Vectorstore
The extracted text from each PDF is converted into embeddings using the HuggingFace `hkunlp/instructor-xl` model. These embeddings are then stored in a `Chroma` vectorstore. By persisting the vectorstore, we efficiently reuse the data for answering future queries.

### 3. Agent Architecture
We implemented tools for each candidate's manifesto using a RAG (Retrieval-Augmented Generation) setup. Each tool is responsible for retrieving and answering questions about a specific candidate’s manifesto. Additionally, a DuckDuckGo search tool is integrated to fetch real-time web data, and a poll prediction tool is included for querying pre-election polls and their forecasts.

### 4. LLM Integration
The chatbot uses the `gemini-1.5-flash` model from Google Generative AI for generating responses. This LLM is deployed within the RAG architecture to provide accurate and context-aware answers based on both document retrieval and external web search.

### 5. Interactive Querying
Users can ask the chatbot detailed questions about individual manifestos, compare policies between candidates, or inquire about pre-election predictions and general election information. The system uses a mix of retrieval from vectorstores and real-time web search to deliver comprehensive responses.

## Requirements

- Python 3.x
- `langchain` for building the RAG-based model and managing agent architectures
- `langchain-community` for using additional tools from the Langchain community
- `langchain-chroma` for managing and storing document embeddings in Chroma's vectorstore
- `pypdf` for reading and extracting text from PDFs
- `InstructorEmbedding` for generating text embeddings using HuggingFace models
- `sentence-transformers==2.2.2` for text preprocessing and vectorization
- `langchain_google_genai` for connecting to Google’s generative AI models like `gemini-1.5-flash`

