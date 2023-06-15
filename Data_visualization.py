import streamlit as st
import pandas as pd

df = pd.read_csv("by_age_group(17~21).csv", encoding='cp949')

if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(df)
