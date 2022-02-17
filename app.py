from explore import show_explore_page
from predict_page import show_predict_page
import streamlit as st

st.sidebar.title('Navigation')
select_page = st.sidebar.selectbox(
    "Explore or Predict", ("Explore", "Predict"))

if select_page == 'Explore':
    show_explore_page()
else:
    show_predict_page()
