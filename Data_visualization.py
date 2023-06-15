import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

category = ["업종별", "발생형태별", "연령별", "요양기간별", "근속기간별"]
add_selectbox = st.sidebar.selectbox("어떤 데이터를 원하시나요?", category)

def plot(df):
    ilist = df["산업중분류별(2)"].unique().tolist()
    industries = st.multiselect("업종을 선택해주세요!", ilist[1:])
    st.header("You selected: {}".format(", ".join(industries)))

    '''dfs = {country: df[df["country"] == country] for country in countries}

    fig = go.Figure()
    for country, df in dfs.items():
        fig = fig.add_trace(go.Scatter(x=df["year"], y=df["gdpPercap"], name=country))

    st.plotly_chart(fig)'''

if add_selectbox == "업종별":
    df = pd.read_csv("by_industry(17~21).csv", encoding='cp949')
    if st.checkbox('원데이터 살펴보기'):
        st.subheader('Raw Data')
        st.write(df)
    plot(df)

elif add_selectbox == "발생형태별":
    df = pd.read_csv("by_type_of_occurrence(17~21).csv", encoding='cp949')
    if st.checkbox('원데이터 살펴보기'):
        st.subheader('Raw Data')
        st.write(df)
        
elif add_selectbox == "연령별":
    df = pd.read_csv("by_age_group(17~21).csv", encoding='cp949')
    if st.checkbox('원데이터 살펴보기'):
        st.subheader('Raw Data')
        st.write(df)
        
elif add_selectbox == "요양기간별":
    df = pd.read_csv("by_period_of_care(17~21).csv", encoding='cp949')
    if st.checkbox('원데이터 살펴보기'):
        st.subheader('Raw Data')
        st.write(df)
        
elif add_selectbox == "근속기간별":
    df = pd.read_csv("by_length_of_employment(17~21).csv", encoding='cp949')
    if st.checkbox('원데이터 살펴보기'):
        st.subheader('Raw Data')
        st.write(df)
    
# Using "with" notation
with st.sidebar:
    add_radio = st.radio(
        "Choose a shipping method",
        ("Standard (5-15 days)", "Express (2-5 days)")
    )
    
