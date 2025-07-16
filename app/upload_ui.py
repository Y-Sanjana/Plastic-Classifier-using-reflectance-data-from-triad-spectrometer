import streamlit as st
import pandas as pd
import joblib
import matplotlib.pyplot as plt

# Load models and scalers
scaler = joblib.load('models/scaler.joblib')
label_encoder = joblib.load('models/label_encoder.joblib')
rf_model = joblib.load('models/rf_model.joblib')
svm_model = joblib.load('models/svm_model.joblib')

st.set_page_config(page_title="Plastic Classifier", layout="centered")
st.title("🧪 Plastic Classifier (CSV Upload)")
st.markdown("Upload a **.csv file** with exactly **18 values** from your plastic sensor (410–940nm).")

uploaded_file = st.file_uploader("📤 Upload CSV file", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file, header=0)

        if df.shape != (1, 18):
            st.error("❌ Uploaded file must contain exactly **1 row and 18 columns**.")
        else:
            sensor_values = df.values.flatten().astype(float)
            X_scaled = scaler.transform([sensor_values])

            # Predict
            rf_pred = rf_model.predict(X_scaled)[0]
            svm_pred = svm_model.predict(X_scaled)[0]

            rf_label = label_encoder.inverse_transform([rf_pred])[0]
            svm_label = label_encoder.inverse_transform([svm_pred])[0]

            rf_proba = rf_model.predict_proba(X_scaled)[0]
            svm_proba = svm_model.predict_proba(X_scaled)[0]

            st.success("✅ Sensor data uploaded and processed.")

            # Show predictions
            st.markdown("## Predicted Plastics")
            col1, col2 = st.columns(2)

            with col1:
                st.subheader("Random Forest")
                st.write(f"**Prediction:** {rf_label}")
                st.bar_chart(pd.Series(rf_proba, index=label_encoder.classes_))

            with col2:
                st.subheader("SVM")
                st.write(f"**Prediction:** {svm_label}")
                st.bar_chart(pd.Series(svm_proba, index=label_encoder.classes_))

            # Plot spectrum
            st.markdown("## Reflectance Spectrum")
            wavelengths = list(map(int, df.columns))
            fig, ax = plt.subplots(figsize=(8, 4))
            ax.plot(wavelengths, sensor_values, marker='o', color='seagreen')
            ax.set_xlabel("Wavelength (nm)")
            ax.set_ylabel("Reflectance")
            ax.set_title("Plastic Sample Spectrum")
            ax.grid(True)
            st.pyplot(fig)

    except Exception as e:
        st.error(f"⚠️ Error reading or processing file: {e}")
else:
    st.info("👈 Upload your `.csv` file from the Arduino reading to begin.")
