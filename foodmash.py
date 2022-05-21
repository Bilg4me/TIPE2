import streamlit as st
from tri import matchs, tri
from itertools import combinations
from classes import Aliment
from random import shuffle, sample, choice
import yagmail
st.title('Foodmash')

# INITIALIZATION

if 'aliments' not in st.session_state:
    food = choice(['fruits_valid.txt', 'genericfood_valid.txt'])
    with open(food) as file:
        alimentsListe = file.readlines()
    st.session_state.aliments = [Aliment(a) for a in sample(alimentsListe, k=10)]
    st.session_state.matchs = list(combinations(st.session_state.aliments, 2))
    shuffle(st.session_state.matchs)
    st.session_state.progression = 0

if st.session_state.progression == len(st.session_state.matchs):
    st.balloons()
    st.success('Thank you for foodmashing this list.')
    st.table(tri(st.session_state.aliments, True))
    contents = ["{} {}".format(nom,str(elo)) for (nom,elo) in tri(st.session_state.aliments,True)]
    yagmail.SMTP('dxtamailing@gmail.com', 'khube27kharre9').send('dxtamailing@gmail.com', 'foodmash', contents)
    st.stop()
   
[a1,a2] = st.session_state.matchs[st.session_state.progression]
[b1,b2] = st.session_state.matchs[st.session_state.progression - 1]
print(st.session_state.progression)

# BODY

col1,col2 = st.columns(2)

with col1: 
    st.write(str(a1))
    st.image(a1.image)
    if st.button("I prefer",key=1):
        matchs(b1,b2, 1)
        
with col2:
    st.write(str(a2))
    st.image(a2.image)
    if st.button("I prefer",key=2):
        matchs(b1,b2, 0)

st.progress(st.session_state.progression/len(st.session_state.matchs))
st.session_state.progression += 1
st.table(tri(st.session_state.aliments, True))

# =TODO========================================================================
# -> Side bar to choose eloRating parameters (coefficient K et critere)
# -> Submit to csv the table made after foodmashing (by email or an other way)
# =============================================================================
