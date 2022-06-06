import streamlit as st
from multiapp import MultiApp
from apps import home,stock_information,comparing_stocks,predict_stock # import your app modules here

app = MultiApp()

app.add_app("Home", home.app)
app.add_app("Stock Information", stock_information.app)
app.add_app("Comparing stocks", comparing_stocks.app)
app.add_app("Forecast stock price", predict_stock.app)

app.run()
