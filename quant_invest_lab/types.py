from typing import Literal

Timeframe = Literal[
    "1min",
    "3min",
    "5min",
    "15min",
    "30min",
    "1hour",
    "2hour",
    "4hour",
    "12hour",
    "1day",
]

PortfolioMetric = Literal[
    "Expected return",
    "Expected volatility",
    "Skewness",
    "Kurtosis",
    "VaR",
    "CVaR",
    "Max drawdown",
    "Kelly criterion",
    "Sharpe ratio",
    "Sortino ratio",
    "Burke ratio",
    "Calmar ratio",
    "Tail ratio",
    "Specific risk",
    "Systematic risk",
    "Portfolio beta",
    "Portfolio alpha",
    "Jensen alpha",
    "R2",
    "Tracking error",
    "Treynor ratio",
    "Information ratio",
]
