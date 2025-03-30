# ------------------------------------------
# 📚 Import Required Libraries
# ------------------------------------------
import yfinance as yf
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import argrelextrema
import warnings
warnings.filterwarnings("ignore")


# ------------------------------------------
# 🟢 Get Stock Data from Yahoo Finance
# ------------------------------------------
stock_symbol = input("Enter NSE stock symbol (e.g., TCS, RELIANCE): ").upper()
data = yf.download(f"{stock_symbol}.NS", period="1y", auto_adjust=True)

# ------------------------------------------
# 📈 Moving Averages Calculation
# ------------------------------------------
data['50_MA'] = data['Close'].rolling(window=50).mean()
data['200_MA'] = data['Close'].rolling(window=200).mean()

# ------------------------------------------
# 🔥 Detecting Local Extrema for S&R
# ------------------------------------------
data['Min'] = data.iloc[argrelextrema(data['Close'].values, np.less_equal, order=10)[0]]['Close']
data['Max'] = data.iloc[argrelextrema(data['Close'].values, np.greater_equal, order=10)[0]]['Close']

# ------------------------------------------
# 🎯 Filter Key Support/Resistance Levels
# ------------------------------------------
def find_key_levels(levels, threshold=0.01):
    clean_levels = []
    for level in sorted(levels):
        if not clean_levels or all(abs(level - l) / l > threshold for l in clean_levels):
            clean_levels.append(level)
    return clean_levels

# Get unique support and resistance levels
support_levels = find_key_levels(data['Min'].dropna().values, threshold=0.01)
resistance_levels = find_key_levels(data['Max'].dropna().values, threshold=0.01)

# Select only 3-5 strongest levels
top_resistance_levels = sorted(resistance_levels, reverse=True)[:4]
bottom_support_levels = sorted(support_levels)[:4]

# ------------------------------------------
# 🟢 Nearest Support & Resistance Detection
# ------------------------------------------
latest_price = data['Close'].iloc[-1].item()  # Get latest price correctly

# Convert to list to avoid Series ambiguity
bottom_support_levels = list(bottom_support_levels)
top_resistance_levels = list(top_resistance_levels)

# Get nearest support and resistance safely
nearest_support = max([s for s in bottom_support_levels if s <= latest_price], default=None)
nearest_resistance = min([r for r in top_resistance_levels if r >= latest_price], default=None)

# Suggest Buy/Sell Based on Nearest Levels
if nearest_support and nearest_resistance:
    if latest_price <= nearest_support * 1.02:  # Near support zone
        action = "📈 Suggested: BUY near support."
    elif latest_price >= nearest_resistance * 0.98:  # Near resistance zone
        action = "📉 Suggested: SELL near resistance."
    else:
        action = "🔍 Suggested: HOLD. Price is between key levels."
else:
    action = "❗ Unable to determine clear action."

print(f"\n✅ Nearest Support: ₹{nearest_support:.2f}" if nearest_support else "❗ No valid support levels found.")
print(f"✅ Nearest Resistance: ₹{nearest_resistance:.2f}" if nearest_resistance else "❗ No valid resistance levels found.")
print(f"{action}\n")

# ------------------------------------------
# 📊 Plot Stock with Clean Support & Resistance
# ------------------------------------------
plt.figure(figsize=(12, 6))
plt.plot(data.index, data['Close'], label='Stock Price', color='blue')

# Plot Refined Support Levels
for level in bottom_support_levels:
    plt.axhline(y=level, color='green', linestyle='--', label='Support' if level == bottom_support_levels[0] else "")

# Plot Refined Resistance Levels
for level in top_resistance_levels:
    plt.axhline(y=level, color='red', linestyle='--', label='Resistance' if level == top_resistance_levels[0] else "")

# Plot Settings
plt.title(f"📊 {stock_symbol} - Key Support & Resistance Levels")
plt.xlabel('Date')
plt.ylabel('Price (₹)')
plt.legend()
plt.grid(alpha=0.3)
plt.tight_layout()

# Save Cleaned Plot to Downloads
plot_path = f"C:/Users/ragal/Downloads/{stock_symbol}_Final_Support_Resistance.png"
plt.savefig(plot_path)
plt.show()

print(f"✅ Final cleaned support/resistance plot saved as '{plot_path}'!")

# ------------------------------------------
# 📊 Save Processed Data to Excel
# ------------------------------------------
output_path = f"C:/Users/ragal/Downloads/{stock_symbol}_stock_data.xlsx"
with pd.ExcelWriter(output_path, engine='xlsxwriter') as writer:
    data.to_excel(writer, sheet_name='Stock Data')
    worksheet = writer.sheets['Stock Data']

    # Insert Cleaned S&R Plot into Excel
    worksheet.insert_image('J2', plot_path)

print(f"✅ Data and plot saved to '{output_path}' successfully!")
