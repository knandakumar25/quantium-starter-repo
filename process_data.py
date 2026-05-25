import pandas as pd
import os

# Define file paths
data_dir = './data'
input_files = [
    'daily_sales_data_0.csv',
    'daily_sales_data_1.csv',
    'daily_sales_data_2.csv'
]
output_file = './data/formatted_daily_sales.csv'

# Initialize an empty list to hold dataframes
dfs = []

for file in input_files:
    file_path = os.path.join(data_dir, file)
    # Read the CSV
    df = pd.read_csv(file_path)
    
    # Filter for 'pink morsel'
    df = df[df['product'] == 'pink morsel']
    
    # Clean the 'price' column (remove '$' and convert to float)
    df['price'] = df['price'].str.replace('$', '').astype(float)
    
    # Calculate 'sales'
    df['sales'] = df['price'] * df['quantity']
    
    # Select specific columns
    df = df[['sales', 'date', 'region']]
    
    # Append to our list
    dfs.append(df)

# Combine all dataframes into a single one
combined_df = pd.concat(dfs, ignore_index=True)

# Write to the output CSV
combined_df.to_csv(output_file, index=False)

print(f"Successfully processed data and saved to {output_file}")
