import streamlit as st
from book_read import run_book_read_app
from book_proposal import run_book_proposal_app
from bookcafe_stor import run_bookcafe_stor_app

def main() :
    menu = ['평균 독서율📌 ','북카페 검색☕️','책 검색📚']

    choice = st.sidebar.selectbox('메뉴', menu)
    imge_url1 = 'https://images.pexels.com/photos/3268388/pexels-photo-3268388.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    imge_url2 = 'https://images.pexels.com/photos/1926988/pexels-photo-1926988.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    imge_url3 = 'https://images.pexels.com/photos/4068029/pexels-photo-4068029.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'


    if choice == '평균 독서율📌 ' :
        st.sidebar.image(imge_url1)
        run_book_read_app()

    elif choice == '책 검색📚' :
        st.sidebar.image(imge_url2)
        run_book_proposal_app()

    elif choice == '북카페 검색☕️' :
        st.sidebar.image(imge_url3)
        run_bookcafe_stor_app()

if __name__ == '__main__' :
    main()