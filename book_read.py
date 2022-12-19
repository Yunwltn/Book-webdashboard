import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sb
import altair as alt

def run_book_read_app() :
    st.title('우리나라 도서관 평균 독서량 :books:')
    image_url = 'https://cdn.pixabay.com/photo/2017/07/02/09/03/books-2463779_960_720.jpg'
    st.image(image_url, use_column_width=True)

    df = pd.read_csv('READ_QY_2020.csv',index_col=0)
    st.subheader('')

    st.subheader('월별 평균')
    MONTH = df.groupby('MONTH')['READ_QY'].mean()
    st.bar_chart(MONTH, height=600)
    MONTH = MONTH.to_frame()
    max_MONTH = MONTH.loc[ MONTH['READ_QY'] == MONTH['READ_QY'].max() ].index.tolist()[0]
    st.info('평균 독서율이 제일 높은 월은 ' + str(max_MONTH) + '월 입니다')
    st.subheader('')

    st.subheader('연령대별 평균')
    AGE = df.groupby('AGE')['READ_QY'].mean()
    st.bar_chart(AGE, height=600)
    AGE = AGE.to_frame()
    max_AGE = AGE.loc[ AGE['READ_QY'] == AGE['READ_QY'].max() ].index.tolist()[0]
    st.info('평균 독서율이 제일 높은 연령대는 ' + max_AGE + '입니다')

    if st.checkbox('월별 연령대 평균량 알아보기') :
        my_choice = st.selectbox('월을 선택하세요', df['MONTH'].unique())
        if my_choice != 0 :
            MONTH_AGE = df[['MONTH','AGE', 'READ_QY']]
            choice_Month = MONTH_AGE.loc[ MONTH_AGE['MONTH'] == my_choice ]
            choice_Month = choice_Month.groupby('AGE')['READ_QY'].mean().to_frame()
        
            fig1 = px.bar(choice_Month, y='READ_QY', height=600, title= str(my_choice)+ '월 연령대별 평균 독서량')
            st.plotly_chart(fig1)
    st.subheader('')

    st.subheader('전국 연령대별 회원수와 대출건수')
    AREA_AGEdf = df.groupby('AGE')[['LON_CO','LON_MBER_CO']].sum()
    st.dataframe(AREA_AGEdf)
    if st.checkbox('차트로 보기') :
        AREA_AGEdf = AREA_AGEdf.reset_index()
        fig2 = px.bar(AREA_AGEdf, x= 'AGE', y=['LON_CO','LON_MBER_CO'], barmode='group', height=600, title= '전국 연령대별 회원수와 대출건수')
        st.plotly_chart(fig2)

    st.subheader('지역별 정보')
    status = st.radio('지역별로 정보 보기', ['지역별 평균 독서량','지역별 회원수','지역별 대출건수'])

    if status == '지역별 평균 독서량' :
        AREA_READQY = df.groupby('AREA')['READ_QY'].mean().to_frame()

        fig3 = px.bar(AREA_READQY, y='READ_QY', height=600, title= '지역별 평균 독서량')
        st.plotly_chart(fig3)
        AREA_READQY = AREA_READQY.reset_index()
        max_AREA_READQY = AREA_READQY.loc[ AREA_READQY['READ_QY'] == AREA_READQY['READ_QY'].max() ]
        st.info('평균 독서량이 가장 높은 지역은 ' + max_AREA_READQY['AREA'].tolist()[0] + '입니다')

    elif status == '지역별 회원수' :
        AREA_LON = df.groupby('AREA')['LON_CO'].sum().to_frame().reset_index()

        fig4 = px.pie(AREA_LON, 'AREA', 'LON_CO', title='지역별 회원수', hole=.3, )
        st.plotly_chart(fig4)
        max_AREA_LON = AREA_LON.loc[ AREA_LON['LON_CO'] == AREA_LON['LON_CO'].max() ]
        st.info('회원수가 가장 많은 지역은 ' + max_AREA_LON['AREA'].tolist()[0] + '입니다')

    elif status == '지역별 대출건수' :
        AREA_LONMBER = df.groupby('AREA')['LON_MBER_CO'].sum().to_frame().reset_index()

        fig5 = px.pie(AREA_LONMBER, 'AREA', 'LON_MBER_CO', title='지역별 대출건수', hole=.3)
        st.plotly_chart(fig5)
        max_AREA_LONMBER = AREA_LONMBER.loc[ AREA_LONMBER['LON_MBER_CO'] == AREA_LONMBER['LON_MBER_CO'].max() ]
        st.info('대출건수가 가장 많은 지역은 ' + max_AREA_LONMBER['AREA'].tolist()[0] + '입니다')

    if st.checkbox('각 지역별 세부 데이터 보기') :
        my_choice = st.selectbox('지역을 선택하세요', df['AREA'].unique())
        if my_choice != 0 :
            df2 = df[['AREA','AGE','LON_CO','LON_MBER_CO']]
            df2 = df2.loc[ df2['AREA'] == my_choice ]
            st.dataframe(df2.groupby('AGE')[['LON_CO','LON_MBER_CO']].sum())
    st.subheader('')

    st.subheader('상관분석')
    st.dataframe(df.corr())
    chart = alt.Chart(df).mark_circle().encode(x= 'LON_MBER_CO', y= 'LON_CO', color ='READ_QY')
    st.altair_chart(chart)



