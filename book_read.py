import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sb

def run_book_read_app() :
    st.title('우리나라 도서관 평균 독서량 :books:')
    st.write('국립중앙도서관의 연간 독서량 파일을 활용하여')
    st.write('우리나라 평균 독서량을 월별, 연령대별, 지역별로 분석했습니다')
    st.info('2020년도의 월, 지역, 연령, 성별, 회원수, 대출건수, 독서량 컬럼을 사용했습니다')
    image_url = 'https://cdn.pixabay.com/photo/2017/07/02/09/03/books-2463779_960_720.jpg'
    st.image(image_url, use_column_width=True)

    df = pd.read_csv('READ_QY_2020.csv',index_col=0)
    st.subheader('')

    status = st.radio('평균 독서량', ['월별 평균','연령대별 평균'])

    if status == '월별 평균' :
        st.subheader('월별 독서량 평균')
        MONTH = df.groupby('월')['독서량'].mean().to_frame()
        max_MONTH = MONTH.loc[ MONTH['독서량'] == MONTH['독서량'].max() ].index.tolist()[0]
        st.info('평균 독서율이 제일 높은 월은 ' + str(max_MONTH) + '월 입니다')
        st.bar_chart(MONTH, height=600)

    elif status == '연령대별 평균' :
        st.subheader('연령대별 독서량 평균')
        AGE = df.groupby('연령')['독서량'].mean().to_frame()
        max_AGE = AGE.loc[ AGE['독서량'] == AGE['독서량'].max() ].index.tolist()[0]
        st.info('평균 독서율이 제일 높은 연령대는 ' + max_AGE + '입니다')
        st.bar_chart(AGE, height=600)

    if st.checkbox('월별 연령대 평균량 알아보기') :
        my_choice = st.selectbox('월을 선택하세요', df['월'].unique())
        if my_choice != 0 :
            MONTH_AGE = df[['월','연령', '독서량']]
            choice_Month = MONTH_AGE.loc[ MONTH_AGE['월'] == my_choice ]
            choice_Month = choice_Month.groupby('연령')['독서량'].mean().to_frame()
        
            fig1 = px.bar(choice_Month, y='독서량', height=600, title= str(my_choice)+ '월 연령대별 평균 독서량', color='독서량', color_continuous_scale='plotly3')
            st.plotly_chart(fig1)
    st.subheader('')

    st.subheader('전국 연령대별 회원수와 대출건수')
    
    AREA_AGEdf = df.groupby('연령')[['회원수','대출건수']].sum()
    AREA_AGEdf = AREA_AGEdf.reset_index()
    fig2 = px.bar(AREA_AGEdf, x= '연령', y=['회원수','대출건수'], barmode='group', height=600, color_continuous_scale='plotly3')
    st.plotly_chart(fig2)
    st.dataframe(AREA_AGEdf)
    st.subheader('')

    st.subheader('지역별 정보')
    status = st.radio('지역별로 정보 보기', ['지역별 평균 독서량','지역별 회원수','지역별 대출건수'])

    if status == '지역별 평균 독서량' :
        AREA_READQY = df.groupby('지역')['독서량'].mean().to_frame()

        AREA_READQY = AREA_READQY.reset_index()
        max_AREA_READQY = AREA_READQY.loc[ AREA_READQY['독서량'] == AREA_READQY['독서량'].max() ]
        st.info('평균 독서량이 가장 높은 지역은 ' + max_AREA_READQY['지역'].tolist()[0] + '입니다')
        fig3 = px.bar(AREA_READQY, y='독서량', height=600, title= '지역별 평균 독서량', color='독서량', color_continuous_scale='plotly3')
        st.plotly_chart(fig3)

    elif status == '지역별 회원수' :
        AREA_LON = df.groupby('지역')['회원수'].sum().to_frame().reset_index()

        max_AREA_LON = AREA_LON.loc[ AREA_LON['회원수'] == AREA_LON['회원수'].max() ]
        st.info('회원수가 가장 많은 지역은 ' + max_AREA_LON['지역'].tolist()[0] + '입니다')
        fig4 = px.pie(AREA_LON, '지역', '회원수', title='지역별 회원수', hole=.3)
        st.plotly_chart(fig4)

    elif status == '지역별 대출건수' :
        AREA_LONMBER = df.groupby('지역')['대출건수'].sum().to_frame().reset_index()

        max_AREA_LONMBER = AREA_LONMBER.loc[ AREA_LONMBER['대출건수'] == AREA_LONMBER['대출건수'].max() ]
        st.info('대출건수가 가장 많은 지역은 ' + max_AREA_LONMBER['지역'].tolist()[0] + '입니다')
        fig5 = px.pie(AREA_LONMBER, '지역', '대출건수', title='지역별 대출건수', hole=.3)
        st.plotly_chart(fig5)

    if st.checkbox('각 지역별 세부 데이터 보기') :
        my_choice = st.selectbox('지역을 선택하세요', df['지역'].unique())
        if my_choice != 0 :
            df2 = df[['지역','연령','회원수','대출건수']]
            df2 = df2.loc[ df2['지역'] == my_choice ]
            st.info(my_choice + '의 총 회원 수는' + str(df2['회원수'].sum()) + '명 입니다')
            st.dataframe(df2.groupby('연령')[['회원수','대출건수']].sum())



