# Plastic Classifier

This project is a plastic classifier that uses triad spectroscopy sensor (AS7265X) data to identify types of plastic materials namely PET,PP,HDPE,LDPE. It consists of two main components: a data collection script that reads sensor data from an Arduino device, and a Streamlit web application that allows users to upload sensor data in CSV format and predicts the plastic type using machine learning models.

## Features

- Collect sensor data from an Arduino nano / uno via serial communication.
- Upload sensor data CSV files through a user-friendly Streamlit interface.
- Predict plastic type using two machine learning models: Random Forest and Support Vector Machine (SVM).
- Visualize the reflectance spectrum of the plastic sample.
- Display prediction probabilities for both models.

## Installation

1. Clone the repository or download the project files.

2. It is recommended to create a virtual environment:

```bash
python -m venv venv
```

3. Activate the virtual environment:

- On Windows:

```bash
venv\Scripts\activate
```

- On macOS/Linux:

```bash
source venv/bin/activate
```

4. Install the required dependencies:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Collect  Sensor Data

Connect your Arduino device to the appropriate serial port (default is `COM3` in `save_sensor_reading.py`). Run the script to read sensor data and save it to a CSV file:

```bash
python save_sensor_reading.py
```

This will create a `sensor_output.csv` file in the `data` directory containing the sensor readings.

### 2. Run the Streamlit Web Application

Launch the Streamlit app to upload the sensor data CSV and classify the plastic type:

```bash
streamlit run app/upload_ui.py
```

- Upload a CSV file with exactly 18 sensor values (one row, 18 columns).
- The app will display predictions from both Random Forest and SVM models.
- It will also plot the reflectance spectrum of the uploaded sample.

## Project Structure

```
plastic_classifier/
│
├── app/
│   └── upload_ui.py          # Streamlit web app for uploading and classifying sensor data
│
├── data/
│   ├── plastic_dataset (1).csv  # Dataset file (example)
│   └── sensor_output.csv         # Sensor data output from Arduino
│
├── models/
│   ├── label_encoder.joblib   # Label encoder for plastic types
│   ├── rf_model.joblib        # Random Forest model
│   ├── scaler.joblib          # Scaler for sensor data
│   └── svm_model.joblib       # Support Vector Machine model
│
├── save_sensor_reading.py     # Script to read sensor data from Arduino
├── requirements.txt           # Python dependencies
└── README.md                  # Project documentation (this file)
```

## Dependencies

- numpy
- pandas
- scikit-learn==1.6.1
- joblib
- matplotlib
- seaborn
- streamlit
- plotly
- openpyxl

## Notes

- Ensure your Arduino is connected to the correct serial port and the baud rate matches in `save_sensor_reading.py`.
- The uploaded CSV file must have exactly 18 values corresponding to sensor readings at wavelengths 410–940nm.

## License

This project is provided as-is without any warranty. Feel free to modify and use it as needed.

## Author

Y SANJANA
