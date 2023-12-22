import pandas as pd
import matplotlib.pyplot as plt


# Load the Excel file with exchange rate data
excel_file_path_exchange = 'data/ExchangeRateData.xlsx'
df_exchange_rate = pd.read_excel(excel_file_path_exchange)

# Assuming your Excel file has columns 'Date' and 'Exchange Rate'
# Make sure to replace 'Date' and 'Exchange Rate' with your actual column names
date_col = 'Date'
exchange_rate_col = 'Exchange Rate'

# Filter the DataFrame based on the date
date_to_filter = '1992-09-15'
filtered_df_exchange_rate = df_exchange_rate[df_exchange_rate['Date'] == date_to_filter]

# Access the exchange_rate_col for the specified date
exchange_rate_value = filtered_df_exchange_rate['Exchange Rate'].iloc[0]

print(f'The exchange rate on {date_to_filter} is: {exchange_rate_value}')

valid_condition = df_exchange_rate[exchange_rate_col] >= exchange_rate_value
invalid_condition = ~valid_condition

# Create a new DataFrame for invalid values
invalid_df_exchange_rate = df_exchange_rate[invalid_condition].copy()

# Set the exchange_rate_value for invalid dates
invalid_df_exchange_rate[exchange_rate_col] = exchange_rate_value

# Plot the exchange rate data
plt.figure(figsize=(13,9))
plt.plot(df_exchange_rate.loc[valid_condition, date_col], df_exchange_rate.loc[valid_condition, exchange_rate_col], label='GBP to German Marks Exchange Rate', marker='o', zorder=1)
plt.scatter(df_exchange_rate.loc[invalid_condition, date_col], df_exchange_rate.loc[invalid_condition, exchange_rate_col], color='red', label='Invalid GBP to German Marks Exchange Rate', marker='x', s=50, zorder=1)
plt.scatter(invalid_df_exchange_rate[date_col], invalid_df_exchange_rate[exchange_rate_col], color='yellow', label='New GBP to German Marks Exchange Rate', marker='x', s=50, zorder=2)
plt.title('GBP to German Marks Exchange Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.grid(True)

# Convert the date string to a datetime object (Fluctuation band from 2.25 to 15%)
date_of_change = pd.to_datetime('1992-09-15')

# Add a vertical line at the date of September 16, 1992
plt.axvline(x=date_of_change, color='green', linestyle='--', label='September 15, 1992')

#Highlight miniminum value exchange rate on the chart
plt.scatter(date_of_change, exchange_rate_value, color='black', label='Mininimun 2.25%', marker='s', zorder=2)

# Find the minimum value in the 'Exchange Rate' column
min_exchange_rate = df_exchange_rate[exchange_rate_col].min()
filtered_df_exchange_rate_min_date = df_exchange_rate[df_exchange_rate['Exchange Rate'] == min_exchange_rate]
print(f'The minimum exchange rate is: {min_exchange_rate} on {pd.to_datetime(filtered_df_exchange_rate_min_date[date_col])}')
#Highlight miniminum value exchange rate on the chart
plt.scatter(filtered_df_exchange_rate_min_date[date_col], min_exchange_rate, color='purple', label='Mininimun value', marker='s', zorder=2)
# Add a vertical line at the date of September 16, 1992
plt.axvline(x=filtered_df_exchange_rate_min_date[date_col], color='purple', linestyle='--')

#Show the chart
plt.legend()
plt.show()

# Obtain diferences between real values and values with 2.25 fluctuation band
# exchange_rate_diferences = exchange_rate_value - df_exchange_rate.loc[invalid_condition, exchange_rate_col]
# print(f'The maximun diference exchange rate is: {exchange_rate_diferences.max()}')
# # Check levels of international reserves supporting the diferences
# # Calculate the differences intraday
# differences = exchange_rate_diferences.diff()
#for diference in differences:
    # Sum international reserves (we have positive and negative diferences)