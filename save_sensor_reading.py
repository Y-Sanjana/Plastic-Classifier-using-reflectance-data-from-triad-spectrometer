import serial
import time
import os

port = 'COM3'  # Update to your Arduino port
baud = 115200
output_dir = 'data'
output_path = os.path.join(output_dir, 'sensor_output.csv')

os.makedirs(output_dir, exist_ok=True)

with serial.Serial(port, baud, timeout=10) as ser:
    print("Waiting for Arduino data...")
    time.sleep(3)  # Wait for Arduino reset and startup

    header = ser.readline().decode('utf-8', errors='ignore').strip()
    values = ser.readline().decode('utf-8', errors='ignore').strip()

    print("Header:", header)
    print("Values:", values)

    with open(output_path, 'w') as f:
        f.write(header + '\n')
        f.write(values + '\n')

    print(f"Data saved to {output_path}")
