# 📧 Spam Detection

A machine learning web application that classifies messages as **Spam** or **Not Spam** using Natural Language Processing (NLP).

## 🚀 Live Demo

👉 [Try the Spam Detection App](https://sahil-studio-spam-classifier-app-zvmze8.streamlit.app/)

## 📌 Project Overview

This project uses NLP and machine learning techniques to detect whether a given SMS/message is spam.

The text is converted into numerical features using **TF-IDF**, and a trained machine learning model is used to make the prediction.

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- NLTK
- Scikit-learn
- TF-IDF
- Streamlit

## ⚙️ Workflow

1. Load and preprocess the text data
2. Clean and tokenize the messages
3. Convert text into numerical features using TF-IDF
4. Train a machine learning classification model
5. Save the trained model and vectorizer
6. Build a Streamlit web application
7. Deploy the application

## 📊 Model

- **Feature Extraction:** TF-IDF
- **Task:** Binary Text Classification
- **Classes:** Spam / Not Spam

## 📂 Project Structure

```text
├── app.py
├── model.pkl
├── vectorizer.pkl
├── requirements.txt
├── spam.png
└── README.md
