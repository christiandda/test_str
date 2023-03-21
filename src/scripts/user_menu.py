import streamlit as st
from streamlit_option_menu import option_menu
from scripts import orders


session = st.session_state
def delete_login_info():
    del st.session_state['login']
    del st.session_state['username']
    st.success("Logout successful")
    st.experimental_set_query_params(logout=True)
    session.clear()
    st.experimental_rerun()

import streamlit as st

def user_menu():
    with st.sidebar:
        choose = option_menu("Menu", ["Do an order","Logout"],
                            icons=['house','easel',"clipboard-data", '123',"graph-up", 'tv','person'],
                            menu_icon="cast", default_index=0,
                            styles={"container": {"padding": "5!important", "background-color": "#fafafa"},
                                    "icon": {"color": "orange", "font-size": "25px"}, 
                                    "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                    "nav-link-selected": {"background-color": "#02ab21"},
                                    },
                            )
    if choose == "Do an order":
        orders.insert_oders()
    elif choose == 'Logout':
        delete_login_info()
        