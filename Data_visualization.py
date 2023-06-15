import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
import numpy as np

category = ["업종별", "발생형태별", "연령별", "요양기간별", "근속기간별"]
add_selectbox = st.sidebar.selectbox("어떤 데이터를 원하시나요?", category)

def plot_by_industry(df):
    ilist = df["산업중분류별(2)"].unique().tolist()
    industries = st.selectbox("업종을 선택해주세요!", ilist[1:])
    st.subheader("{}을 선택해주셨네요.".format(industries))
    idx = df.index[(df["산업중분류별(2)"] == industries)]

    data1 = {'2017': df.loc[idx, '2017.4'].values.tolist()[0],
                  '2018': df.loc[idx, '2018.4'].values.tolist()[0],
                  '2019': df.loc[idx, '2019.4'].values.tolist()[0],
                  '2020': df.loc[idx, '2020.4'].values.tolist()[0],
                  '2021': df.loc[idx, '2021.4'].values.tolist()[0]}
    
    occur_data = pd.DataFrame.from_dict(data=data1, orient='index', columns=['요양재해율 (%)'])
    occur_data = occur_data.replace('-', 0)
    occur_data = occur_data.astype(float, errors='ignore')
    st.line_chart(occur_data)
    
    data2 = {'2017': df.loc[idx, ['2017', '2017.1', '2017.2', '2017.3']].values.tolist()[0],
            '2018': df.loc[idx, ['2018', '2018.1', '2018.2', '2018.3']].values.tolist()[0],
            '2019': df.loc[idx, ['2019', '2019.1', '2019.2', '2019.3']].values.tolist()[0],
            '2020': df.loc[idx, ['2020', '2020.1', '2020.2', '2020.3']].values.tolist()[0],
            '2021': df.loc[idx, ['2021', '2021.1', '2021.2', '2021.3']].values.tolist()[0]}
    
    chart_data = pd.DataFrame.from_dict(data=data2, orient='index', columns=['사업장 수', '근로자 수', '요양재해자 수', '사망자 수'])
    chart_data = chart_data.replace('-', 0)
    chart_data = chart_data.astype(int, errors='ignore')
    st.line_chart(chart_data)
    
def plot_by_age(df):
    ilist = [x for x in df["산업중분류별(2)"].unique().tolist() if x != '소계']
    industries = st.selectbox("업종을 선택해주세요!", ilist[1:])
    st.subheader("{}을 선택해주셨네요.".format(industries))
    idx = df.index[(df["산업중분류별(2)"] == industries)]

    data1 = {'2017': df.loc[idx, '2017'].values.tolist()[0],
            '2018': df.loc[idx, '2018'].values.tolist()[0],
            '2019': df.loc[idx, '2019'].values.tolist()[0],
            '2020': df.loc[idx, '2020'].values.tolist()[0],
            '2021': df.loc[idx, '2021'].values.tolist()[0]}
    
    total_data = pd.DataFrame.from_dict(data=data1, orient='index',
                                        columns=['합계'])
    total_data = total_data.replace('-', 0)
    total_data = total_data.astype(int, errors='ignore')
    st.line_chart(total_data)
    
    data2 = {'2017': df.loc[idx, ['2017.1', '2017.2', '2017.3', '2017.4', '2017.5', '2017.6', '2017.7', '2017.8', '2017.9', '2017.10']].values.tolist()[0],
            '2018': df.loc[idx, ['2018.1', '2018.2', '2018.3', '2018.4', '2018.5', '2018.6', '2018.7', '2018.8', '2018.9', '2018.10']].values.tolist()[0],
            '2019': df.loc[idx, ['2019.1', '2019.2', '2019.3', '2019.4', '2019.5', '2019.6', '2019.7', '2019.8', '2019.9', '2019.10']].values.tolist()[0],
            '2020': df.loc[idx, ['2020.1', '2020.2', '2020.3', '2020.4', '2020.5', '2020.6', '2020.7', '2020.8', '2020.9', '2020.10']].values.tolist()[0],
            '2021': df.loc[idx, ['2021.1', '2021.2', '2021.3', '2021.4', '2021.5', '2021.6', '2021.7', '2021.8', '2021.9', '2021.10']].values.tolist()[0]}
    
    chart_data = pd.DataFrame.from_dict(data=data2, orient='index',
                                        columns=['18세 미만', '18~24세', '25~29세', '30~34세', '35~39세', '40~44세', '45~49세', '50~54세', '55~59세', '60세 이상'])
    chart_data = chart_data.replace('-', 0)
    chart_data = chart_data.astype(int, errors='ignore')
    st.line_chart(chart_data)

if add_selectbox == "업종별":
    df = pd.read_csv("by_industry(17~21).csv", encoding='cp949')
    if st.checkbox('원데이터 살펴보기'):
        st.subheader('Raw Data')
        st.write(df)
    plot_by_industry(df)

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
    plot_by_age(df)
        
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
    
