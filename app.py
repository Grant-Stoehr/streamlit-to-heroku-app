import streamlit as st
import time
import numpy as np
import pandas as pd

df = pd.read_csv("WakeCountyHousing.csv")
#df['Date'] = pd.to_datetime(df['Date'])
#df.set_index(df.Date, inplace=True)

def categorise(row):  
    if row['Year_Built'] == row['Year_Remodeled']:
        return "NO"
    else:
        return "YES"
    
df['Is_Remodeled'] = df.apply(lambda row: categorise(row), axis=1)
#print(df.head())


st.subheader('Sale Prices')
st.write(df.head())
#Bar Chart
display_df = df[:10]
st.bar_chart(display_df["Total_Sale_Price"])



if "count" not in st.session_state:
    st.session_state.count = 0


text = st.text(str(st.session_state.count))


if st.button('Say hello'):
    st.session_state.count += 1


your_city = st.text_input("Enter your city name")
st.title(your_city)


#if result:
#    st.write(result)
#    new_df = get_price_arount_date(st.session_state.chart)
#    st.line_chart(new_df)
