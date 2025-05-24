import streamlit as st
import joblib
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Load model components
model = joblib.load('./model/model.pkl')
le = joblib.load(
    'model/label_encoder.pkl')

# Selected features
selected_features = [
    'Marital_status', 'Application_order', 'Admission_grade', 'Displaced',
    'Debtor', 'Gender', 'Scholarship_holder', 'Age_at_enrollment'
]

# Categorical mappings
marital_status_mapping = {'Single': 1, 'Married': 2, 'Widower': 3,
                          'Divorced': 4, 'Facto union': 5, 'Legally separated': 6}
displaced_mapping = {'Yes': 1, 'No': 0}
debt_status_mapping = {'Yes': 1, 'No': 0}
gender_mapping = {'Male': 0, 'Female': 1}
scholarship_holder_mapping = {'Yes': 1, 'No': 0}

# Page title
st.set_page_config(
    page_title="🏫Student Dropout Prediction 🏫", layout="centered")
st.title("🎓 Student Dropout Prediction")
st.markdown(
    "Masukkan data mahasiswa untuk memprediksi apakah akan **Dropout** atau **Lulus**.")

# Input layout
st.subheader("📋 Data Mahasiswa")
inputs = {}

for idx, feature in enumerate(selected_features):
    if feature == 'Marital_status':
        inputs[feature] = st.selectbox(
            "Status Pernikahan", marital_status_mapping.keys(), key=f"{feature}_{idx}")
    elif feature == 'Application_order':
        inputs[feature] = st.number_input(
            "Urutan Pilihan Program Studi", min_value=1, max_value=9, step=1, key=f"{feature}_{idx}")
    elif feature == 'Admission_grade':
        inputs[feature] = st.number_input(
            "Nilai Penerimaan (0 - 200)", min_value=0, max_value=200, key=f"{feature}_{idx}")
    elif feature == 'Displaced':
        inputs[feature] = st.selectbox(
            "Apakah Mahasiswa Terlantar?", displaced_mapping.keys(), key=f"{feature}_{idx}")
    elif feature == 'Debtor':
        inputs[feature] = st.selectbox(
            "Apakah Mahasiswa Memiliki Hutang?", debt_status_mapping.keys(), key=f"{feature}_{idx}")
    elif feature == 'Gender':
        inputs[feature] = st.selectbox(
            "Jenis Kelamin", gender_mapping.keys(), key=f"{feature}_{idx}")
    elif feature == 'Scholarship_holder':
        inputs[feature] = st.selectbox(
            "Penerima Beasiswa?", scholarship_holder_mapping.keys(), key=f"{feature}_{idx}")
    elif feature == 'Age_at_enrollment':
        inputs[feature] = st.number_input(
            "Usia Saat Masuk Kuliah", min_value=10, max_value=100, key=f"{feature}_{idx}")

# Convert inputs
input_values = []
for feature in selected_features:
    if feature == 'Marital_status':
        input_values.append(marital_status_mapping[inputs[feature]])
    elif feature == 'Displaced':
        input_values.append(displaced_mapping[inputs[feature]])
    elif feature == 'Debtor':
        input_values.append(debt_status_mapping[inputs[feature]])
    elif feature == 'Gender':
        input_values.append(gender_mapping[inputs[feature]])
    elif feature == 'Scholarship_holder':
        input_values.append(scholarship_holder_mapping[inputs[feature]])
    else:
        input_values.append(float(inputs[feature]))

# Prediction process
input_df = pd.DataFrame([input_values], columns=selected_features)


if st.button("🔍 Make Prediction"):
    prediction = model.predict(input_df)
    prediction_label = le.inverse_transform(prediction)[0]
    proba = model.predict_proba(input_df)[0]
    confidence = np.max(proba) * 100

    # Output result
    if prediction_label.lower() == "dropout":
        st.error(
            f"🚨 Prediksi: {prediction_label}\n\n❗ Tingkat Keyakinan: {confidence:.2f}%")
    else:
        st.success(
            f"✅ Prediksi: {prediction_label}\n\n🎯 Tingkat Keyakinan: {confidence:.2f}%")

    # Optional: visualisasi probabilitas
    st.subheader("📈 Probabilitas Klasifikasi")
    prob_df = pd.DataFrame({
        'Status': le.classes_,
        'Probabilitas (%)': proba * 100
    })
    st.bar_chart(prob_df.set_index('Status'))
