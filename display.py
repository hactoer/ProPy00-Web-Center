import streamlit as st
def PEND():# proenterprise name display
    st.markdown(
        '''
        <style>
        .custom-title{
            position: relatively;
            top: 10px;
            left: 500px;
            font-size: 24px;
            font-weight: bold;
            color: blue;
            background-color: rgba(255,255,255,0.8);
            padding: 5px 10px;
            border-radius: 5px;
            display: inline-block;
        }
        @media (prefers-color-scheme: light) {
            .custom-title {
                background-color: rgba(0,0,0,0.8);
            }
        }
        </style>
        ''',
        unsafe_allow_html=True
    )
    st.markdown('<div class="custom-title">ProgrammerPython00</div>',unsafe_allow_html=True)
def TOCW():#table of contents web
    st.write('**目錄**')
    st.markdown('---')
    st.markdown('<a href="https://pdf-compress-programmerpython00-mvuzreq28l3eoxt8yue6dla.streamlit.app" target="_blank">[PDF 壓縮器]</a>'
                ,unsafe_allow_html=True)
def SF():#Search Function
    with open('searchstyle.css') as f:
        st.markdown(f'<style>{f.read()}</style>',unsafe_allow_html=True)
        ...
