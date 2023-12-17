import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file with total reserves data
excel_file_path = 'data/ReservesData.xlsx'
df = pd.read_excel(excel_file_path)

# Assuming your Excel file has columns 'Date' and 'Total reserves'
# Make sure to replace 'Date' and 'Exchange Rate' with your actual column names
date_col = 'Date'
exchange_rate_col = 'Total Reserves'

# Plot the exchange rate data
plt.figure(figsize=(13,9))
plt.plot(df[date_col], df[exchange_rate_col], label='Total sum of GBP reserves across all banks in the Economic Union', marker='o', zorder=1)
plt.title('Total sum of GBP reserves across all banks in the Economic Union')
plt.xlabel('Date')
plt.ylabel('Total Reserves')
plt.legend()
plt.grid(True)

# Detect possible attacks to our cell (Exchange rate)
#threshold = 0.025  # Threshold to detect a posible attack
#attacks = df[df[exchange_rate_col].pct_change() > threshold]

#Highlight speculative attacks on the chart
#plt.scatter(attacks[date_col], attacks[exchange_rate_col], color='red', label='Attacks', marker='s', zorder=2)

# Convert the date string to a datetime object
date_of_attack = pd.to_datetime('1992-09-16')

# Add a vertical line at the date of September 16, 1992
plt.axvline(x=date_of_attack, color='green', linestyle='--', label='September 16, 1992')

#Show the chart
plt.legend()
plt.show()
