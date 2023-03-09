import codecs
import pandas as pd
import streamlit as st
import numpy as np


st.title('Olympics 🏅')

DATA_URL=('olympic_athletes2.csv')


#cache de 500
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows ,index_col=0, encoding='latin-1')
    return data

#metodo de buscar nombre
def load_data_byname(name):
    doc = codecs.open('olympic_athletes2.csv', 'rU', 'latin1')
    data=pd.read_csv(doc)
    lowercase = lambda x: str(x).lower()
    name_lower = name.lower()
    filtered_data_byname = data[data["athlete_full_name "].str.contains(name_lower)]
    return filtered_data_byname


sidebar = st.sidebar
data_load_state = st.text('cargando dataset')
data = load_data(50)
st.subheader("Raw data")

#buscar por nombre
myname = sidebar.text_input("nombre: ")
botonname = sidebar.button("Search by name ")

if(botonname):
    filterbyname = load_data_byname(myname)
    count_now = filterbyname.shape[0]
    st.write(f"total names : {count_now}")
    data=filterbyname




st.sidebar.title('Heriberto Arriola Peztña ')
st.sidebar.text('zs2006737@estudiantes.uv.mx')
st.sidebar.markdown("___")
agree = sidebar.checkbox("Show raw data")
if agree:
    
    data_load_state.text('hecho!! (using st.cache)')
    st.dataframe(data)
    st.sidebar.markdown("___")

