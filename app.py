
import streamlit as st
import pickle
import nltk
nltk.download('punkt_tab')
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer
import string
ps = PorterStemmer()
model = pickle.load(open('model.pkl', 'rb'))
tfidf = pickle.load(open('vectorizer.pkl', 'rb'))
st.header(":blue[sms spam detector]", divider=True)
# st.image('spam.png', width = 500)
st.caption('Check whether a message is spam or not.')
input_sms = st.text_area(':blue-badge[Enter the message]')

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
if st.button('predict',type = 'primary'):
    transformed_sms = text_transform(input_sms)

    vectorized_sms = tfidf.transform([transformed_sms])

    result = model.predict(vectorized_sms)

    if result == 1:
        st.header('spam')

    else:
        st.header('Not spam')
















