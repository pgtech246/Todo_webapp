import streamlit as st
import readwrite

todos = readwrite.get_todos("todos.txt")

st.title("My Todo App")
st.subheader("This is my todo app.")
st.write("This app is to increase your productivity.")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="Add", label_visibility="collapsed", placeholder="Add new todo")
