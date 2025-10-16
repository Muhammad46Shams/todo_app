import streamlit as st
import functions

todos = functions.get_todos()

st.title('My todo App')
st.subheader('This is todo app')
st.write('this app is to increase productivity')

for todo in todos:
    st.checkbox(todo)
    
st.text_input(label="", placeholder='Add todo')