import streamlit as st
from projet_model import add_customer, delete_customer, get_all_customers, update_customer
import projet_view

def main():
    projet_view.show_header()

    name, age, salary, email = projet_view.show_add_customer_sidebar()
    if st.sidebar.button("Ajouter Client"):
        success = add_customer(name, age, salary, email)
        if success:
            projet_view.show_success_message("Le client a été ajouté avec succès à la base de données.")
        else:
            projet_view.show_error_message("Erreur lors de l'ajout du client.")

    customers = get_all_customers()
    projet_view.show_customers(customers)


    selected_customer_id, name, age, salary, email = projet_view.show_update_customer_sidebar(customers)
    if st.sidebar.button("Modifier Client"):
        success = update_customer(selected_customer_id, name, age, salary, email)
        if success:
            projet_view.show_success_message("Le client a été modifié avec succès !")
        else:
            projet_view.show_error_message("Erreur lors de la modification du client !")


if __name__ == '__main__':
    main()
