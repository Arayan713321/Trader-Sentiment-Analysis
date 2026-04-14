# Trader Performance vs Market Sentiment Analysis 🚀🔥

## Objective
To analyze the measurable impact of market sentiment (Fear & Greed Index) on individual trader behavior and overall profitability.

## Dataset
- **Sentiment Data**: Daily classifications (Fear, Greed, Neutral, etc.).
- **Trader Data**: Transaction-level logs including leverage, price, and PnL.

## Methodology
1. **Cleaning**: Datetime conversion and missing value imputation.
2. **Merging**: Aligning trade data with sentiment regimes.
3. **Feature Engineering**: Calculating Win Rates, Daily PnL, and Risk Metrics.
4. **Segmentation**: Categorizing traders by risk and activity levels.
5. **Modeling**: Predictive analysis using Random Forest.

## Key Insights
- **Insight 1**: Traders significantly increase leverage during Greed phases. However, the increase in PnL is inconsistent. (Market optimism leads to risk-taking without guaranteed returns).
- **Insight 2**: During Fear periods, trade frequency increases but win rate drops. (Traders overtrade in volatile markets, reducing profitability).
- **Insight 3**: Consistently profitable traders use lower leverage during Fear. (Successful traders adapt risk instead of reacting emotionally).

## Strategies
- **Strategy 1**: Reduce leverage by 20–30% during Fear periods.
- **Strategy 2**: Avoid high-frequency trading in Fear markets.
- **Strategy 3**: Use moderate leverage during Greed, not maximum.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run data generation: `python scratch/generate_data.py`
3. Execute Notebook: `Trader_Performance_vs_Market_Sentiment.ipynb`

## Final Edge 🧠
**“Findings indicate that trader psychology, influenced by market sentiment, plays a critical role in performance, but disciplined risk management is the key differentiator for consistent profitability.”**
