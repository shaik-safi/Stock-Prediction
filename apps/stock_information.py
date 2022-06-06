import streamlit as st
import numpy as np
import pandas as pd
from data.create_data import create_table
import matplotlib.pyplot as plt
import seaborn as sns
from datetime import datetime , date , timedelta

stock_name_list = ["Apple","Google","Microsoft","Amazon","Tesla","Facebook","Nvidia","Taiwan Semiconductor","Adobe","Accenture","Oracle","Cisco","Intel","Qualcomm","Sony","Infosys","Vmware","Hp","Electronic Arts","Twitter","Lg","Blackberry","Gopro","Jpmorgan","Visa"]
stock_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN','TSLA','FB','NVDA','TSM','ADBE','ACN','ORCL','CSCO','INTC','QCOM','sony','INFY','VMW','HPQ','EA','TWTR','LPL','BB','GPRO','JPM','V']
def app():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title('Stock Information')
    option = st.selectbox('Select Stock',stock_list)
    start = st.date_input("Enter Start Date",date(2019, 7, 6),max_value=datetime.now()- timedelta(days = 1))
    if st.button('Get Info'):
        sns.set_style('whitegrid')
        plt.style.use("fivethirtyeight")

        from pandas_datareader.data import DataReader
        import yfinance as yf
        tech_list = [option]
        end = datetime.now()
        stock = yf.download(option, start, end)
        company_list = [stock]
        company_name = [option]

        for company, com_name in zip(company_list, company_name):
            company["company_name"] = com_name

        df = pd.concat(company_list, axis=0)
        day_range = stock.iloc[stock.shape[0] - 1][1:3]
        # st.write(stock.describe())
        index = stock_list.index(option)
        stock_name = stock_name_list[index]
        st.header(f"{stock_name}")
        st.title(f'''$ {round(stock.iloc[stock.shape[0] - 1]["Adj Close"], 2)}''')
        #Figure 1
        plt.figure(figsize=(15, 6))
        plt.subplots_adjust(top=1.25, bottom=1.2)
        plt.figure(figsize=(15, 6))
        plt.subplots_adjust(top=1.25, bottom=1.2)
        plt.subplot(2, 2, 1)
        stock['Adj Close'].plot(linewidth=1)
        plt.ylabel('Close')
        plt.xlabel(None)
        plt.title(f"Closing Price of {stock_name}")
        st.pyplot()

        col1, col2 = st.columns(2)
        col1.metric("Previous Close", f'${round(stock.iloc[stock.shape[0] - 2]["Adj Close"], 2)}')
        col2.metric("Maximum Close Price", f'${round(stock.describe().iloc[7]["Close"],2)}')

        col1, col2= st.columns(2)
        col1.metric("Day Range", f'${round(day_range["Low"],2)} - ${round(day_range["High"],2)}')
        col2.metric("Year Range", f'${round(stock.describe().iloc[3]["Low"],2)} - ${round(stock.describe().iloc[7]["High"],2)}')
        st.markdown(f"#### Volume traded each day of {stock_name}")
        plt.figure(figsize=(15, 7))
        plt.subplots_adjust(top=1.25, bottom=1.2)
        plt.subplot(2, 2, 1)
        company['Volume'].plot(linewidth=1)
        plt.ylabel('Volume')
        plt.xlabel(None)
        plt.title(f"Sales Volume for {stock_name}")
        st.pyplot()

        st.markdown(f"#### Moving average of {stock_name}")
        ma_day = [10, 20, 50]

        ma_day = [10, 20]

        for ma in ma_day:
            for company in company_list:
                column_name = f"MA for {ma} days"
                company[column_name] = company['Adj Close'].rolling(ma).mean()

        plt.figure(figsize=(15, 7))
        stock[['Adj Close', 'MA for 10 days', 'MA for 20 days']].plot(linewidth=1)
        plt.title(stock_name)
        st.pyplot()

        st.markdown(f"#### Daily return of {stock_name}")
        for company in company_list:
            company['Daily Return'] = company['Adj Close'].pct_change()

        plt.figure(figsize=(15, 7))
        stock[['Daily Return']].plot(legend=True, linewidth=1)
        plt.title(stock_name)
        st.pyplot()

        st.markdown(f"#### Average daily return of {stock_name}")
        plt.figure(figsize=(12, 7))

        plt.subplot(2, 2, 1)
        stock['Daily Return'].hist(bins=50)
        plt.ylabel('Daily Return')
        plt.title(f'{stock_name}')
        st.pyplot()
