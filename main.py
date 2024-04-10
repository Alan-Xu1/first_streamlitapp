import streamlit as st
import pandas as pd

car_name = st.sidebar.text_input('Car Name')
transmission = st.sidebar.multiselect('Choose the type of transmission', ['Manual','Automatic'], default=['Manual','Automatic'])
selling_price = st.sidebar.slider('Selling price', 0, 20, value=(0,20))
year = st.sidebar.slider('Year', 2000, 2024, value=(2000,2024))
submit = st.sidebar.button('Submit', type='primary')

df = pd.read_csv('car_data.csv')
if submit:
    if car_name == '':
        new_df = df.loc[(df['Transmission'].isin(transmission)) & (df['Selling_Price'] >= selling_price[0]) & 
                        (df['Selling_Price'] <= selling_price[1]) &
                        (df['Year'] >= year[0]) &
                        (df['Year'] <= year[1])]
        st.dataframe(new_df)
    else:
        new_df = df.loc[(df['Car_Name'] == car_name) &
                        (df['Transmission'].isin(transmission)) & (df['Selling_Price'] >= selling_price[0]) & 
                        (df['Selling_Price'] <= selling_price[1]) &
                        (df['Year'] >= year[0]) &
                        (df['Year'] <= year[1])]
        st.dataframe(new_df)