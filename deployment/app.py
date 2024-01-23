# Creating a selection method between EDA and Prediction page

import streamlit as st
import eda
import prediction

page = st.sidebar.selectbox('Choose a page:', ('EDA', 'Detection'))

if page == 'EDA':
    eda.run()
else:
    prediction.run()    