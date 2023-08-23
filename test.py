import streamlit as st
from read import *

path='tkt.csv'

df = read_csv(path)

st.title("This is just a test")

st.write(df)

print(df)
