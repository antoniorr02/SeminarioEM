import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error
import matplotlib.pyplot as plt


# Load the Excel file with exchange rate data
excel_file_path_exchange = 'data/ExchangeRateData.xlsx'
df_exchange_rate = pd.read_excel(excel_file_path_exchange)
excel_file_path_reserves = 'data/ReservesData.xlsx'
df_reserves = pd.read_excel(excel_file_path_reserves)

# Assuming your Excel file has columns 'Date' and 'Exchange Rate'
# Make sure to replace 'Date' and 'Exchange Rate' with your actual column names
date_col = 'Date'
exchange_rate_col = 'Exchange Rate'
reserves = 'Total Reserves'

# Assuming you have two pandas DataFrames df_exchange_rate_exchange_rate and df_exchange_rate_reserves
# with columns 'Date' and 'Exchange Rate' for the exchange rate
# and 'Date' and 'International Reserves' for the reserves

# Convert 'Date' columns to datetime format
df_exchange_rate['Date'] = pd.to_datetime(df_exchange_rate['Date'], format='%d/%m/%Y')
df_reserves['Date'] = pd.to_datetime(df_reserves['Date'], format='%d/%m/%Y')

df_exchange_rate_monthly = df_exchange_rate.resample('M', on='Date').mean().reset_index()

# Merge the two DataFrames on the 'Date' column
merged_df_exchange_rate = pd.merge(df_exchange_rate_monthly, df_reserves, on='Date', how='inner')

# # Calculate the daily change in exchange rate
# merged_df_exchange_rate['Exchange Rate Change'] = merged_df_exchange_rate['Exchange Rate'].diff()

# Drop the NaN value resulting from the diff() operation
merged_df_exchange_rate = merged_df_exchange_rate.dropna()

# Select features and target variable
X = merged_df_exchange_rate[['Exchange Rate']]
y = merged_df_exchange_rate['Total Reserves']

# Split the data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Create a linear regression model
model = LinearRegression()

# Train the model
model.fit(X_train, y_train)

# Make predictions on the test set
y_pred = model.predict(X_test)

# Evaluate the model
mse = mean_squared_error(y_test, y_pred)
print(f'Mean Squared Error: {mse}')

# Plot the original data and the linear regression line
plt.scatter(X_test, y_test, color='blue', label='Actual Reserves')
plt.plot(X_test, y_pred, color='red', linewidth=2, label='Linear Regression Prediction')
plt.xlabel('Exchange Rate')
plt.ylabel('International Reserves')
plt.legend()
plt.title('Linear Regression: Exchange Rate vs International Reserves')
plt.show()

############################
# Make predictions on the entire dataset
merged_df_exchange_rate['Reserves Prediction'] = model.predict(X)

# Create a DataFrame to store the results
results_df = merged_df_exchange_rate[['Date', 'Exchange Rate', 'Total Reserves', 'Reserves Prediction']]

# Save the results to an Excel file
excel_file_path_results = 'output/linear_regression_results.xlsx'
results_df.to_excel(excel_file_path_results, index=False)

############################
# Create a DataFrame to store the model coefficients and intercept
coefficients_df = pd.DataFrame({'Feature': X_train.columns, 'Coefficient': model.coef_})

# Add a row for the intercept
intercept_row = pd.DataFrame({'Feature': 'Intercept', 'Coefficient': model.intercept_}, index=[0])
coefficients_df = pd.concat([intercept_row, coefficients_df]).reset_index(drop=True)

# Save the coefficients to an Excel file
excel_file_path = 'output/linear_regression_coefficients.xlsx'
coefficients_df.to_excel(excel_file_path, index=False)

# TOTAL RESERVES = B0 + B1 * EXCHANGE RATE
# TOTAL RESERVES --> y_train
# EXCHANGE RATE --> x_train
# B0 --> model_intercept
# B1 --> model_coeficient