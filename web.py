import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state['new_todo'] + '\n'
    todos.append(todo) 
    functions.write_todos(todos)


st.title('My todo App')
st.subheader('This is todo app')
st.write('this app is to increase productivity')

for todo in todos:
    st.checkbox(todo)
    
st.text_input(label="New todo", placeholder='Add todo', on_change=add_todo, key='new_todo')

st.session_state