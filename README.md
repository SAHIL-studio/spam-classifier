# 📧 Spam Detection

A machine learning web application that classifies messages as **Spam** or **Not Spam** using Natural Language Processing (NLP).

## 🚀 Live Demo

👉 [**Try the Spam Detection App**](https://sahil-studio-spam-classifier-app-zvmze8.streamlit.app/)

## 📌 Project Overview

This project uses Natural Language Processing and machine learning techniques to classify text messages as spam or not spam.

The text is preprocessed and converted into numerical features using **TF-IDF**, which are then passed to a trained machine learning model to make the prediction.

The trained model and vectorizer are saved using Pickle and integrated into a **Streamlit** web application.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- TF-IDF
- Streamlit

## ⚙️ Workflow

1. Load the SMS dataset
2. Clean and preprocess the text
3. Tokenize the messages
4. Remove unnecessary words and characters
5. Convert text into numerical features using TF-IDF
6. Train a machine learning classification model
7. Save the trained model and vectorizer
8. Build the Streamlit application
9. Deploy the application using Streamlit Community Cloud

## 📂 Project Structure

```text
Spam-Detection/
│
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── spam.png
└── README.md
