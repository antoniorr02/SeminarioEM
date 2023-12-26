import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file with exchange rate data
excel_file_path = 'data/ExchangeRateData.xlsx'
df_exchange_rate = pd.read_excel(excel_file_path)

# Load the Excel file with reserves
excel_file_path = 'data/ReservesData.xlsx'
df_reserves = pd.read_excel(excel_file_path)

date_col = 'Date'
reserves_col = 'Total Reserves'

# Predicted Reserves (calculated in script LinearRegresionReservesExchangeRate.py)
excel_file_path = 'output/linear_regression_results.xlsx'
df_predicted_reserves = pd.read_excel(excel_file_path)
predicted_reserves = 'Reserves Prediction'

# Plot the reserves data
plt.figure(figsize=(13,9))
plt.plot(df_reserves[date_col], df_reserves[reserves_col], label='Total Reserves', marker='o', zorder=1)
plt.scatter(df_predicted_reserves[date_col], df_predicted_reserves[predicted_reserves], color='green', label='Reserves prediction', marker='s', s=50, zorder=1)
plt.title('International GPB Reserves')
plt.xlabel('Date')
plt.ylabel('Total Reserves')
plt.legend()
plt.grid(True)

#Show the chart
plt.legend()
plt.show()

# Save the results to an Excel file
excel_file_path_results = 'output/reserves_predicted.xlsx'
df_predicted_reserves.to_excel(excel_file_path_results, index=False)