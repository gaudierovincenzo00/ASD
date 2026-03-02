import streamlit as st
import time


def login_form(): #Form di login
st.ballons()
    with st.form("login_form"):
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")
        submit = st.form_submit_button("Accedi", type="primary", use_container_width="true")
        