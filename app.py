import streamlit as st
from book_read import run_book_read_app
from book_proposal import run_book_proposal_app
from bookcafe_stor import run_bookcafe_stor_app

def main() :
<<<<<<< HEAD
    menu = ['평균 독서율📌 ','북카페 검색☕️','책 검색📚']
=======
    menu = ['우리나라 평균 독서율','책 추천','북카페 찾기']
>>>>>>> parent of aa6c9b2 (add)
    choice = st.sidebar.selectbox('메뉴', menu)
    imge_url1 = 'https://images.pexels.com/photos/4068029/pexels-photo-4068029.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    imge_url2 = 'https://images.pexels.com/photos/3599208/pexels-photo-3599208.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'


    if choice == '평균 독서율📌 ' :
        st.sidebar.image(imge_url1)
        run_book_read_app()

<<<<<<< HEAD
    elif choice == '책 검색📚' :
        st.sidebar.image(imge_url2)
        run_book_proposal_app()

    elif choice == '북카페 검색☕️' :
        st.sidebar.image(imge_url3)
=======
    elif choice == '책 추천' :
        run_book_proposal_app()

    elif choice == '북카페 찾기' :
        st.sidebar.image(imge_url2)
>>>>>>> parent of aa6c9b2 (add)
        run_bookcafe_stor_app()

if __name__ == '__main__' :
    main()