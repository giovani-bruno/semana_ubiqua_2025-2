import streamlit as st
from os import listdir

def main():
    paginas = [
        st.Page("Sobre.py", title="👨‍💻 Sobre"),
        st.Page("Davi.py", title="🤖 Davi")
        ]

    pg = st.navigation(paginas, position='hidden')
    
    pg.run()

def barra_navegacao():
    st.sidebar.page_link("Sobre.py")
    st.sidebar.page_link("Davi.py")

if __name__ == "__main__":
    main()