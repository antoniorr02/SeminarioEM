import pandas as pd
import matplotlib.pyplot as plt
import sys

# Function to simulate a posible attack
def simulate_attack(filtered_df_reserves, start_date, attack_size):
    # Apply the speculative attack by decreasing the exchange rate
    mask = filtered_df_reserves['Date'] >= start_date
    filtered_df_reserves.loc[mask, 'Total Reserves'] -= attack_size

# Check if the script was called with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: python script.py arg1")
    sys.exit(1)

# Retrieve command-line arguments
attack_size = float(sys.argv[1])

# Load your exchange rate data
# If is the first attack (100M) get the real data, else get the continuation of attack
if attack_size == 100:
    excel_file_path = 'data/ReservesData.xlsx'
    df_reserves = pd.read_excel(excel_file_path)
else:
    excel_file_path = 'output/ReservesDataAfterPosibleAttack.xlsx'
    df_reserves = pd.read_excel(excel_file_path)

# Filter the DataFrame based on the date (Before Soros Attack)
date_to_filter = '1992-09-15'
filtered_df_reserves = df_reserves[df_reserves['Date'] <= date_to_filter]

# Example usage of the function to simulate a attack with different dimensions
if (attack_size == 100):
    start_date_attack = '1991-07-1'
elif (attack_size == 200):
    start_date_attack = '1991-07-2'
elif (attack_size == 300):
    start_date_attack = '1991-07-3'
else:
    start_date_attack = '1991-07-4'

#Real Attack scale
attack_size *= 10000000

simulate_attack(filtered_df_reserves, start_date_attack, attack_size)

# Plot the exchange rate data after the speculative attack
plt.figure(figsize=(13, 9))
plt.plot(filtered_df_reserves['Date'], filtered_df_reserves['Total Reserves'], label='Total Reserves', marker='o')
plt.title('Total Reserves after attacks')
plt.xlabel('Date')
plt.ylabel('International Reserves')
plt.legend()
plt.grid(True)
plt.show()

# Save the results to an Excel file
excel_file_path_results = 'output/ReservesDataAfterPosibleAttack.xlsx'
filtered_df_reserves.to_excel(excel_file_path_results, index=False)

#####################


# Load the Excel file with exchange rate data
excel_file_path_exchange = 'data/ExchangeRateData.xlsx'
df_exchange_rate = pd.read_excel(excel_file_path_exchange)

# Filter the DataFrame based on the date (Before Soros Attack)
date_to_filter = '1992-09-15'
filtered_df_exchange_rate = df_exchange_rate[df_exchange_rate['Date'] <= date_to_filter]

# Convert 'Date' columns to datetime format
df_exchange_rate['Date'] = pd.to_datetime(df_exchange_rate['Date'], format='%d/%m/%Y')

df_exchange_rate_monthly = df_exchange_rate.resample('M', on='Date').mean().reset_index()

# Merge the two DataFrames on the 'Date' column
merged_df_exchange_rate = pd.merge(df_exchange_rate_monthly, filtered_df_reserves, on='Date', how='inner')
print(merged_df_exchange_rate)

# Filter the DataFrame based on the date (exchange rate to dates after attacks)
filtered_df_exchange_rate = merged_df_exchange_rate[merged_df_exchange_rate['Date'] >= start_date_attack]

# Open excel with coefficients calculated with linear regression
excel_file_path = 'output/linear_regression_coefficients.xlsx'
df_coefficients = pd.read_excel(excel_file_path)
intercept = df_coefficients.loc[0,'Coefficient']
coefficient = df_coefficients.loc[1,'Coefficient']

# Simulate exchange rate values acording new international reserves
filtered_df_exchange_rate.loc[:,'Exchange Rate'] = ((filtered_df_exchange_rate['Total Reserves'] - intercept) / coefficient).clip(lower=0)


print (filtered_df_exchange_rate)

# Plot the exchange rate data
plt.figure(figsize=(13,9))
plt.plot(merged_df_exchange_rate['Date'], merged_df_exchange_rate['Exchange Rate'], label='GBP to German Marks Exchange Rate', marker='o', zorder=1)
plt.plot(filtered_df_exchange_rate['Date'], filtered_df_exchange_rate['Exchange Rate'], color='green', label='Exchange Rate prediction', marker='s', zorder=1)
plt.title('GBP to German Marks Exchange Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.grid(True)

#Show the chart
plt.legend()
plt.show()

# Save the results to an Excel file
excel_file_path_results = 'output/ExchangeRateAfterPosibleAttack.xlsx'
filtered_df_reserves.to_excel(excel_file_path_results, index=False)

##############################3

## Next code can be used if we want simulate how reserves are when we reduce exchage rate in a value.

# # Load the Excel file with reserves
# excel_file_path = 'data/ReservesData.xlsx'
# df_reserves = pd.read_excel(excel_file_path)
# filtered_df_reserves = df_reserves[df_reserves['Date'] <= date_to_filter]
# merged_df_simulated_reserves = pd.merge(filtered_df, filtered_df_reserves, on='Date', how='inner')

# # Simulate exchage rate with flucuation band
# excel_file_path = 'output/linear_regression_coefficients.xlsx'
# df_coefficients = pd.read_excel(excel_file_path)
# intercept = df_coefficients.loc[0,'Coefficient']
# coefficient = df_coefficients.loc[1,'Coefficient']

# merged_df_simulated_reserves['Total Reserves'] = (intercept + coefficient * merged_df_simulated_reserves['Exchange Rate'])
# print(merged_df_simulated_reserves)

# # Plot the reserves data
# plt.figure(figsize=(13,9))
# plt.plot(merged_df_simulated_reserves['Date'], merged_df_simulated_reserves['Total Reserves'], label='Reserves', marker='o', zorder=1)
# plt.title('International GPB Reserves')
# plt.xlabel('Date')
# plt.ylabel('Total Reserves')
# plt.legend()
# plt.grid(True)
# plt.show()

# # Save the results to an Excel file
# excel_file_path_results = 'output/attack_results.xlsx'
# merged_df_simulated_reserves.to_excel(excel_file_path_results, index=False)