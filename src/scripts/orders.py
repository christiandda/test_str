import streamlit as st
import os
from pathlib import Path

from streamlit_option_menu import option_menu


PROJECT_ROOT = os.path.abspath(os.path.join(
                  os.path.dirname(__file__), 
                  os.pardir)
)
scripts_folder = (PROJECT_ROOT + "/" + "scripts")
files_folder = (scripts_folder + "/" + "files")




def insert_oders():
    #Add the cover image for the cover page. Used a little trick to center the image
             # To display the header text using css style

    st.title('**We add orders**')
    st.markdown(""" <style> .font {
        font-size:40px ; font-family: 'Cooper Black'; color: #FF9633;} 
        </style> """, unsafe_allow_html=True)
    st.write("We add orders and get a return about which driver will do it")



