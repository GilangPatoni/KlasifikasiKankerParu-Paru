import pickle
import numpy as np
import streamlit as st

model = pickle.load(open('lung_cancer.sav', 'rb'))

st.title('Klasifikasi Kanker Paru-paru')
kol1, kol2, kol3 = st.columns(3)

with kol1:
    SMOKING = st.number_input('Perokok (1 = Tidak; 2 = Ya)')
    PEER_PRESSURE = st.number_input('Pengaruh Teman (1 = Tidak; 2 = Ya)')
    ALLERGY = st.number_input('Alergi (1 = Tidak; 2 = Ya)')
    COUGHING = st.number_input('Batuk (1 = Tidak; 2 = Ya)')
    CHEST_PAIN = st.number_input('Nyeri Dada (1 = Tidak; 2 = Ya)')

with kol2:
    YELLOW_FINGERS = st.number_input('Jari Kuning (1 = Tidak; 2 = Ya)')
    CHRONIC_DISEASE = st.number_input('Penyakit Kronis (1 = Tidak; 2 = Ya)')
    WHEEZING = st.number_input('Mengi (suara bernada tinggi yang dihasilkan saat bernapas) (1 = Tidak; 2 = Ya)')
    SHORTNESS_OF_BREATH = st.number_input('Sesak Nafas (1 = Tidak; 2 = Ya)')

with kol3:
    ANXIETY = st.number_input('Kecemasan (1 = Tidak; 2 = Ya)')
    FATIGUE = st.number_input('Kelelahan (1 = Tidak; 2 = Ya)')
    ALCOHOL_CONSUMING = st.number_input('Mengkonsumsi Minuman Keras (1 = Tidak; 2 = Ya)')
    SWALLOWING_DIFFICULTY = st.number_input('Sulit Menelan (1 = Tidak; 2 = Ya)')

prediksi = ''
if st.button('Hasil Prediksi'):
    prediksi = model.predict([[SMOKING, YELLOW_FINGERS, ANXIETY, PEER_PRESSURE, CHRONIC_DISEASE,
                               FATIGUE, ALLERGY, WHEEZING, ALCOHOL_CONSUMING, COUGHING,
                               SHORTNESS_OF_BREATH, SWALLOWING_DIFFICULTY, CHEST_PAIN]])

    if (prediksi[0] == 1):
        prediksi = 'Pasien Terkena Kanker Paru-paru'
    else:
        prediksi = 'Pasien Tidak Terkena Kanker Paru-paru'
st.success(prediksi)