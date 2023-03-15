import codecs
import pandas as pd
import streamlit as st
import plotly.express as px

st.title('Olympics 🏅')

DATA_URL=('olympic_athletes2.csv')
df=pd.read_csv(DATA_URL)

#cache de 500
@st.cache
def load_data(nrows):
    data = pd.read_csv(DATA_URL,nrows=nrows , encoding='latin-1')
    return data

#metodo de buscar nombre
def load_data_byname(name):
    doc = codecs.open('olympic_athletes2.csv', 'rU', 'latin1')
    data=pd.read_csv(doc)
    lowercase = lambda x: str(x).lower()
    name_lower = name.lower()
    data["athlete_full_name"] = data["athlete_full_name"].str.lower()
    filtered_data_byname = data[data["athlete_full_name"].str.contains(name_lower)]
    return filtered_data_byname

#__________ 

sidebar = st.sidebar

#para cargar el data set en 500

data = load_data(500)
st.subheader("Raw data")
data_load_state = st.text('esperando dataset')
st.sidebar.image("logo.png")
st.sidebar.title('Heriberto Arriola Peztña ')
st.sidebar.text('zs2006737@estudiantes.uv.mx')
st.sidebar.markdown("___")

agree = sidebar.checkbox("Show raw data")

if agree:
    
    data_load_state.text('hecho!! (using st.cache)')
    st.dataframe(data)

#buscar por nombre
st.markdown("___")
st.subheader("Buscar por nombre")
myname = sidebar.text_input("nombre: ")
botonname = sidebar.button("Search by name ")

if(botonname):
    filterbyname = load_data_byname(myname)
    count_now = filterbyname.shape[0]
    st.write(f"total names : {count_now}")
    data=filterbyname
    st.dataframe(data)

#el multiselect filtrar por sede
multiselectdf= df.sort_values(by="first_game") #para ordenar en alfabetico
game = st.sidebar.multiselect("Selecciona los JJOO", options=multiselectdf['first_game'].unique(), default=multiselectdf['first_game'].unique()[:3])

st.markdown("___")
st.subheader("Filtrar por sede")
st.write("Mostrar competidores por cada edición de JJOO:\n\n " + ", ".join(game)) #concatenar la cadena game

st.write(df.query(f"""first_game==@game"""))
st.markdown("___")

#histograma por competidores por rango de edad
st.subheader("Gráficos")
st.write("Histograma que muestra la relacion entre la cantidad de competidores que han participado en los JJOO por rango de edad (año de nacimiento)")

fig = px.histogram(df, x='athlete_year_birth', nbins=10)
fig.update_layout(title='Numero de competidores por rango de edad',
                  xaxis_title='Año de nacimiento',
                  yaxis_title='Frecuencia')
st.plotly_chart(fig)

st.write("\n\nGrafica de barras que muestra cuantas veces a participado cada competidor.\n Para el grafico se cargaron los primero 30 registros")

fig2 = px.bar(df[:30], x='games_participations', y='athlete_full_name', orientation='h', color='games_participations')
fig2.update_layout(title='¿Cuantas veces han participado los competidores en los JJOO?',
                  xaxis_title='participations',
                  yaxis_title='nombres')

st.plotly_chart(fig2)

datagrafica=load_data(1000)

st.write("\n\nGrafica de dispersion que muestra la relacion entre las medallas ganadas y el año de nacimiento de los competidores.\n Para el grafico se cargaron los primero 1000 registros")
fig3 = px.scatter(datagrafica, x='athlete_year_birth', y='athlete_medals')
fig3.update_layout(title='Grafica de Dispersión del Titanic',
                   xaxis_title='Año de nacimiento',
                   yaxis_title='Medallas')
st.plotly_chart(fig3)

st.sidebar.image("Uv Anverso.png")
