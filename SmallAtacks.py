import pandas as pd
import matplotlib.pyplot as plt
import sys

# Function to simulate a posible attack
def simulate_attack(df, start_date, attack_percentage):
    # Apply the speculative attack by decreasing the exchange rate
    mask = df['Date'] >= start_date
    df.loc[mask, 'Exchange Rate'] *= (1 - attack_percentage)

# Check if the script was called with the correct number of arguments
if len(sys.argv) != 2:
    print("Usage: python script.py arg1")
    sys.exit(1)

# Retrieve command-line arguments
attack_size = float(sys.argv[1])

# Load your exchange rate data
excel_file_path = 'data/ExchangeRateData.xlsx'
df = pd.read_excel(excel_file_path)

# Filter the DataFrame based on the date
date_to_filter = '1992-09-15'
filtered_df = df[df['Date'] <= date_to_filter]

# Example usage of the function to simulate a speculative attack
start_date_attack = '1991-07-1'

simulate_attack(filtered_df, start_date_attack, attack_size)

# Plot the exchange rate data after the speculative attack
plt.figure(figsize=(13, 9))
plt.plot(filtered_df['Date'], filtered_df['Exchange Rate'], label='Exchange Rate', marker='o')
plt.title('GBP to German Marks Exchange Rate Over Time')
plt.xlabel('Date')
plt.ylabel('Exchange Rate')
plt.legend()
plt.grid(True)
plt.show()

#####################

# Load the Excel file with reserves
excel_file_path = 'data/ReservesData.xlsx'
df_reserves = pd.read_excel(excel_file_path)
filtered_df_reserves = df_reserves[df_reserves['Date'] <= date_to_filter]
merged_df_simulated_reserves = pd.merge(filtered_df, filtered_df_reserves, on='Date', how='inner')

# Simulate exchage rate with flucuation band
excel_file_path = 'output/linear_regression_coefficients.xlsx'
df_coefficients = pd.read_excel(excel_file_path)
intercept = df_coefficients.loc[0,'Coefficient']
coefficient = df_coefficients.loc[1,'Coefficient']

merged_df_simulated_reserves['Total Reserves'] = (intercept + coefficient * merged_df_simulated_reserves['Exchange Rate'])
print(merged_df_simulated_reserves)

# Plot the reserves data
plt.figure(figsize=(13,9))
plt.plot(merged_df_simulated_reserves['Date'], merged_df_simulated_reserves['Total Reserves'], label='Reserves', marker='o', zorder=1)
plt.title('International GPB Reserves')
plt.xlabel('Date')
plt.ylabel('Total Reserves')
plt.legend()
plt.grid(True)
plt.show()
