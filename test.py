import streamlit as st
from read import *

path='Data/tkt.csv'

df = read_csv(path)

st.title("This is just a test")

st.write(df)
st.write("save file back to Data folder")
df.to_csv("Data/newfile.csc")

print(df)
