#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 29 17:27:30 2021

@author: brome
"""

import streamlit as st

with st.form(key='my_form'):
    pseudo = st.text_input(label='pseudo')
    age = st.number_input('age',0,77)
    sexe = st.radio('sexe', ['M','F'])
    grpsanguin = st.selectbox(label='groupe sanguin', options=['O','A','B','AB'])
    allergies = st.multiselect('Allergies', ['fruits à coques','oeuf','lait'])
    niveausportif = st.select_slider('Niveau sportif', options=['Novice','Intermédiaire','Confirmé'])
    submit_button = st.form_submit_button(label='Submit')
    
    
# -> redirection vers autre app (après le submit)
# -> Choose to sort fruits or vegetables or other type of food