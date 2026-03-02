import streamlit as st
import time

st.cache_data.clear()     # per cache_data
st.cache_resource.clear() # per cache_resource

def page():
    read_an = st.Page("section/read_an.py", title="Tutte le anagrafiche", icon=":material/person:")
    add_an = st.Page("section/add_an.py", title="Aggiugni Anagrafica", icon=":material/person_add:")

    page = st.navigation(
        {
            "Anagrafiche": [read_an, add_an],
        }
    )
    page.run()

def sidebar():
    st.sidebar.caption("Benvenuto Admin")
    st.sidebar.caption("Created with love by [AWI](https://www.agenziawebitalia.com)")

def app():
    page()
    sidebar()

app()

