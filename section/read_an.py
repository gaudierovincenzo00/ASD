import streamlit as st
import pandas as pd
from db.connection import carica_anagrafiche

# 1. Inizializziamo lo stato del limite se non esiste
if 'limit_righe' not in st.session_state:
    st.session_state.limit_righe = 20

def mostra_dati():
    st.title("Visualizza anagrafiche")
    st.caption("Tabella di visualizzazione delle anagrafiche inserite")

    # 2. Carichiamo i dati in base allo stato attuale
    df = carica_anagrafiche(st.session_state.limit_righe)
    
    # 3. Visualizzazione
    st.dataframe(df, use_container_width=True, hide_index=True)

    if st.button(f"Mostra tutte", use_container_width=True, icon=":material/view_list:"):
        st.session_state.limit_righe = None # Rimuove il limite
        st.rerun()

mostra_dati()