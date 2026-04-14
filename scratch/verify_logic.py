import pandas as pd
import numpy as np

# Load
sentiment_df = pd.read_csv('data/sentiment_data.csv')
trader_df = pd.read_csv('data/trader_data.csv')

# Prep
sentiment_df['Date'] = pd.to_datetime(sentiment_df['Date'])
trader_df['time'] = pd.to_datetime(trader_df['time'])
trader_df['closedPnL'] = trader_df['closedPnL'].fillna(0)
trader_df['Date'] = trader_df['time'].dt.normalize()

# Merge
df = pd.merge(trader_df, sentiment_df, on='Date', how='left')

# Test grouping
daily_metrics = df.groupby(['Date', 'account', 'Classification']).agg({
    'closedPnL': ['sum', 'count'],
    'leverage': 'mean',
    'size': 'mean',
}).reset_index()

print("Merge and Group successful.")
print(df.columns)
