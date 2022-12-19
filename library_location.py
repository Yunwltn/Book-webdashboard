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
    df = df.dropna()
    st.subheader('')

    st.subheader('전국 도서관 정보')
    df_count = df['ONE_AREA_NM'].count()
    fig1 = px.bar(y= df['ONE_AREA_NM'], height=600, title= '전국 공공 도서관 갯수 (총 ' + str(df_count) + '개)')
    st.plotly_chart(fig1)
    st.dataframe(df[['ONE_AREA_NM', 'LBRRY_NM', 'LBRRY_ADDR']])
    
    if st.checkbox('도서관명으로 검색하기') :
        library_name = st.text_input('검색할 도서관명을 입력해주세요')
        library_name = df.loc[ df['LBRRY_NM'].str.contains(library_name) ]
        st.dataframe(library_name[['ONE_AREA_NM', 'LBRRY_NM', 'LBRRY_ADDR']])
    st.subheader('')

    st.subheader('각 지역별 도서관 정보')
    AREA_choice1 = st.selectbox('지역을 선택하세요', df['ONE_AREA_NM'].unique())
    df2 = df.loc[ df['ONE_AREA_NM'] == AREA_choice1 ]
    AREA_choice2 = st.selectbox('세부 지역을 선택하세요', df2['TWO_AREA_NM'].unique())

    AREA_choicedf = df.loc[ (df['ONE_AREA_NM'] == AREA_choice1) & (df['TWO_AREA_NM'] == AREA_choice2) ]
    st.dataframe(AREA_choicedf[['LBRRY_TY_NM', 'ONE_AREA_NM', 'LBRRY_NM', 'LBRRY_ADDR']])

    st.map(AREA_choicedf)
    AREAdf = df.loc[ df['ONE_AREA_NM'] == AREA_choice1 ]
    AREAdf_count = AREAdf['ONE_AREA_NM'].count()
    fig2 = px.bar(AREAdf, y= 'TWO_AREA_NM', height=600, title= AREA_choice1 + '의 공공 도서관 갯수(총 ' + str(AREAdf_count) + '개)')
    st.plotly_chart(fig2)