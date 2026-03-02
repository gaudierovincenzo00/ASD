import streamlit as st
import time
from query.utenti import read_user

def login_form(): #Form di login

    # 1. Carica tutti gli utenti in memoria
    users_list = read_user()
    users = {u[1]: (u[2], u[3]) for u in users_list}

    def verify_password(username: str, password: str):
        if username in users and users[username][0] == password:
            return users[username][1]  # ritorna ruolo
        return None

    with st.form("login_form"):
        st.title("Login")
        username = st.text_input("Username")
        password = st.text_input("Password", type="password")

        # Every form must have a submit button.
        submit = st.form_submit_button("Accedi", type="primary", use_container_width="true")
        if submit:
            ruolo = verify_password(username, password)
            if ruolo:
                st.session_state.logged_in = True
                st.session_state.user = username
                st.session_state.ruolo = ruolo
                st.success(f"Benvenuto, {username}! Ruolo: {ruolo}")
                st.balloons()
                time.sleep(2)
                st.rerun()
            else:
                st.error("Credenziali non valide")