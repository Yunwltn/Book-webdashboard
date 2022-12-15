import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def run_bookcafe_stor_app() :
    st.title('책읽기 좋은 북카페 찾기☕️')
    image_url = 'https://images.pexels.com/photos/2383122/pexels-photo-2383122.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    st.image(image_url, use_column_width=True)

    df = pd.read_csv('data/bookcafe_stor.csv', index_col=0)
    st.subheader('')
    st.subheader('단어 검색해서 찾기')
    Search = st.radio('분류 선택', ['카페명 검색','주소 검색','카페소개 검색'])  
    sentence = st.text_input('검색할 단어를 입력하세요')

    if len(sentence) == 0 :
        st.write('')

    elif Search == '카페명 검색' :
        st.info('카페명으로 검색된 결과입니다')
        my_Search = df.loc[ df['FCLTY_NM'].str.contains(sentence) ]
        st.dataframe(my_Search.iloc[: ,[8,0,1,3,6,7]])

    elif Search == '주소 검색' :
        st.info('주소명으로 검색된 결과입니다')
        my_Search = df.loc[ df['FCLTY_ROAD_NM_ADDR'].str.contains(sentence) ]
        st.dataframe(my_Search.iloc[: ,[8,0,1,3,6,7]])

    elif Search == '카페소개 검색' :
        st.info('카페 소개로 검색된 결과입니다')
        my_Search = df.loc[ df['OPTN_DC'].str.contains(sentence) ]
        st.dataframe(my_Search.iloc[: ,[8,0,1,3,6,7]])
    st.subheader('')
    st.subheader('지역 선택해서 찾기')
    AREA_df = df['AREA'].value_counts().to_frame().reset_index()
    AREA_list = AREA_df['index'].to_list()
    my_choice = st.selectbox('지역을 선택하세요', AREA_list)
    
    if len(my_choice) != 0 :
        choice_AREA = df.loc[ df['AREA'] == my_choice ]
        st.dataframe(choice_AREA.iloc[: ,[8,0,1,3,6,7]])
        
        map_df = df[['lat', 'lon', 'AREA']]
        map_df = map_df.loc[map_df['AREA'] == my_choice ]
        st.map(map_df)
