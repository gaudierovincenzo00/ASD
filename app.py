import streamlit as st
import time

st.cache_data.clear()     # per cache_data
st.cache_resource.clear() # per cache_resource

def app_run():
    add_anagrafica = st.Page("add_anagrafica.py", title="Aggiugni Anagrafica", icon=":material/person_add:")
    read_anagrafica = st.Page("read_anagrafica.py", title="Leggi Anagrafica", icon=":material/person_add:")
    page = st.navigation(
        {
            "Anagrafica": [add_anagrafica, read_anagrafica],
        }
    )
    page.run()
    st.balloons()
    st.title("hello, welcome!")
    
app_run()
