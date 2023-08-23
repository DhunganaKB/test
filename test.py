import streamlit as st
from read import *
import yagmail
from email.message import EmailMessage
import smtplib

path='Data/tkt.csv'

df = read_csv(path)

st.title("This is just a test")

st.write(df)
st.write("save file back to Data folder")
try:
  df.to_csv("Data/newfile.csv")
except:
  st.write("sending file back is failed")

import tempfile
import pathlib
temp_dir = tempfile.TemporaryDirectory()
st.write(temp_dir.name)
uploaded_file_name = "newfile.csv"
uploaded_file_path = pathlib.Path(temp_dir.name) / uploaded_file_name
st.write(uploaded_file_path)

with open(uploaded_file_path, 'wb') as output_temporary_file:
    df.to_csv(output_temporary_file)

## Reading the file from temporary folder
dk = pd.read_csv(uploaded_file_path)
st.write("reading from the temporary file")
st.write(dk)

question = st.text_input("Do you want to get an email now?")

if question:
  msg = EmailMessage()
  contacts = ['kbdhunga@mtu.edu']
  msg['Subject'] = 'Invitation'
  msg['From'] = 'dhunganain23@gmail.com'
  msg['To'] = ', '.join(contacts)
  
  msg.set_content('''\n Hi Kamal,\n Hope this email find you well. We would like to invite you tomorrow at my daughter's birthday at 4.30 pm at our place. Hope you can make it.
  \n
  Thanks\n
  \n''')
  
  with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
      smtp.login('dhunganain23@gmail.com', 'dbszoxlqycoidmyi')
      smtp.send_message(msg)
