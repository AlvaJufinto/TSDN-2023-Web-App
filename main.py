import streamlit as st
import utils as utl
from views import home,about,contact

st.set_page_config(layout="wide", page_title='Websites Phising Detectors')
st.set_option('deprecation.showPyplotGlobalUse', False)
utl.inject_custom_css()
utl.navbar_component()

def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view()
    elif route == "about":
        about.load_view()
    elif route == "contact":
        contact.load_view()
    elif route == None:
        home.load_view()
        
navigation()