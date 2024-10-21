import pandas as pd

# Define file paths
user_transactions_file_directory = '/content/TaoYin_User_Transactions_v2.parquet'
item_features_file_directory = '/content/Tao Yin_Item_features.parquet'

# Read the parquet files
df_ut = pd.read_parquet(user_transactions_file_directory)
df_if = pd.read_parquet(item_features_file_directory)

# Rename columns for consistency
df_if.rename(columns={'Articlenr': 'articlenr'}, inplace=True)
df_ut.rename(columns={'artikelnr': 'articlenr'}, inplace=True)

# Merge the DataFrames on 'articlenr'
merged_df = pd.merge(df_ut, df_if[['articlenr', 'ETIM']], on='articlenr', how='inner')

# Check the number of common 'articlenr' values
num_common_articlenr = merged_df.shape[0]
print(f"Number of common 'articlenr' values: {num_common_articlenr}")

# Optionally, check unique common 'articlenr' values
num_unique_common_articlenr = merged_df['articlenr'].nunique()
print(f"Number of unique common 'articlenr' values: {num_unique_common_articlenr}")

# Print just the first 5 rows of the merged DataFrame
print("First 5 rows of the merged DataFrame:\n", merged_df.head(5))
