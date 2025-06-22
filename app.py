import pandas as pd
import numpy as np
import streamlit as st
import plotly.express as px
import plotly.graph_objs as go
import matplotlib.pyplot as plt

st.title('India Map Visualization')
st.markdown('This app visualizes various parameters across different states in India using a scatter map. '
            'You can select a state and two parameters to visualize their relationship on the map.')

df=pd.read_csv('Rahul.csv')
state=list(df['State'].unique())
state.insert(0,'Overall India')

columns=sorted(df.columns[5:])

st.sidebar.title('India Map')
select_state=st.sidebar.selectbox('Select a State',state)

primary=st.sidebar.selectbox('Select Primary Parameter',columns)
secondary=st.sidebar.selectbox('Select Secondary Parameter',columns)

plot=st.sidebar.button('Plot Graph')

if plot:
    st.text('Size represent  primary  parameter')
    st.text('Color represents secondary parameter')
    fig = go.Figure()
    if select_state == 'Overall India':
        fig=px.scatter_map(df,lat='Latitude',lon='Longitude',size=primary,color=secondary,
                           zoom=4,map_style='carto-positron',width=1200,height=700,hover_name='District')
        st.plotly_chart(fig,use_container_width=True)
    else:
        df_grouped = df[df['State'] == select_state]

        fig = px.scatter_map(df_grouped, lat='Latitude', lon='Longitude', size=primary, color=secondary, zoom=4,
                              map_style='carto-positron', width=1200, height=700, hover_name='District')
        st.plotly_chart(fig,use_container_width=True)