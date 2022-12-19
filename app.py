import streamlit as st
from book_read import run_book_read_app
from library_location import run_library_location_app

def main() :
    menu = ['도서관 평균 독서율📚','도서관 정보🔍 ','']

    choice = st.sidebar.selectbox('메뉴', menu)    
    imge_url2 = 'https://images.pexels.com/photos/3747517/pexels-photo-3747517.jpeg?auto=compress&cs=tinysrgb&w=1600'
    imge_url1 = 'https://images.pexels.com/photos/1926988/pexels-photo-1926988.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=1'
    imge_url3 = ''

    if choice == '도서관 평균 독서율📚' :
        st.sidebar.image(imge_url1)
        run_book_read_app()
        

    elif choice == '도서관 정보🔍 ' :
        st.sidebar.image(imge_url2)
        run_library_location_app()

    elif choice == '' :
        st.sidebar.image(imge_url3)
        pass

if __name__ == '__main__' :
    main()