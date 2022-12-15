import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def run_book_proposal_app() :
<<<<<<< HEAD
    st.title('책 검색📚')
    image_url = 'https://images.pexels.com/photos/2041540/pexels-photo-2041540.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
=======
    st.title('책 추천')
    image_url = 'https://images.pexels.com/photos/1392854/pexels-photo-1392854.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
>>>>>>> parent of aa6c9b2 (add)
    st.image(image_url, use_column_width=True)

    df = pd.read_csv('data/book_proposal.csv', index_col=0)
    st.subheader('')
    st.subheader('단어 검색해서 찾기')
    Search = st.radio('분류 선택', ['제목 검색','저자 검색','출판사 검색', '줄거리 검색', '발행년도 검색'])  
    sentence = st.text_input('검색할 단어를 입력하세요')

    if len(sentence) == 0 :
        st.write('')

    elif Search == '제목 검색' :
        st.info('책 제목으로 검색된 결과입니다')
        my_Search = df.loc[ df['TITLE'].str.contains(sentence) ]
        my_Search = my_Search.reset_index()
        st.dataframe(my_Search.iloc[: , 2:7])

    elif Search == '저자 검색' :
        st.info('책 저자로 검색된 결과입니다')
        my_Search = df.loc[ df['AUTHR'].str.contains(sentence) ]
        my_Search = my_Search.reset_index()
        st.dataframe(my_Search.iloc[: , 2:7])

    elif Search == '출판사 검색' :
        st.info('책 출판사로 검색된 결과입니다')
        my_Search = df.loc[ df['PUBLISHER'].str.contains(sentence) ]
        my_Search = my_Search.reset_index()
        st.dataframe(my_Search.iloc[: , 2:7])

    elif Search == '줄거리 검색' :
        st.info('책 줄거리로 검색된 결과입니다')
        my_Search = df.loc[ df['BOOK_INTRCN'].str.contains(sentence) ]
        my_Search = my_Search.reset_index()
        st.dataframe(my_Search.iloc[: , 2:7])

    elif Search == '발행년도 검색' :
        st.info('책 발행년도로 검색된 결과입니다')
        my_Search = df.loc[ df['YEAR'].str.contains(sentence) ]
        my_Search = my_Search.reset_index()
        st.dataframe(my_Search.iloc[: , 2:7])

    st.subheader('')
    st.subheader('연령대별 인기순위보기')
   
    AGE_df = df['AGE'].value_counts().to_frame().reset_index()
    AGE_list = AGE_df['index'].to_list()
    AGE_list.sort()
    my_choice = st.selectbox('연령을 선택하세요', AGE_list)

    if len(my_choice) != 0 :
        choice_AREA = df.loc[ df['AGE'] == my_choice ]
        choice_AREA = choice_AREA.reset_index()
        st.dataframe(choice_AREA.iloc[: , 2:7])

