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
merged_df = pd.merge(df_ut, df_if, on='articlenr', how='inner')

# Display the first 5 rows of the merged DataFrame
print("First 5 rows of the merged DataFrame:\n", merged_df.head(5))
