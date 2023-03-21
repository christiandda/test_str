import streamlit as st
from streamlit_option_menu import option_menu
from scripts import drivers
from scripts import shops
from scripts import location
from scripts import heatmap
from scripts import orders



st.set_page_config(layout='wide')

# Defines a sidebar menu using the st.sidebar function from the Streamlit library

# This opens a sidebar in the Streamlit app.
with st.sidebar:
    choose = option_menu("Menu", ["Drivers","Shops","Location Map", "Heatmap","Orders"],
                         icons=['house','easel',"clipboard-data", '123',"graph-up", 'tv','person'],
                         menu_icon="cast", default_index=0,
                         styles={"container": {"padding": "5!important", "background-color": "#fafafa"},
                                "icon": {"color": "orange", "font-size": "25px"}, 
                                "nav-link": {"font-size": "16px", "text-align": "left", "margin":"0px", "--hover-color": "#eee"},
                                "nav-link-selected": {"background-color": "#02ab21"},
                                },
                        )

# This creates a drop-down menu in the sidebar with six options: 
# "About", "What is anime?", "Exploring data", "Get recommendations", "EDA", "Anime Info", and "About the Creator". 
# The icons argument provides icons for each option. menu_icon sets the icon for the sidebar. 
# default_index sets the default option in the drop-down menu. styles sets the styling for the drop-down menu.


# This uses the choose variable to determine which option was selected in the drop-down menu. 
# Depending on the option selected, it calls a specific function to display the corresponding 
# content in the main panel of the Streamlit app.

if choose == "Drivers":
    drivers.drivers_info()

elif choose == "Shops":
    shops.shops_info()

elif choose == "Location Map":
    location.location_info()

elif choose == "Heatmap":
    heatmap.heatmap_info()

elif choose == "Orders":
    orders.insert_oders()