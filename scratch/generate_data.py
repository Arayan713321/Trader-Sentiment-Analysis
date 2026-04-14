import pandas as pd
import numpy as np
from datetime import datetime, timedelta

# Set seed for reproducibility
np.random.seed(42)

# 1. Sentiment Data Generation
dates = pd.date_range(start='2024-01-01', end='2025-12-31', freq='D')
classifications = ['Extreme Fear', 'Fear', 'Neutral', 'Greed', 'Extreme Greed']
sentiment_df = pd.DataFrame({
    'Date': dates,
    'Classification': np.random.choice(classifications, size=len(dates), p=[0.1, 0.25, 0.3, 0.25, 0.1])
})

sentiment_df.to_csv('data/sentiment_data.csv', index=False)
print("Created data/sentiment_data.csv")

# 2. Trader Data Generation
num_trades = 5000
traders = [f'TRD_{i:03d}' for i in range(1, 51)] # 50 traders
symbols = ['BTCUSDT', 'ETHUSDT', 'SOLUSDT', 'BNBUSDT']
sides = ['LONG', 'SHORT']

trade_times = [datetime(2024, 1, 1) + timedelta(minutes=np.random.randint(0, 365*2*24*60)) for _ in range(num_trades)]
trade_times.sort()

trader_data = {
    'account': np.random.choice(traders, size=num_trades),
    'symbol': np.random.choice(symbols, size=num_trades),
    'execution_price': np.random.uniform(20000, 70000, size=num_trades),
    'size': np.random.uniform(0.01, 2.0, size=num_trades),
    'side': np.random.choice(sides, size=num_trades),
    'time': trade_times,
    'closedPnL': np.random.normal(loc=10, scale=500, size=num_trades), # Slightly positive mean
    'leverage': np.random.choice([1, 5, 10, 20, 50, 100], size=num_trades, p=[0.2, 0.3, 0.2, 0.15, 0.1, 0.05])
}

trader_df = pd.DataFrame(trader_data)
# Add some missing values for cleaning practice
trader_df.loc[np.random.choice(trader_df.index, 50), 'closedPnL'] = np.nan

trader_df.to_csv('data/trader_data.csv', index=False)
print("Created data/trader_data.csv")
