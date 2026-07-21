# Natural Gas Spot Price Forecasting

This project forecasts the daily Henry Hub natural gas spot price using four different modelling approaches — SARIMA, Random Forest, XGBoost, and LSTM — and then studies the volatility of the price series with a GARCH(1,1) model. It was built for the "Advanced Time Series Forecasting" assignment.

## Project structure

```
project/
├── data/
│   ├── raw/
│   │   └── DHHNGSP.csv              
│   └── processed/
│       └── cleaned_featured_data.csv 
├── notebooks/
│   ├── EDA_Decomposition.ipynb     
│   ├── Forecasting_Models.ipynb    
│   ├── Volatility_GARCH.ipynb        
│   └── Final_Comparison_Reflection.ipynb 
│   ├── point_metrics.json            
│   ├── garch_metrics.json            
│   └── model_comparison_plots.png    
├── src/
│   └── engine.py                     
├── requirements.txt
└── README.md
```

## Dataset

- **Source:** Federal Reserve Economic Data (FRED), series ID `DHHNGSP` — Henry Hub Natural Gas Spot Price ($/MMBtu).
- **Frequency:** Daily (business days).
- **Coverage:** 13 July 2021 – 13 July 2026 (1,305 rows, 57 of which were originally missing).
- **Target:** Next-day spot price. The final 20% of the series (255 observations) is held out as the test set for the point-forecast models; the GARCH model uses the last 10% of the return series.

## How to run

1. Create a virtual environment and install the dependencies:

   ```bash
   python -m venv venv
   source venv/bin/activate        # on Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. Run the notebooks in this order, from inside the `notebooks/` folder

   1. `EDA_Decomposition.ipynb` — cleans `data/raw/DHHNGSP.csv` and writes `data/processed/cleaned_featured_data.csv`.
   2. `Forecasting_Models.ipynb` — trains and tunes the four forecasting models and writes `point_metrics.json` and `model_comparison_plots.png`.
   3. `Volatility_GARCH.ipynb` — fits the GARCH(1,1) model and writes `garch_metrics.json`.
   4. `Final_Comparison_Reflection.ipynb` — loads both JSON files and builds the summary tables used in the report.

## Models covered

| Task | Model(s) |
|---|---|
| Point forecasting (classical) | SARIMA |
| Point forecasting (machine learning) | Random Forest, XGBoost|
| Point forecasting (deep learning) | LSTM  |
| Volatility modelling | GARCH(1,1) on daily returns |

## Notes

- Missing values in the raw series were filled using time-based interpolation.
- Outliers were flagged with the IQR method but kept in the data, since the large spikes are genuine market events rather than data errors.
- Lag features (1, 7 and 30-day), a 7-day rolling mean/standard deviation, and calendar-based indicators (month, quarter, winter flag) were engineered for the tree-based models.
- Full discussion, evidence, and critical reflection are in ``.