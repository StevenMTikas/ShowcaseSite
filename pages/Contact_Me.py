import streamlit as st
from send_email import send_email

st.header('Contact Me')

with st.form(key='contact_me_form'):
    user_email = st.text_input('Enter your e-mail address:')
    raw_message = st.text_area('Enter your message here:')
    user_message = f'''\
Subject: New e-mail from {user_email}

From: {user_email}
{raw_message}
'''
    button = st.form_submit_button('Submit')
    if button:
        send_email(user_message)
        st.info('Your e-mail was sent successfully')