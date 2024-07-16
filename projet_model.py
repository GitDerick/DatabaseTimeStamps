# Model
import mysql.connector

def create_connection():
    conn = None
    try:
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="projet_test",
            port=3306
        )
        return conn
    except mysql.connector.Error as e:
        print(e)
    return conn

def add_customer(name, age, salary, email):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            sql = "INSERT INTO customer(name, age, salary, email) VALUES (%s, %s, %s, %s)"
            cursor.execute(sql, (name, age, salary, email))
            conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Erreur lors de l'ajout du client : {e}")
            return False
        finally:
            if conn.is_connected():
                conn.close()

def delete_customer(customer_id):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            sql = "DELETE FROM customer WHERE id = %s"
            cursor.execute(sql, (customer_id,))
            conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Erreur lors de la suppression du client : {e}")
            return False
        finally:
            if conn.is_connected():
                conn.close()



def update_customer(customer_id, name, age, salary, email):
    conn = create_connection()
    if conn is not None:
        try:
            cursor = conn.cursor()
            sql = "UPDATE customer SET name = %s, age = %s, salary = %s, email = %s WHERE id = %s"
            cursor.execute(sql, (name, age, salary, email, customer_id))
            conn.commit()
            return True
        except mysql.connector.Error as e:
            print(f"Erreur lors de la mise à jour du client : {e}")
            return False
        finally:
            if conn.is_connected():
                conn.close()


def get_all_customers():
    conn = create_connection()
    customers = []
    if conn is not None:
        try:
            cursor = conn.cursor()
            cursor.execute("SELECT * FROM customer")
            rows = cursor.fetchall()
            for row in rows:
                customers.append({
                    "id": row[0],
                    "name": row[1],
                    "age": row[2],
                    "salary": row[3],
                    "email": row[4]
                })
        except mysql.connector.Error as e:
            print(f"Erreur lors de la récupération des clients : {e}")
        finally:
            if conn.is_connected():
                conn.close()
    return customers
