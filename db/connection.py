# db/connection.py
import streamlit as st
import pandas as pd
from supabase import create_client, Client

def get_supabase_client():
    url = st.secrets["supabase"]["url"]
    key = st.secrets["supabase"]["key"]
    return create_client(url, key)

supabase = get_supabase_client()

def carica_anagrafiche(limit=15):
    try:
        # Se passiamo None, carichiamo tutto (rimuovendo il limit)
        query = supabase.table("anagrafiche").select("*")
        if limit:
            query = query.limit(limit)
        
        response = query.execute()
        return pd.DataFrame(response.data)
    except Exception as e:
        st.error(f"Errore caricamento: {e}")
        return pd.DataFrame()
