import streamlit as st

st.title("read anagrafica")


from supabase import create_client, Client

# Recupero delle credenziali dai secrets
url: str = st.secrets["supabase"]["url"]
key: str = st.secrets["supabase"]["key"]

# Inizializzazione del client
supabase: Client = create_client(url, key)

# Esempio di query
st.title("Dati da Supabase")
response = supabase.table("data").select("*").execute()

st.write(response.data)
