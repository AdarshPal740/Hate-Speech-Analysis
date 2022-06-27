import streamlit as st
import pickle
import string
from nltk.corpus import stopwords
import nltk
from nltk.stem.snowball import SnowballStemmer
import re
stemmer = nltk.SnowballStemmer("english")
def clean(text):
    text = str(text).lower()
    text = re.sub('\[.*?\]', '', text)
    text = re.sub('https?://\S+|www\.\S+', '', text)
    text = re.sub('<.*?>+', '', text)
    text = re.sub('[%s]' % re.escape(string.punctuation), '', text)
    text = re.sub('\n', '', text)
    text = re.sub('\w*\d\w*', '', text)
    text = [word for word in text.split(' ') if word not in stopwords.words('english')]
    text=" ".join(text)
    text = [stemmer.stem(word) for word in text.split(' ')]
    text=" ".join(text)
    return text
cv=pickle.load(open('CV.pkl','rb'))
clf=pickle.load(open('CLF.pkl','rb'))
st.title("Twitter Sentiment Analysis")
input_sent=st.text_area("Enter the sentencs")
if st.button('Predict'):
    transformed_sent=clean(input_sent)
    vector_input=cv.transform([transformed_sent])  
    result=clf.predict(vector_input)
    print(result)
    if result=='Hate Speech':
        st.header("Hate Speech")
    if result=='Offensive Language':
        st.header("Offensive Language")
    if result=='No Hate and Offensive':
        st.header("No Hate and Offensive")        