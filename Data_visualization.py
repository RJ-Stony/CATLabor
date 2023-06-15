import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

category = ["업종별", "발생형태별", "연령별", "요양기간별", "근속기간별"]
add_selectbox = st.sidebar.selectbox("어떤 데이터를 원하시나요?", category)

def plot(df):
    ilist = df["산업중분류별(2)"].unique().tolist()
    industries = st.multiselect("업종을 선택해주세요!", ilist[1:])
    st.subheader("{}을 선택해주셨네요.".format(", ".join(industries)))
    idx = df.index[(df["산업중분류별(2)"] == industries[0])]
    st.write(idx)
    st.write(list(df.loc[[idx], :]))
    
    '''chart_data = pd.DataFrame(
        np.random.randn(20, 3),
        columns=['2017', '2018', '2019', '2020', '2021'])

    st.line_chart(chart_data)'''

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
    
