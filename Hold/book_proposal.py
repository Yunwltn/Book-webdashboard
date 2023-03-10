import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def run_book_proposal_app() :
    st.title('μ± κ²μπ')
    image_url = 'https://images.pexels.com/photos/2041540/pexels-photo-2041540.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    st.image(image_url, use_column_width=True)

    df = pd.read_csv('data/book_proposal.csv', index_col=0)
    st.subheader('')
    st.subheader('λ¨μ΄ κ²μν΄μ μ°ΎκΈ°')
    Search = st.radio('λΆλ₯ μ ν', ['μ λͺ© κ²μ','μ μ κ²μ','μΆνμ¬ κ²μ', 'μ€κ±°λ¦¬ κ²μ', 'λ°νλλ κ²μ'])  
    sentence = st.text_input('κ²μν  λ¨μ΄λ₯Ό μλ ₯νμΈμ')

    if len(sentence) == 0 :
        st.write('')

    elif Search == 'μ λͺ© κ²μ' :
        st.info('μ± μ λͺ©μΌλ‘ κ²μλ κ²°κ³Όμλλ€')
        my_Search = df.loc[ df['TITLE'].str.contains(sentence) ]
        my_Search = my_Search.reset_index()
        st.dataframe(my_Search.iloc[: , 2:7])

    elif Search == 'μ μ κ²μ' :
        st.info('μ± μ μλ‘ κ²μλ κ²°κ³Όμλλ€')
        my_Search = df.loc[ df['AUTHR'].str.contains(sentence) ]
        my_Search = my_Search.reset_index()
        st.dataframe(my_Search.iloc[: , 2:7])

    elif Search == 'μΆνμ¬ κ²μ' :
        st.info('μ± μΆνμ¬λ‘ κ²μλ κ²°κ³Όμλλ€')
        my_Search = df.loc[ df['PUBLISHER'].str.contains(sentence) ]
        my_Search = my_Search.reset_index()
        st.dataframe(my_Search.iloc[: , 2:7])

    elif Search == 'μ€κ±°λ¦¬ κ²μ' :
        st.info('μ± μ€κ±°λ¦¬λ‘ κ²μλ κ²°κ³Όμλλ€')
        my_Search = df.loc[ df['BOOK_INTRCN'].str.contains(sentence) ]
        my_Search = my_Search.reset_index()
        st.dataframe(my_Search.iloc[: , 2:7])

    elif Search == 'λ°νλλ κ²μ' :
        st.info('μ± λ°νλλλ‘ κ²μλ κ²°κ³Όμλλ€')
        my_Search = df.loc[ df['YEAR'].str.contains(sentence) ]
        my_Search = my_Search.reset_index()
        st.dataframe(my_Search.iloc[: , 2:7])

    st.subheader('')
    st.subheader('μ°λ Ήλλ³ μΈκΈ°μμλ³΄κΈ°')
   
    AGE_df = df['AGE'].value_counts().to_frame().reset_index()
    AGE_list = AGE_df['index'].to_list()
    AGE_list.sort()
    my_choice = st.selectbox('μ°λ Ήμ μ ννμΈμ', AGE_list)

    if len(my_choice) != 0 :
        choice_AREA = df.loc[ df['AGE'] == my_choice ]
        choice_AREA = choice_AREA.reset_index()
        st.dataframe(choice_AREA.iloc[: , 2:7])

        

