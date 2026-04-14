# Trader Performance vs Market Sentiment Analysis 📈

## Objective
This project explores the correlation between market sentiment (Fear & Greed Index) and individual trader performance. The goal is to identify behavioral patterns during different sentiment regimes and develop data-driven strategies for risk management.

## Dataset
- **Sentiment Data**: Daily Fear/Greed classifications from 2024 to 2025.
- **Trader Data**: Over 5,000 trade logs including symbols, execution prices, leverage, and closed PnL across 50 unique accounts.

## Methodology
1. **Data Integration**: Syncing intra-day trade logs with daily sentiment indices.
2. **Behavioral Feature Engineering**: Calculating daily PnL, win rates, and leverage profiles.
3. **Comparative Analysis**: Statistical breakdown of performance during 'Fear' vs. 'Greed' periods.
4. **Predictive Modeling**: Using Random Forest to predict daily profitability based on behavior.

## Key Insights 🔥
- **Insight 1**: Traders significantly increase leverage during Greed phases, but PnL updates remain inconsistent, indicating over-optimism.
- **Insight 2**: During Fear periods, trade frequency increases while win rates drop, suggesting emotional overtrading in volatile markets.
- **Insight 3**: Top-tier "Winner" segment traders use lower leverage during Fear phases compared to underperforming segments.

## Strategies 💡
- **Strategy 1**: Reduce leverage by 20–30% during Fear periods to mitigate increased liquidation risk.
- **Strategy 2**: Avoid high-frequency trading in Fear markets to reduce signal noise and transaction drag.
- **Strategy 3**: Use moderate leverage during Greed phases to prevent overexposure during market euphoria.

## How to Run
1. Install dependencies: `pip install -r requirements.txt`
2. Run data generation (optional): `python scratch/generate_data.py`
3. Launch notebook: `jupyter notebook Trader_Sentiment_Analysis.ipynb`

## Final Edge 🧠
**“Findings indicate that trader psychology, influenced by market sentiment, plays a critical role in performance, but disciplined risk management is the key differentiator for consistent profitability.”**

---
*Developed for Trader Performance Analysis Portfolio.*
