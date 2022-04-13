import streamlit as st
import time
import numpy as np
import pandas as pd
import sqlite3
from sqlite3 import Error


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


st.subheader('Enter your name')
your_name = st.text_input("")
st.title(your_name)

conn = sqlite3.connect('app.sqlite')
cur = conn.cursor()
cur.execute("CREATE TABLE IF NOT EXISTS comments (comment varChar(350))")
conn.close()

#Create a text area
st.subheader('Give us some feedback!')
comment = st.text_area("")
#push the comment to a db witht he press of a streamlit button
if st.button('Submit'):
    conn = sqlite3.connect('app.sqlite')
    cur = conn.cursor()
    cur.execute("INSERT INTO comments VALUES (?)", (comment,))
    conn.commit()
    conn.close()
    

st.subheader('Comments')
conn = sqlite3.connect('app.sqlite')
cur = conn.cursor()
cur.execute("SELECT * FROM comments")
comments = cur.fetchall()
conn.close()
st.table(comments)


#if result:
#    st.write(result)
#    new_df = get_price_arount_date(st.session_state.chart)
#    st.line_chart(new_df)

