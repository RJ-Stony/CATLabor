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
    st.subheader("{}을 선택해주셨네요!".format(industries))
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
    st.subheader("{}을 선택해주셨네요!".format(industries))
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

def plot_by_type_of_occurrence(df):
    ilist = [x for x in df["산업중분류별(2)"].unique().tolist() if x != '소계']
    industries = st.selectbox("업종을 선택해주세요!", ilist[1:])
    st.subheader("{}을 선택해주셨네요!".format(industries))
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
    
    data2 = {'2017': df.loc[idx, ['2017.1', '2017.2', '2017.3', '2017.4', '2017.5', '2017.6', '2017.7', '2017.8', '2017.9', '2017.10', '2017.11', '2017.12', '2017.13',
                                  '2017.14', '2017.15', '2017.16', '2017.17', '2017.18', '2017.19', '2017.20', '2017.21', '2017.22', '2017.23', '2017.24']].values.tolist()[0],
            '2018': df.loc[idx, ['2018.1', '2018.2', '2018.3', '2018.4', '2018.5', '2018.6', '2018.7', '2018.8', '2018.9', '2018.10', '2018.11', '2018.12', '2018.13',
                                  '2018.14', '2018.15', '2018.16', '2018.17', '2018.18', '2018.19', '2018.20', '2018.21', '2018.22', '2018.23', '2018.24']].values.tolist()[0],
            '2019': df.loc[idx, ['2019.1', '2019.2', '2019.3', '2019.4', '2019.5', '2019.6', '2019.7', '2019.8', '2019.9', '2019.10', '2019.11', '2019.12', '2019.13',
                                  '2019.14', '2019.15', '2019.16', '2019.17', '2019.18', '2019.19', '2019.20', '2019.21', '2019.22', '2019.23', '2019.24']].values.tolist()[0],
            '2020': df.loc[idx, ['2020.1', '2020.2', '2020.3', '2020.4', '2020.5', '2020.6', '2020.7', '2020.8', '2020.9', '2020.10', '2020.11', '2020.12', '2020.13',
                                  '2020.15', '2020.16', '2020.17', '2020.18', '2020.19', '2020.20', '2020.21', '2020.22', '2020.23', '2020.24', '2020.25']].values.tolist()[0],
            '2021': df.loc[idx, ['2021.1', '2021.2', '2021.3', '2021.4', '2021.5', '2021.6', '2021.7', '2021.8', '2021.9', '2021.10', '2021.11', '2021.12', '2021.13',
                                  '2021.14', '2021.15', '2021.16', '2021.17', '2021.18', '2021.19', '2021.20', '2021.21', '2021.22', '2021.23', '2021.24']].values.tolist()[0]}
    
    chart_data = pd.DataFrame.from_dict(data=data2, orient='index',
                                        columns=['떨어짐', '넘어짐', '부딪힘', '물체에 맞음', '무너짐', '끼임', '절단·베임·찔림', '감전', '폭발·파열', '화재', '깔림·뒤집힘', '이상온도 물체접촉',
                                                 '빠짐·익사', '불균형 및 무리한 동작', '화학물질 누출·접촉', '산소결핍', '사업장내 교통사고', '사업장외 교통사고', '업무상질병', '체육행사 등의 사고',
                                                 '폭력행위', '동물상해', '기타', '분류불능'])
    chart_data = chart_data.replace('-', 0)
    chart_data = chart_data.astype(int, errors='ignore')
    st.line_chart(chart_data)
    
def plot_by_period_of_care(df):
    ilist = [x for x in df["산업중분류별(2)"].unique().tolist() if x != '소계']
    industries = st.selectbox("업종을 선택해주세요!", ilist[1:])
    st.subheader("{}을 선택해주셨네요!".format(industries))
    idx = df.index[(df["산업중분류별(2)"] == industries)]

    data1 = {'2017': df.loc[idx, '2017'].values.tolist()[0],
            '2018': df.loc[idx, '2018'].values.tolist()[0],
            '2019': df.loc[idx, '2019'].values.tolist()[0],
            '2020': df.loc[idx, '2020'].values.tolist()[0],
            '2021': df.loc[idx, '2021'].values.tolist()[0]}
    
    total_data = pd.DataFrame.from_dict(data=data1, orient='index',
                                        columns=['요양재해자 수'])
    total_data = total_data.replace('-', 0)
    total_data = total_data.astype(int, errors='ignore')
    st.line_chart(total_data)
    
    data2 = {'2017': df.loc[idx, ['2017.2', '2017.3', '2017.4', '2017.5', '2017.6', '2017.7']].values.tolist()[0],
            '2018': df.loc[idx, ['2018.2', '2018.3', '2018.4', '2018.5', '2018.6', '2018.7']].values.tolist()[0],
            '2019': df.loc[idx, ['2019.2', '2019.3', '2019.4', '2019.5', '2019.6', '2019.7']].values.tolist()[0],
            '2020': df.loc[idx, ['2020.2', '2020.3', '2020.4', '2020.5', '2020.6', '2020.7']].values.tolist()[0],
            '2021': df.loc[idx, ['2021.2', '2021.3', '2021.4', '2021.5', '2021.6', '2021.7']].values.tolist()[0]}
    
    chart_data = pd.DataFrame.from_dict(data=data2, orient='index',
                                        columns=['6개월 이상', '91~180일', '29~90일', '15~28일', '8~14일', '4~7일'])
    chart_data = chart_data.replace('-', 0)
    chart_data = chart_data.astype(int, errors='ignore')
    st.line_chart(chart_data)
    
def plot_by_length_of_employment(df):
    ilist = [x for x in df["산업중분류별(2)"].unique().tolist() if x != '소계']
    industries = st.selectbox("업종을 선택해주세요!", ilist[1:])
    st.subheader("{}을 선택해주셨네요!".format(industries))
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
    
    data2 = {'2017': df.loc[idx, ['2017.1', '2017.2', '2017.3', '2017.4', '2017.5', '2017.6', '2017.7', '2017.8', '2017.9']].values.tolist()[0],
            '2018': df.loc[idx, ['2018.1', '2018.2', '2018.3', '2018.4', '2018.5', '2018.6', '2018.7', '2018.8', '2018.9']].values.tolist()[0],
            '2019': df.loc[idx, ['2019.1', '2019.2', '2019.3', '2019.4', '2019.5', '2019.6', '2019.7', '2019.8', '2019.9']].values.tolist()[0],
            '2020': df.loc[idx, ['2020.1', '2020.2', '2020.3', '2020.4', '2020.5', '2020.6', '2020.7', '2020.8', '2020.9']].values.tolist()[0],
            '2021': df.loc[idx, ['2021.1', '2021.2', '2021.3', '2021.4', '2021.5', '2021.6', '2021.7', '2021.8', '2021.9']].values.tolist()[0]}
    
    chart_data = pd.DataFrame.from_dict(data=data2, orient='index',
                                        columns=['6개월 미만', '6개월~1년 미만', '1~2년 미만', '2~3년 미만', '3~4년 미만', '4~5년 미만', '5~10년 미만', '10년 이상', '분류불능'])
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
    plot_by_type_of_occurrence(df)
        
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
    plot_by_period_of_care(df)
        
elif add_selectbox == "근속기간별":
    df = pd.read_csv("by_length_of_employment(17~21).csv", encoding='cp949')
    if st.checkbox('원데이터 살펴보기'):
        st.subheader('Raw Data')
        st.write(df)
    plot_by_length_of_employment(df)
    
