import streamlit as st
from display import *
def main():
    st.set_page_config(
        page_title='ProPy00 Web Center',
        page_icon='💾',
        Layout='centered',
        initial_sidebar_state='auto'
)     
    TOCW()
    PEND()
if __name__=='__main__':main()