import streamlit as st
from send_email import send_email
import pandas as pd

st.header('Contact Us')

with st.form(key='contact_me_form'):
    df = pd.read_csv('main_company/topics.csv')
    user_email = st.text_input('Enter your e-mail address:')
    user_topic = st.selectbox(label='Choose a topic', 
                             options=(df['topic']), 
                             index=None, key='topic')
    raw_message = st.text_area('Enter your message here:')
    user_message = f'''\
Subject: New e-mail from {user_email}

From: {user_email}
Topic: {user_topic}
{raw_message}
'''
    button = st.form_submit_button('Submit')
    if button:
        send_email(user_message)
        st.info('Your e-mail was sent successfully')