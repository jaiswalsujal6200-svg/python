import pandas as pd
import matplotlib.pyplot as plt

# Load dataset
df = pd.read_csv("weather.csv")

print("\n--- Dataset Head ---")
print(df.head())

print("\n--- Dataset Info ---")
print(df.info())

print("\n--- Dataset Describe ---")
print(df.describe())

# --- Clean & Prepare Data ---
# Convert date column
df['date'] = pd.to_datetime(df['date'], dayfirst=True, errors='coerce')

# Remove rows with invalid dates
df = df.dropna(subset=['date'])

# Sort by date
df = df.sort_values(by='date')

# --- Plotting ---
plt.figure(figsize=(12, 8))

# Temperature Plot
plt.subplot(2, 1, 1)
plt.plot(df['date'], df['temperature'], marker='o', linestyle='-', color='blue')
plt.title("Temperature Trend")
plt.xlabel("Date")
plt.ylabel("Temperature (°C)")
plt.grid(True)

# Humidity Plot
plt.subplot(2, 1, 2)
plt.plot(df['date'], df['humidity'], marker='o', linestyle='-', color='orange')
plt.title("Humidity Trend")
plt.xlabel("Date")
plt.ylabel("Humidity (%)")
plt.grid(True)

plt.tight_layout()
plt.show()
