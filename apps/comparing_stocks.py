import streamlit as st
import numpy as np
import pandas as pd
from pandas_datareader import data as pdr
import yfinance as yfin
from data.create_data import create_table
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime, date,timedelta

def app():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title('Comparing Stock')
    stock_name_list = ["Apple","Google","Microsoft","Amazon","Tesla","Facebook","Nvidia","Taiwan Semiconductor","Adobe","Accenture","Oracle","Cisco","Intel","Qualcomm","Sony","Infosys","Vmware","Hp","Electronic Arts","Twitter","Lg","Blackberry","Gopro","Jpmorgan","Visa"]
    stock_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN','TSLA','FB','NVDA','TSM','ADBE','ACN','ORCL','CSCO','INTC','QCOM','sony','INFY','VMW','HPQ','EA','TWTR','LPL','BB','GPRO','JPM','V']
    option1 = st.selectbox('Select Stock 1',stock_list)
    option2 = st.selectbox('Select Stock 2',stock_list)
    start = st.date_input("Enter Start Date",date(2019, 7, 6),max_value=datetime.now()- timedelta(days = 1))
    index1 = stock_list.index(option1)
    index2 = stock_list.index(option2)
    if st.button('Compare'):
        end = datetime.now()
        yfin.pdr_override()
        closing_df = pdr.get_data_yahoo(stock_list, start, end)['Adj Close']
        tech_rets = closing_df.pct_change()
        st.markdown(f"### {stock_name_list[index1]} vs {stock_name_list[index2]}")
        if option1 == option2:
            sns.jointplot(x=option1, y=option1, data=tech_rets, kind='scatter', color='seagreen')
        else:
            sns.jointplot(x=option1, y=option2, data=tech_rets, kind='scatter')
        st.pyplot()
