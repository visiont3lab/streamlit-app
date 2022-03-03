import streamlit as st
import plotly.express as px
import pandas as pd

st.write("This is my first app")

df = pd.read_csv("https://raw.githubusercontent.com/pcm-dpc/COVID-19/master/dati-andamento-nazionale/dpc-covid19-ita-andamento-nazionale.csv")

col1, col2 = st.columns(2)
col3, col4 = st.columns(2)

  
with col1:
  fig1 = px.area(df,x="data", y=["dimessi_guariti","deceduti"])
  st.header("Andamento Nazionale")
  st.plotly_chart(fig1)

with col2:
  fig2 = px.area(df,x="data", y=["nuovi_positivi"])
  st.header("Nuovi Positivi")
  st.plotly_chart(fig2)

with col3:
  fig3 = px.area(df,x="data", y=["variazione_totale_positivi"])
  st.header("Variazione Positivi")
  st.plotly_chart(fig1)

with col4:
  fig4 = px.line(df,x="data", y=["totale_positivi","dimessi_guariti","deceduti","totale_casi"])
  st.header("Covid19 Status")
  st.plotly_chart(fig4)
