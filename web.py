import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)
    st.session_state["new_todo"] = ""

# Order matters
# Refreshing re-executes python code
# Requires a lot of ram to run this across servers
st.title("My To-Do App")
st.subheader("Created by Adam Luk")
st.write("This app is to increase productivity")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo) # needs to have dynamic keys for each to do
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Enter a new to-do", on_change=add_todo, key='new_todo')
st.session_state # dictionary updated with new_todo