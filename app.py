import streamlit as st
import time

st.cache_data.clear()     # per cache_data
st.cache_resource.clear() # per cache_resource

def app_run()
    add_anagrafica = st.Page("/add_anagrafica.py", title="Aggiugni Anagrafica", icon=":material/person_add:")
    st.balloons()
    st.title("hello, welcome!")

app_run()
