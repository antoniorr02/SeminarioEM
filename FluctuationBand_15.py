import pandas as pd
import matplotlib.pyplot as plt

# Load the Excel file with exchange rate data
excel_file_path = 'data/ExchangeRateData.xlsx'
df = pd.read_excel(excel_file_path)

# Assuming your Excel file has columns 'Date' and 'Exchange Rate'
# Make sure to replace 'Date' and 'Exchange Rate' with your actual column names
date_col = 'Date'
exchange_rate_col = 'Exchange Rate'

# Filter the DataFrame based on the date
date_to_filter = '1992-09-16'
filtered_df = df[df['Date'] == date_to_filter]

# Access the exchange_rate_col for the specified date
exchange_rate_value = filtered_df['Exchange Rate'].iloc[0]

print(f'The exchange rate on {date_to_filter} is: {exchange_rate_value}')

valid_condition = df[exchange_rate_col] >= exchange_rate_value
invalid_condition = ~valid_condition

# Create a new DataFrame for invalid values
invalid_df = df[invalid_condition].copy()

# Set the exchange_rate_value for invalid dates
invalid_df[exchange_rate_col] = exchange_rate_value

# Plot the exchange rate data
plt.figure(figsize=(13,9))
plt.plot(df.loc[valid_condition, date_col], df.loc[valid_condition, exchange_rate_col], label='GBP to German Marks Exchange Rate', marker='o', zorder=1)
plt.scatter(df.loc[invalid_condition, date_col], df.loc[invalid_condition, exchange_rate_col], color='red', label='Invalid GBP to German Marks Exchange Rate', marker='x', s=50, zorder=1)
plt.scatter(invalid_df[date_col], invalid_df[exchange_rate_col], color='yellow', label='New GBP to German Marks Exchange Rate', marker='x', s=50, zorder=2)
plt.title('GBP to German Marks Exchange Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.grid(True)

# Convert the date string to a datetime object (Fluctuation band from 2.25 to 15%)
date_of_change = pd.to_datetime('1992-09-16')

# Add a vertical line at the date of September 16, 1992
plt.axvline(x=date_of_change, color='green', linestyle='--', label='September 16, 1992')

#Highlight miniminum value exchange rate on the chart
plt.scatter(date_of_change, exchange_rate_value, color='black', label='Mininimun 15%', marker='s', zorder=2)

# Find the minimum value in the 'Exchange Rate' column
min_exchange_rate = df[exchange_rate_col].min()
filtered_df_min_date = df[df['Exchange Rate'] == min_exchange_rate]
print(f'The minimum exchange rate is: {min_exchange_rate} on {pd.to_datetime(filtered_df_min_date[date_col])}')
#Highlight miniminum value exchange rate on the chart
plt.scatter(filtered_df_min_date[date_col], min_exchange_rate, color='purple', label='Mininimun value', marker='s', zorder=2)
# Add a vertical line at the date of September 16, 1992
plt.axvline(x=filtered_df_min_date[date_col], color='purple', linestyle='--')

#Show the chart
plt.legend()
plt.show()

##################################################

# Load the Excel file with reserves
excel_file_path = 'data/ReservesData.xlsx'
df_reserves = pd.read_excel(excel_file_path)

date_col = 'Date'
reserves_col = 'Total Reserves'

# Filter the DataFrame based on the date
date_to_filter_reserves = '1992-08-31'
filtered_df_reserves_before = df_reserves[df_reserves['Date'] <= date_to_filter_reserves]
filtered_df_reserves_after = df_reserves[df_reserves['Date'] > date_to_filter_reserves]

# Plot the reserves data
plt.figure(figsize=(13,9))
plt.plot(filtered_df_reserves_before[date_col], filtered_df_reserves_before[reserves_col], label='Reserves Before Quit Flutuation Band', marker='o', zorder=1)
plt.scatter(filtered_df_reserves_after[date_col], filtered_df_reserves_after[reserves_col], color='red', label='Invalid Reserves', marker='x', s=50, zorder=1)
plt.title('International GPB Reserves')
plt.xlabel('Date')
plt.ylabel('Total Reserves')
plt.legend()
plt.grid(True)

# Convert the date string to a datetime object (Fluctuation band from 2.25 to 15%)
date_of_change = pd.to_datetime('1992-08-31')

# Add a vertical line at the date of September 16, 1992
plt.axvline(x=date_of_change, color='green', linestyle='--', label='September, 1992')

#Show the chart
plt.legend()
plt.show()



