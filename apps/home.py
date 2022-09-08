import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table

def app():
    st.title('Visualization and Forecasting of Stocks using Historical Data')
    st.image('https://images.unsplash.com/photo-1590283603385-17ffb3a7f29f?ixlib=rb-1.2.1&ixid=MnwxMjA3fDB8MHxwaG90by1wYWdlfHx8fGVufDB8fHx8&auto=format&fit=crop&w=2070&q=80')
    st.header('About Projet:')
    st.write('''
    The stock market has an air of unpredictability about it. A stock market, also known as an equity market or a share market, is a collection of buyers and sellers (a loose network of economic transactions, not a physical facility or discrete entity) of stocks (also known as shares), which represent ownership claims on businesses; these may include securities listed on a public stock exchange as well as private stock. Shares of private enterprises are sold to investors through equity crowdfunding platforms as an example of the latter. Shares of common stock, as well as other asset kinds such as corporate bonds and convertible bonds, are traded on stock exchanges.
    Small individual stock investors to huge institutional investors, which can be headquartered anywhere in the world and include banks, insurance firms, pension funds, and hedge funds, all participate in the stock market. A stock exchange trader may execute their buy or sell orders on their behalf.
    ''')
    st.header('Problem Definition:')
    st.write('''Today's financial investors have a trading dilemma since they don't know which stocks to buy or which stocks to sell in order to maximize profits.
    Predicting long term value of the stock is relatively easy than predicting on day-to-day basis as the stocks fluctuate rapidly every hour based on world events.
    ''')
    st.header('Project By')
    st.write("Name: N SHAIK SAFI")
    st.write("Github: https://github.com/shaik-safi")
    st.write("LinkedIn: https://www.linkedin.com/in/shaik-safi-1353831b3/")
