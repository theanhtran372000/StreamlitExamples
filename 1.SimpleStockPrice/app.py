import yfinance as yf
import streamlit as st
import pandas as pd

st.write("""
# Simple Stock Proce App

Shown are the stock closing price and the volumn of Apple!

| Syntax | Description |
| - | - |
| Header | Title |
| Paragraph | Text |    
""")

# Define the ticker syymbol
tickerSymbol = 'AAPL'

# Get data from this ticker
tickerData = yf.Ticker(tickerSymbol)

# Get historical prices for this ticker
tickerDf = tickerData.history(period='id', start='2010-5-20', end='2022-5-20')

# Columns: Open     High    Low     Close    Dividends      Stock Splits


st.write("""
## Closing price         
""")
st.line_chart(tickerDf.Close)

st.write("""
## Volumn
""")
st.line_chart(tickerDf.Volume)