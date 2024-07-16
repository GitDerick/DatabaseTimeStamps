# View

import streamlit as st
from projet_model import add_customer, delete_customer, get_all_customers, update_customer


def show_header():
    st.write('# Projet RCS')

def show_add_customer_sidebar():
    st.sidebar.title("Ajouter un Nouveau Client")
    name = st.sidebar.text_input("Nom")
    age = st.sidebar.number_input("Age", min_value=0, max_value=120)
    salary = st.sidebar.number_input("Salaire", min_value=0.0)
    email = st.sidebar.text_input("Email")
    return name, age, salary, email

def show_customers(customers):
    st.header("Liste des Clients")
    for customer in customers:
        st.write(f"ID: {customer['id']}, Name: {customer['name']}, Age: {customer['age']}, Salary: {customer['salary']}, Email: {customer['email']}")
        if st.button(f"Supprimer le client {customer['id']}"):
            delete_customer(customer['id'])
            st.success("Le client a été supprimé avec succès!")


def show_update_customer_sidebar(customers):
    st.sidebar.title("Modifier un Client")
    selected_customer_id = st.sidebar.selectbox("Sélectionner un client à modifier :", [customer['id'] for customer in customers])
    selected_customer = next((customer for customer in customers if customer['id'] == selected_customer_id), None)
    if selected_customer:
        name = st.sidebar.text_input("Nom", value=selected_customer['name'])
        age = st.sidebar.number_input("Age", min_value=0, max_value=120, value=selected_customer['age'])
        salary = st.sidebar.text_input("Salaire", value=str(selected_customer['salary']))
        email = st.sidebar.text_input("Email", value=selected_customer['email'])
        return selected_customer_id, name, age, salary, email
    else:
        return None, None, None, None, None



def show_success_message(message):
    st.success(message)

def show_error_message(message):
    st.error(message)
