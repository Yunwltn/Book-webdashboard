import streamlit as st
import pandas as pd
import numpy as np
from PIL import Image

def run_book_read_app() :
    st.title('우리나라 평균 독서율📌 ')
    image_url = 'https://images.pexels.com/photos/289737/pexels-photo-289737.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    st.image(image_url, use_column_width=True)

    df = pd.read_csv('data/red book_2020.csv')
    st.subheader('')
    st.subheader('올해 평균 독서율')
    status = st.radio('독서율', ['월별 독서율','연령별 독서율'])
    
    if status == '월별 독서율' :
        Month_READ_RT = df.groupby('Month')['READ_RT'].mean()
        st.bar_chart(Month_READ_RT)

        AGE_mean = df.groupby('AGE')['READ_RT'].mean().to_frame().reset_index()
        st.info('평균 독서율이 제일 높은 월은 1월이고, 낮은 월은 3월입니다')
        
    elif status == '연령별 독서율' :
        AGE_READ_RT = df.groupby('AGE')['READ_RT'].mean()
        st.bar_chart(AGE_READ_RT)
        st.info('평균 독서율이 제일 높은 연령대는 유아(6-7)대이고, 낮은 연령대는 20대입니다')

    st.subheader('')
    st.subheader('월별 연령대 독서율')
    my_choice = st.selectbox('월을 선택하세요', df['Month'].unique())
    
    if my_choice != 0 :
        Month_AGE = pd.pivot_table(df, index= ['Month','AGE'], aggfunc= np.mean, values=['READ_RT']).reset_index()
        choice_Month = Month_AGE.loc[ Month_AGE['Month'] == my_choice ]
        choice_Month = choice_Month.set_index('AGE')
        st.bar_chart(choice_Month['READ_RT'])

    video_file = open('')
    st.video(video_file)