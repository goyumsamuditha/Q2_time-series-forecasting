import numpy as np
from sklearn.metrics import mean_absolute_error, mean_squared_error

def get_metrics(y_true, y_pred):
    """Calculates and returns standard time series forecasting metrics."""
    mae = mean_absolute_error(y_true, y_pred)
    rmse = np.sqrt(mean_squared_error(y_true, y_pred))
    mape = np.mean(np.abs((y_true - y_pred) / y_true)) * 100
    return {
        "MAE": mae,
        "RMSE": rmse,
        "MAPE": mape
    }
    
def create_lstm_sequence(data, timesteps = 30):
   """Transforms a 1D array into sliding window sequences for an LSTM."""
   X, y = [], []
   for i in range(len(data) - timesteps):
       X.append(data[i:(i + timesteps)])
       y.append(data[i + timesteps])
   return np.array(X), np.array(y)