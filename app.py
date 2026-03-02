import streamlit as st
import time

st.cache_data.clear()     # per cache_data
st.cache_resource.clear() # per cache_resource



###############################################################################
# 1. Inizializza lo stato di login una volta sola
###############################################################################
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
    st.session_state.user = None     # salva chi si è autenticato

if "ruolo" not in st.session_state:
    st.session_state.ruolo = "Ospite"
    st.session_state.user = None     # salva chi si è autenticato


def app_run():
    caption("Created with love by [AWI](https://www.agenziawebitalia.com)")
    page.run()



#app_run()
if st.session_state.logged_in:
    app_run()
else:
    login_form()
