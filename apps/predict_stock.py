import streamlit as st
import numpy as np
import pandas as pd
from data.create_data import create_table
import matplotlib.pyplot as plt
import seaborn as sns
from pandas_datareader import data as pdr
from datetime import datetime , date , timedelta
from sklearn.preprocessing import MinMaxScaler

def app():
    st.set_option('deprecation.showPyplotGlobalUse', False)
    st.title('Forecast stock price')
    stock_name_list = ["Apple","Google","Microsoft","Amazon","Tesla","Facebook","Nvidia","Taiwan Semiconductor","Adobe","Accenture","Oracle","Cisco","Intel","Qualcomm","Sony","Infosys","Vmware","Hp","Electronic Arts","Twitter","Lg","Blackberry","Gopro","Jpmorgan","Visa"]
    stock_list = ['AAPL', 'GOOG', 'MSFT', 'AMZN','TSLA','FB','NVDA','TSM','ADBE','ACN','ORCL','CSCO','INTC','QCOM','sony','INFY','VMW','HPQ','EA','TWTR','LPL','BB','GPRO','JPM','V']
    option = st.selectbox('Select Stock',stock_list)
    start = st.date_input("Enter Start Date",date(2021, 5, 31),max_value=datetime.now()- timedelta(days = 365))
    if st.button('Forecast'):
        index = stock_list.index(option)
        df = pdr.get_data_yahoo(option, start, end=datetime.now())
        st.markdown(f"###  {stock_name_list[index]} Dataset")
        st.write(df)
        st.markdown("###  Close Price History")
        plt.figure(figsize=(16,6))
        plt.title('Close Price History')
        plt.plot(df['Close'])
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close Price USD ($)', fontsize=18)
        plt.show()
        st.pyplot()

        # Create a new dataframe with only the 'Close column
        data = df.filter(['Close'])
        # Convert the dataframe to a numpy array
        dataset = data.values
        # Get the number of rows to train the model on
        training_data_len = int(np.ceil( len(dataset) * .95 ))

        # Scale the data
        from sklearn.preprocessing import MinMaxScaler

        scaler = MinMaxScaler(feature_range=(0,1))
        scaled_data = scaler.fit_transform(dataset)

        # Create the training data set
        # Create the scaled training data set
        train_data = scaled_data[0:int(training_data_len), :]
        # Split the data into x_train and y_train data sets
        x_train = []
        y_train = []

        for i in range(60, len(train_data)):
            x_train.append(train_data[i-60:i, 0])
            y_train.append(train_data[i, 0])
            if i<= 61:
                print(x_train)
                print(y_train)
                print()

        # Convert the x_train and y_train to numpy arrays
        x_train, y_train = np.array(x_train), np.array(y_train)

        # Reshape the data
        x_train = np.reshape(x_train, (x_train.shape[0], x_train.shape[1], 1))
        # x_train.shape

        from keras.models import Sequential
        from keras.layers import Dense, LSTM
        print(x_train.shape)
        # Build the LSTM model
        model = Sequential()
        model.add(LSTM(128, return_sequences=True, input_shape= (x_train.shape[1], 1)))
        model.add(LSTM(64, return_sequences=False))
        model.add(Dense(25))
        model.add(Dense(1))

        # Compile the model
        model.compile(optimizer='adam', loss='mean_squared_error')

        # Train the model
        model.fit(x_train, y_train, batch_size=1, epochs=10)
        #print(model.summary())

        # Create the testing data set
        # Create a new array containing scaled values from index 1543 to 2002
        test_data = scaled_data[training_data_len - 60: , :]
        # Create the data sets x_test and y_test
        x_test = []
        y_test = dataset[training_data_len:, :]
        for i in range(60, len(test_data)):
            x_test.append(test_data[i-60:i, 0])

        # Convert the data to a numpy array
        x_test = np.array(x_test)

        # Reshape the data
        x_test = np.reshape(x_test, (x_test.shape[0], x_test.shape[1], 1 ))

        # Get the models predicted price values
        predictions = model.predict(x_test)
        predictions = scaler.inverse_transform(predictions)

        # Get the root mean squared error (RMSE)
        rmse = np.sqrt(np.mean(((predictions - y_test) ** 2)))

        st.markdown("###  Predicted Close Price")
        # Plot the data
        train = data[:training_data_len]
        valid = data[training_data_len:]
        valid['Predictions'] = predictions
        # Visualize the data
        plt.figure(figsize=(16,6))
        plt.title('Model')
        plt.xlabel('Date', fontsize=18)
        plt.ylabel('Close Price USD ($)', fontsize=18)
        plt.plot(train['Close'])
        plt.plot(valid[['Close', 'Predictions']])
        plt.legend(['Train', 'Val', 'Predictions'], loc='upper left')
        plt.show()
        st.pyplot()

        st.write(valid)
