import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from book_read import run_book_read_app
from library_location import run_library_location_app
from book_main import run_book_main_app

def main() :
    menu = ['📕 메인화면','📙 도서관 평균 독서량','📒 도서관 정보']

    imge_url0 = 'https://cdn.pixabay.com/photo/2016/06/01/06/26/open-book-1428428_960_720.jpg'
    st.sidebar.image(imge_url0)
    st.sidebar.title(':book: Library Information :book:')
    choice = st.sidebar.selectbox('MENU', menu)
    st.sidebar.write('')

    st.sidebar.write('도서관 회원수')
    st.sidebar.write('')
    
    df = pd.read_csv('READ_QY_2020.csv',index_col=0)

    AREA_df = df.groupby('연령')['회원수'].sum().to_frame()
    st.sidebar.bar_chart(AREA_df)

    library_input = st.sidebar.text_input('간편 도서관명으로 주소 검색하기')
    df = pd.read_csv('LIBRARY_202211.csv',index_col=0)
    df = df.loc[ df['도서관명'].str.contains(library_input, case=False) ]
    st.sidebar.dataframe(df[['도서관명','주소']])
    st.sidebar.info('도서관 정보를 더 보고싶다면 상단의 도서관 정보를 클릭해주세요 :mag:')

    if choice == '📕 메인화면' :
        run_book_main_app()

    elif choice == '📙 도서관 평균 독서량' :
        run_book_read_app()
        
    elif choice == '📒 도서관 정보' :
        run_library_location_app()

if __name__ == '__main__' :
    main()