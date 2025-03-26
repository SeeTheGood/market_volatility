# Market Risk Metrics & Portfolio Performance Analytics

This project uses Python to analyze the risk-return profile of major US equities and indices, including volatility, Sharpe ratio, Sortino ratio, M2 ratio, Calmar ratio, and maximum drawdown.

By applying quantitative finance metrics to real historical market data, this notebook explores how traders and analysts assess risk-adjusted performance over time.

---

## 🧠 Key Concepts & Methods

### 📊 Assets Analyzed:
- Individual Stocks: `MSFT`, `AAPL`, `NVDA`, `META`
- Benchmarks: `^GSPC` (S&P 500), `^IXIC` (Nasdaq)

### 🧮 Metrics Computed:
- **Log Returns & Annualized Volatility**
- **Trailing Volatility** (Rolling window)
- **Sharpe Ratio** – Risk-adjusted excess return
- **Sortino Ratio** – Downside-risk-adjusted return
- **M² Ratio** – Sharpe-based performance scaled to benchmark volatility
- **Maximum Drawdown** – Worst peak-to-trough loss
- **Calmar Ratio** – Return-to-drawdown efficiency

---

## 📦 Tools & Libraries
- `yfinance` for data collection
- `NumPy`, `Pandas`, `SciPy` for calculations
- `Plotly` for interactive visualizations
- `pandas_datareader` for alternative sources

---

## 📈 Visualizations

- Histogram plots of log return distributions
- Rolling charts of Sharpe and Sortino ratios over time
- Drawdown and Calmar ratio bar charts for cross-asset comparison
- Interactive volatility timelines

---

## 🤖 Use Cases

This kind of analysis supports:
- **Quantitative risk modeling**
- **Backtesting investment strategies**
- **Performance evaluation across market conditions**
- **Stress testing portfolios or single stocks**

---

## 💬 About This Project

This is part of my journey to join a propreatory trading firm. I’m combining my quant engineering background with passion for options trading with practical Python skills to explore how traders measure and control downside risk.

If you're working in financial engineering, quant research, or risk analytics, I’d love to hear your thoughts.

---

## 📎 File Included:
- `market_risk_metrics.ipynb`: Main analysis notebook

