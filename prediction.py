import joblib
import requests
import streamlit as st

# pkl
phish_model = open('phishing.pkl', 'rb')
phish_model_ls = joblib.load(phish_model)

# ML Aspect
try:
    url = st.text_input("input your URL in here:")
    # url = "http://" + url
    response = requests.get(url)
    response.raise_for_status()  # Periksa jika permintaan berhasil

    url = url.replace("https://", "").replace("http://", "")

    X_predict = []
    X_predict.append(str(url))
    y_Predict = phish_model_ls.predict(X_predict)
        # print(y_Predict)
    if y_Predict == 'bad':
        result = "This is a Phishing Site"
        st.write(result)
    else:
        result = "This is not a Phishing Site"
        st.write(result)

except requests.exceptions.RequestException as e:
    st.write("Gagal memproses, website tidak bisa diakses, kemungkinan website berbahaya")