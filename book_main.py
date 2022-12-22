import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def run_book_main_app() :
    st.title('Library Information')
    st.write('환영합니다 Library Information 는 도서관의 평균 독서량을 월별, 연령대별, 지역별로 분석하고')
    st.write('전국에 위치한 도서관의 갯수와 각 지역별 위치를 검색할 수 있는 앱입니다')
    image_url = 'https://cdn.pixabay.com/photo/2013/02/16/20/16/cornell-university-82344_960_720.jpg'
    st.image(image_url, use_column_width=True)
    st.write('')
    
    if st.button('사용한 데이터 프레임 정보 보기 :mag:') :
        READ_df = pd.read_csv('READ_QY_2020.csv',index_col=0)
        LIBRARY_df = pd.read_csv('LIBRARY_202211.csv',index_col=0)

        st.write('국립중앙도서관 연간 독서량(2020)')
        st.dataframe(READ_df)
        st.write('')

        st.write('국립중앙도서관 도서관 정보(202211)')
        st.dataframe(LIBRARY_df)