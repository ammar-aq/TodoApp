import streamlit as st
import requests

BASE_URL = "http://127.0.0.1:8000"

st.title("Todo App")

def create_todo():
    st.header("Create Todo")
    title = st.text_input("Enter Todo Title")
    description = st.text_area("Enter Todo Description")
    if st.button("Add Todo"):
        response = requests.post(f"{BASE_URL}/todos/", json={"title": title, "description": description})
        if response.status_code == 200:
            st.success("Todo added successfully")

def delete_todo():
    st.header("Delete Todo")
    todo_id = st.number_input("Enter Todo ID to delete")
    if st.button("Delete Todo"):
        response = requests.delete(f"{BASE_URL}/todos/{todo_id}")
        if response.status_code == 200:
            st.success("Todo deleted successfully")

def update_todo():
    st.header("Update Todo")
    todo_id = st.number_input("Enter Todo ID to update")
    title = st.text_input("Enter Updated Todo Title")
    description = st.text_area("Enter Updated Todo Description")
    if st.button("Update Todo"):
        response = requests.put(f"{BASE_URL}/todos/{todo_id}", json={"title": title, "description": description})
        if response.status_code == 200:
            st.success("Todo updated successfully")

def read_todo():
    st.header("List of Todos:")
    response = requests.get(f"{BASE_URL}/todos/")
    if response.status_code == 200:
        todos = response.json()

        # Allow sorting by column
        sort_option = st.selectbox("Sort by:", ["id", "title", "description"])
        reverse_order = st.checkbox("Reverse Order")

        # Sort the todos based on user selection
        todos = sorted(todos, key=lambda x: x[sort_option], reverse=reverse_order)

        # Display todos in a table
        #st.table(todos)
        # Display todos with pagination
        # Display todos with pagination
        page_size = st.slider("Number of Todos per Page", min_value=1, max_value=50, value=10)
        page_number = st.number_input("Page Number", min_value=1, value=1)
        start_idx = (page_number - 1) * page_size
        end_idx = start_idx + page_size

        st.table(todos[start_idx:end_idx])

if __name__ == "__main__":
    read_todo()
    create_todo()
    delete_todo()
    update_todo()
    