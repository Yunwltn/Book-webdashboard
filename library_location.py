import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sb
import altair as alt

def run_library_location_app() :
    st.title('도서관 정보 :mag:')
    image_url = 'https://cdn.pixabay.com/photo/2016/08/29/21/38/peabody-institute-1629259_960_720.jpg'
    st.image(image_url, use_column_width=True)

    df = pd.read_csv('LIBRARY_202211.csv',index_col=0)
    st.subheader('')

    st.subheader('전국 도서관 정보')
    df_count = df['지역'].count()
    fig1 = px.bar(y= df['지역'], height=600, title= '전국 공공 도서관 갯수 (총 ' + str(df_count) + '개)')
    st.plotly_chart(fig1)
    st.dataframe(df[['지역', '도서관명', '주소']])
    
    if st.checkbox('도서관명으로 검색하기') :
        library_name = st.text_input('검색할 도서관명을 입력해주세요')
        library_name = df.loc[ df['도서관명'].str.contains(library_name) ]
        st.dataframe(library_name[['지역', '도서관명', '주소']])
    st.subheader('')

    st.subheader('각 지역별 도서관 정보')
    AREA_choice1 = st.selectbox('지역을 선택하세요', df['지역'].unique())
    df2 = df.loc[ df['지역'] == AREA_choice1 ]
    AREA_choice2 = st.selectbox('세부 지역을 선택하세요', df2['세부지역'].unique())

    AREA_choicedf = df.loc[ (df['지역'] == AREA_choice1) & (df['세부지역'] == AREA_choice2) ]
    st.dataframe(AREA_choicedf[['분류', '지역', '도서관명', '주소']])

    st.map(AREA_choicedf)
    AREAdf = df.loc[ df['지역'] == AREA_choice1 ]
    AREAdf_count = AREAdf['지역'].count()
    fig2 = px.bar(AREAdf, y= '세부지역', height=600, title= AREA_choice1 + '의 공공 도서관 갯수(총 ' + str(AREAdf_count) + '개)')
    st.plotly_chart(fig2)