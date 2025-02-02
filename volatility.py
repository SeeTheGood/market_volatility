import datetime as dt 
import pandas as pd 
import numpy as np
import pandas_datareader as pdr
import sys
import yfinance as yf


from pandas_datareader import data as pdr
import plotly.offline as pyo 
import plotly.graph_objs as go
from plotly.subplots import make_subplots
import datetime as dt
import datetime as dt
pd.options.plotting.backend = "plotly"

# Correct stock tickers (NASDAQ -> ^IXIC, S&P500 -> ^GSPC)

# Define start and end dates
start = "2024-08-01"  # Example start date
end = dt.datetime.today().strftime('%Y-%m-%d')  # Set end to today's date
tickers = ['MSFT', 'AAPL', 'NVDA', 'META', '^IXIC', '^GSPC']

# Download stock data
df = yf.download(tickers, start=start, end=end)

# Show Close prices
print(df['Close'].head())

log_returns = np.log(df['Close'] / df['Close'].shift(1)).dropna()
log_returns

#Compute log returns 
daily_std= log_returns.std()
daily_std
annual_std = daily_std * np.sqrt(252)
annual_std*100

# Plot the data

fig= make_subplots(rows=3, cols=3)

fig.update_layout(autosize=False, width=800, height=800, title='Frequency of Log Returns',
         xaxis1 = {"title": "AAPL Annualised Vol: " + str(np.round(annual_std['AAPL'] * 100, 1))},
         xaxis2 = {"title": "META Annulaised Vol:" + str(np.round(annual_std['META']* 100,1))},
         xaxis3 = {"title": "MSFT Annualised Vol: " + str(np.round(annual_std['MSFT'] * 100, 1))},
         xaxis4 = {"title": "NVDA Annualised Vol: " + str(np.round(annual_std['NVDA'] * 100, 1))},
         xaxis5 = {"title": "S&P500 Annualised Vol: " + str(np.round(annual_std['^GSPC'] * 100, 1))},
         xaxis6 = {"title": "NASDAQ Annualised Vol: " + str(np.round(annual_std['^IXIC'] * 100, 1))}
)


fig.show()

# Trailing volatility over time 

# +
print(log_returns.tail())  # Check if log_returns has data

Trading_days = 120
volatility = log_returns.rolling(window=Trading_days).std() * np.sqrt(Trading_days)
volatility.plot().update_layout (autosize=False, width=600, height=600, title='Trailing Volatility over time')
volatility = volatility*100
volatility = volatility.dropna()


# Sharpe Ratio

# the Sharpe Ratio is a measure of risk-adjusted return. It is calculated as the ratio of the excess return of the investment to the standard deviation of the investment. The higher the Sharpe Ratio, the better the investment's return relative to its risk.

Rf=0.01/252
sharpe_ratio = (log_returns.rolling(window = Trading_days).mean() - Rf) * Trading_days/volatility
sharpe_ratio.plot().update_layout(autosize=False, width=600, height=600, title='Sharpe Ratio over time')
sharpe_ratio = sharpe_ratio.dropna()
print (sharpe_ratio)



# sortino ratio

# The Sortino Ratio is a measure of risk-adjusted return. It is calculated as the ratio of the excess return of the investment to the downside deviation of the investment. The higher the Sortino Ratio, the better the investment's return relative to its risk.

sortino_vol = (log_returns[log_returns<0].rolling(window = Trading_days,center = True, min_periods=10 ).mean() - Rf) * Trading_days/volatility[log_returns < 0]
sortino_ratio = (log_returns.rolling(window = Trading_days).mean() - Rf) * Trading_days/sortino_vol
sortino_ratio.plot().update_layout(autosize=False, width=800, height=800, title='Sortino Ratio over time')

m2_ratio = pd.DataFrame()
benchmark_vol = log_returns['^GSPC']
for c in log_returns.columns:
    if c!='^GSPC':
        m2_ratio[c] = (sharpe_ratio[c] * benchmark_vol/Trading_days +Rf)*Trading_days
m2_ratio.plot().update_layout(autosize=False, width=800, height=800, title='M2 Ratio over time')

# +
#Maximum Drawdown
#The Maximum Drawdown is the maximum loss from a peak to a trough of a portfolio, before a new peak is attained. It is a measure of downside risk. The lower the Maximum Drawdown, the better the investment's return relative to its risk.

def max_drawdown(returns):
    cum_returns = (returns + 1).cumprod()
    peak = cum_returns.expanding(min_periods =1).max()
    drawdown = (cum_returns/peak) - 1
    return drawdown.min()
returns =df.Close.pct_change().dropna()
max_drawdowns = returns. apply(max_drawdown, axis=0)
max_drawdowns*100 
# -

#Calmar Ratio
calmars =np.exp(log_returns.mean()*252)/abs(max_drawdowns)
calmars.plot.bar().update_layout(autosize=False, width=800, height=800, title='Calmar Ratio over time')



