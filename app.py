import streamlit as st
from book_read import run_book_read_app
from library_location import run_library_location_app
from book_main import run_book_main_app

def main() :
    menu = ['📕 메인화면','📙 도서관 평균 독서율','📒 도서관 정보']

    imge_url0 = 'https://cdn.pixabay.com/photo/2016/06/01/06/26/open-book-1428428_960_720.jpg'
    st.sidebar.image(imge_url0)
    st.sidebar.title(':book: Library Information :book:')
    choice = st.sidebar.selectbox('MENU', menu)

    imge_url1 = 'https://images.pexels.com/photos/1926988/pexels-photo-1926988.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    imge_url2 = 'https://images.pexels.com/photos/3747517/pexels-photo-3747517.jpeg?auto=compress&cs=tinysrgb&w=1600'

    if choice == '📕 메인화면' :
        run_book_main_app()

    elif choice == '📙 도서관 평균 독서율' :
        st.sidebar.image(imge_url1)
        run_book_read_app()
        
    elif choice == '📒 도서관 정보' :
        st.sidebar.image(imge_url2)
        run_library_location_app()

if __name__ == '__main__' :
    main()