import joblib
import requests
import streamlit as st

def load_view():
    phish_model = open('phishing.pkl', 'rb')
    phish_model_ls = joblib.load(phish_model)

    url = st.text_input("input your URL in here:")

    if url:
        st.cache_data
        url_check(url, phish_model, phish_model_ls)
        
def url_check(url, phish_model, phish_model_ls):
    try:
        response = requests.get(url)
        response.raise_for_status()

        url = url.replace("https://", "").replace("http://", "")

        X_predict = []
        X_predict.append(str(url))
        y_Predict = phish_model_ls.predict(X_predict)
            
        if y_Predict == 'bad':
            result = "This is a Phishing Site"
        else:
            result = "This is not a Phishing Site"

        st.write(result)

    except requests.exceptions.RequestException as e:
        st.write("Gagal memproses, website tidak bisa diakses, kemungkinan website berbahaya")
