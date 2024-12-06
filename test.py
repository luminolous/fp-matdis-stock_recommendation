from st_aggrid import AgGrid
import streamlit as st
import pandas as pd

st.title("Tes AgGrid")

# DataFrame contoh
df = pd.DataFrame({
    "Nama": ["A", "B", "C"],
    "Nilai": [90, 80, 70]
})

# Menampilkan tabel dengan AgGrid
AgGrid(df)
