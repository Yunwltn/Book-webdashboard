import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image
import plotly.express as px
import matplotlib.pyplot as plt
import seaborn as sb
import altair as alt

def run_library_location_app() :
    st.title('도서관 정보 :mag:')
    image_url = 'https://cdn.pixabay.com/photo/2017/07/02/09/03/books-2463779_960_720.jpg'
    st.image(image_url, use_column_width=True)

    df = pd.read_csv('LIBRARY_202211.csv',index_col=0)
    st.subheader('')

    st.subheader('전국 도서관 정보')
    st.dataframe(df[['LBRRY_TY_NM', 'ONE_AREA_NM', 'LBRRY_NM', 'LBRRY_ADDR']])
    AREA_choice1 = st.selectbox('지역을 선택하세요', df['ONE_AREA_NM'].unique())
    df2 = df.loc[ df['ONE_AREA_NM'] == AREA_choice1 ]
    AREA_choice2 = st.selectbox('세부 지역을 선택하세요', df2['TWO_AREA_NM'].unique())

    AREA_choicedf = df.loc[ (df['ONE_AREA_NM'] == AREA_choice1) & (df['TWO_AREA_NM'] == AREA_choice2) ]
    st.dataframe(AREA_choicedf[['LBRRY_TY_NM', 'ONE_AREA_NM', 'LBRRY_NM', 'LBRRY_ADDR']])

    