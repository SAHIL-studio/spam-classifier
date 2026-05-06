import streamlit as st
import pickle
import nltk
nltk.download('punkt')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
ps = PorterStemmer()
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))

st.title('sms spam detection')
input_sms = st.text_area('Enter the message')

def text_transform(text):
    text = text.lower()
    text = nltk.word_tokenize(text)

    y = []
    for i in text:
        if i.isalnum():
            y.append(i)

    text = y[:]
    y.clear()
    for i in text:
         if i not in stopwords.words('english') and i not in string.punctuation:
            y.append(i)

    text = y[:]
    y.clear()

    for i in text:
        y.append(ps.stem(i))
    return " ".join(y)
if st.button('predict'):
    transformed_sms = text_transform(input_sms)

    vectorized_sms = tfidf.transform([transformed_sms])

    result = model.predict(vectorized_sms)

    if result == 1:
        st.header('spam')

    else:
        st.header('Not spam')
















