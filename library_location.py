import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px

def run_library_location_app() :
    st.title('도서관 정보 :mag:')

    st.write('국립중앙도서관의 전국 공공도서관의 정보 파일을 활용하여')
    st.write('전국에 위치한 도서관의 갯수와 각 지역별 위치를 분리하여 검색할 수 있게 만들었습니다')
    st.info('2022년도의 전국 공공 도서관 정보를 사용했습니다')
    
    image_url = 'https://cdn.pixabay.com/photo/2016/08/29/21/38/peabody-institute-1629259_960_720.jpg'
    st.image(image_url, use_column_width=True)

    df = pd.read_csv('LIBRARY_202211.csv',index_col=0)
    st.dataframe(df)
    st.subheader('')

    # 지역별 도서관 갯수 차트와 전국 도서관 데이터프레임
    st.subheader('전국 도서관 정보')

    # 차트 타이틀에 사용할 도서관 총 갯수
    area_count = df['지역'].count()

    df_area_count = df['지역'].value_counts()
    df_area_count = df_area_count.to_frame().reset_index()
    fig1 = px.bar(x= df_area_count['index'], y=df_area_count['지역'], height=600, title= '전국 공공 도서관 갯수 (총 ' + str(area_count) + '개)')
    st.plotly_chart(fig1)
    st.dataframe(df[['지역', '도서관명', '주소']])
    
    # 체크박스 클릭시 도서관명으로 주소 검색 기능
    if st.checkbox('도서관명으로 검색하기:mag:') :
        library_name = st.text_input('검색할 도서관명을 입력해주세요')
        library_name = df.loc[ df['도서관명'].str.contains(library_name) ]
        st.dataframe(library_name[['지역', '도서관명', '주소']])
    st.subheader('')

    # 지역과 세부지역을 선택하면 해당 지역의 데이터 프레임과 지도가 나오게 하기
    st.subheader('각 지역별 도서관 정보')

    AREA_choice1 = st.selectbox('지역을 선택하세요', df['지역'].unique())
    choice1_df = df.loc[ df['지역'] == AREA_choice1 ]

    AREA_choice2 = st.selectbox('세부 지역을 선택하세요', choice1_df['세부지역'].unique())

    choice = df.loc[ (df['지역'] == AREA_choice1) & (df['세부지역'] == AREA_choice2) ]
    st.dataframe(choice[['분류', '지역', '도서관명', '주소']])
    st.map(choice)

    # 선택한 지역의 세부지역별 총 도서관 갯수 차트
    select_AREA = df.loc[ df['지역'] == AREA_choice1 ]

    # 차트 타이틀에 사용할 도서관 총 갯수
    select_AREA_count = select_AREA['지역'].count()

    select_AREA = select_AREA['세부지역'].value_counts()
    select_AREA = select_AREA.to_frame().reset_index()

    fig2 = px.bar(y= select_AREA['index'], x=select_AREA['세부지역'], height=600, title= AREA_choice1 + '의 공공 도서관 갯수(총 ' + str(select_AREA_count) + '개)')
    fig2.update_layout(yaxis = dict(autorange='reversed'))
    st.plotly_chart(fig2)