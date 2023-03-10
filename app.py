import streamlit as st
import pandas as pd
import numpy as np
from book_read import run_book_read_app
from library_location import run_library_location_app
from book_main import run_book_main_app

def main() :
    menu = ['π λ©μΈνλ©΄','π λμκ΄ νκ·  λμλ','π λμκ΄ μ λ³΄']

    # μ¬μ΄λλ° μ΄λ―Έμ§, λ©λ΄
    imge_url0 = 'https://cdn.pixabay.com/photo/2016/06/01/06/26/open-book-1428428_960_720.jpg'
    st.sidebar.image(imge_url0)
    st.sidebar.title(':book: Library Information :book:')
    choice = st.sidebar.selectbox('MENU', menu)
    st.sidebar.write('')

    # μ¬μ΄λλ° μ κ΅­ λμκ΄ μ°λ Ήλ³ νμμ μ°¨νΈ
    st.sidebar.write('μ κ΅­ λμκ΄ μ°λ Ήλ³ νμμ')
    df = pd.read_csv('READ_QY_2020.csv',index_col=0)
    Members_age = df.groupby('μ°λ Ή')['νμμ'].sum().to_frame()
    st.sidebar.bar_chart(Members_age)

    # λμκ΄λͺμΌλ‘ μ£Όμ κ²μ κΈ°λ₯
    library_input = st.sidebar.text_input('κ°νΈ λμκ΄λͺμΌλ‘ μ£Όμ κ²μνκΈ°')
    df = pd.read_csv('LIBRARY_202211.csv',index_col=0)
    df = df.loc[ df['λμκ΄λͺ'].str.contains(library_input, case=False) ]
    st.sidebar.dataframe(df[['λμκ΄λͺ','μ£Όμ']])
    st.sidebar.info('λμκ΄ μ λ³΄λ₯Ό λ λ³΄κ³ μΆλ€λ©΄ μλ¨μ λμκ΄ μ λ³΄λ₯Ό ν΄λ¦­ν΄μ£ΌμΈμ :mag:')

    if choice == 'π λ©μΈνλ©΄' :
        run_book_main_app()

    elif choice == 'π λμκ΄ νκ·  λμλ' :
        run_book_read_app()
        
    elif choice == 'π λμκ΄ μ λ³΄' :
        run_library_location_app()

if __name__ == '__main__' :
    main()