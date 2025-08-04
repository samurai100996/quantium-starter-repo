import pandas as pd
import os

# Directory with CSV files
data_folder = "data"

# List of all CSVs in the folder
csv_files = [f for f in os.listdir(data_folder) if f.endswith('.csv')]

# Placeholder for all data
all_data = []

# Loop through each CSV
for file in csv_files:
    df = pd.read_csv(os.path.join(data_folder, file))

    # Filter only 'Pink Morsel'
    pink_df = df[df['product'] == 'Pink Morsel'].copy()

    # Calculate sales
    pink_df['sales'] = pink_df['quantity'] * pink_df['price']

    # Select relevant columns
    pink_df = pink_df[['sales', 'date', 'region']]

    all_data.append(pink_df)

# Combine all filtered data
final_df = pd.concat(all_data, ignore_index=True)

# Export to CSV
final_df.to_csv("output.csv", index=False)
print("✅ output.csv created!")
