import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import tensorflow as tf
from sklearn.preprocessing import MinMaxScaler

# Load your data
data = pd.read_csv(r"C:\Users\Shane Nosack\Desktop\Coding Dojo\Python\TensorFlow\Predict\prices\2020_2024.csv")
data['Date'] = pd.to_datetime(data['Date'])
data.set_index('Date', inplace=True)

# Reverse the DataFrame
data = data.iloc[::-1]

# Inspect the columns
print("Columns in the DataFrame:", data.columns)

# Strip any leading or trailing spaces in column names
data.columns = data.columns.str.strip()

# Ensure the 'Price' column exists and is correctly named
if 'Price' in data.columns:
    # Remove commas and convert to numeric
    data['Price'] = data['Price'].str.replace(',', '').astype(float)
    prices = data['Price'].values.reshape(-1, 1)
else:
    raise KeyError("The 'Price' column is not found in the DataFrame.")

# Normalize the data
scaler = MinMaxScaler(feature_range=(0, 1))
scaled_prices = scaler.fit_transform(prices)

# Create sequences for LSTM
def create_sequences(data, seq_length):
    sequences = []
    for i in range(len(data) - seq_length):
        sequences.append(data[i:i + seq_length])
    return np.array(sequences)

SEQ_LENGTH = 60
X = create_sequences(scaled_prices, SEQ_LENGTH)
y = scaled_prices[SEQ_LENGTH:]

# Split the data into training and validation sets
split = int(0.8 * len(X))
X_train, X_val = X[:split], X[split:]
y_train, y_val = y[:split], y[split:]

# Create the Model
model = tf.keras.Sequential([
    tf.keras.layers.LSTM(50, return_sequences=True, input_shape=(SEQ_LENGTH, 1)),
    tf.keras.layers.LSTM(50, return_sequences=False),
    tf.keras.layers.Dense(25),
    tf.keras.layers.Dense(1)
])

model.compile(optimizer='adam', loss='mean_squared_error')

# Model summary
model.summary()

# Train the Model
history = model.fit(X_train, y_train, batch_size=64, epochs=100, validation_data=(X_val, y_val))

# Plot training & validation loss values
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Model loss')
plt.ylabel('Loss')
plt.xlabel('Epoch')
plt.legend(['Train', 'Validation'], loc='upper right')
plt.show()

# Make predictions
predicted_prices = model.predict(X_val)
predicted_prices = scaler.inverse_transform(predicted_prices)

# Plot actual vs predicted prices
actual_prices = scaler.inverse_transform(y_val)

plt.figure(figsize=(14,5))
plt.plot(actual_prices, color='black', label='Actual Bitcoin Price')
plt.plot(predicted_prices, color='green', label='Predicted Bitcoin Price')
plt.title('Bitcoin Price Prediction')
plt.xlabel('Time')
plt.ylabel('Bitcoin Price')
plt.legend()
plt.show()

# Save the Model
model.save('bitcoin_price_predictor.keras')
