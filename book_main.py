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
