import os
import streamlit as st
from streamlit_option_menu import option_menu
from scripts import drivers
from scripts import shops
from scripts import location
from scripts import heatmap
from scripts import orders
import json

from scripts import dash_menu
from scripts import driver_menu
from scripts import user_menu

st.set_page_config(layout='wide')
os.environ["STREAMLIT_SERVER_MODE"] = "production"

def call_user(n,p):
    # Load the JSON file into a dictionary
    with open('users_logins.json', 'r') as f:
        my_dict = json.load(f)
    # Print the resulting dictionary
    print(my_dict)

    for user in my_dict:
        if user['name'] == n:
            if user['password'] == p:
                type = user['type']
                messege = "Login successful"
                return True,messege,type
            else:
                messege = "Wrong password"
                return False,messege
                break
    else:
        messege = "Username not found"
        return False,messege


session = st.session_state

if 'login' not in session:
    # Display the login form if the user is not logged in
    username = st.text_input('Username')
    password = st.text_input('Password', type='password')
    submit_button = st.button('Submit')



    if submit_button:
      status, mess,typ = call_user(username,password)
      if status == False:
          st.error(mess)
      else:
          session['login'] = True
          session['username'] = username
          session['menu'] = typ
          st.success('Login successful')
          st.experimental_rerun()

if 'login' in session:
    # Display the appropriate menu based on the user's credentials
    if session['menu'] == 'admin':
        st.write("Hello", session['username'])
        dash_menu.dash_menu()
    elif session['menu'] == 'user':
        st.write("Hello", session['username'])
        user_menu.user_menu()
    elif session['menu'] == 'driver':
        st.write("Hello", session['username'])
        driver_menu.driver_menu()    
    # Allow the user to log out
    if st.button('Log out'):
        session.clear()
        st.experimental_rerun()





#    if submit_button:
#        # Check the user's credentials and log them in if they are valid
#        if username in login_admin['credentials']['usernames']:
#            if password == str(login_admin['credentials']['usernames'][username]['password']):
#                session['login'] = True
#                session['username'] = username
#                session['menu'] = 'admin'
#                st.success('Login successful')
#                st.experimental_rerun()
#
#            else:
#                st.error('Invalid password or user')
#
#        elif username in login_driver['credentials']['usernames']:
#            if password == str(login_driver['credentials']['usernames'][username]['password']):
#                session['login'] = True
#                session['username'] = username
#                session['menu'] = 'driver'
#                st.success('Login successful')
#                st.experimental_rerun()
#
#            else:
#                st.error('Invalid password or user')
#
#        elif username in login_users['credentials']['usernames']:
#            if password == str(login_users['credentials']['usernames'][username]['password']):
#                session['login'] = True
#                session['username'] = username
#                session['menu'] = 'user'
#                st.success('Login successful')
#                st.experimental_rerun()
#
#            else:
#                st.error('Invalid password or user')
#
#        else:
#            st.error('Invalid password or user')
#
#if 'login' in session:
#    # Display the appropriate menu based on the user's credentials
#    if session['menu'] == 'admin':
#        st.write(f"Hello, {login_admin['credentials']['usernames'][session['username']]['name']}")
#        heatmap.heatmap_info()
#    elif session['menu'] == 'driver':
#        st.write(f"Hello, {login_driver['credentials']['usernames'][session['username']]['name']}")
#        drivers.drivers_info()
#    elif session['menu'] == 'user':
#        st.write(f"Hello, {login_users['credentials']['usernames'][session['username']]['name']}")
#        orders.insert_oders()
#        # Allow the user to log out
#    if st.button('Log out'):
#        session.clear()
#        st.experimental_rerun()
#