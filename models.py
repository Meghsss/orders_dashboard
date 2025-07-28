import mysql.connector

db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="megha",
    database="order_dashboard"
)
cursor = db.cursor()

def insert_customers(df):
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO customers (customer_id, customer_name, location) VALUES (%s, %s, %s)",
            (row['customer_id'], row['customer_name'], row['location'])
        )
    db.commit()

def insert_orders(df):
    for _, row in df.iterrows():
        cursor.execute(
            "INSERT INTO orders (order_id, customer_id, amount, date) VALUES (%s, %s, %s, %s)",
            (row['order_id'], row['customer_id'], row['amount'], row['date'])
        )
    db.commit()

def get_customer_summary(customer_id):
    cursor.execute("""
        SELECT c.customer_id, c.customer_name, COUNT(o.order_id), COALESCE(SUM(o.amount), 0)
        FROM customers c LEFT JOIN orders o ON c.customer_id = o.customer_id
        WHERE c.customer_id = %s
        GROUP BY c.customer_id
    """, (customer_id,))
    return cursor.fetchone()

def get_top_customers():
    cursor.execute("""
        SELECT c.customer_id, c.customer_name, SUM(o.amount) AS total
        FROM customers c
        JOIN orders o ON c.customer_id = o.customer_id
        GROUP BY c.customer_id
        ORDER BY total DESC
        LIMIT 3
    """)
    return cursor.fetchall()

def get_orders_report():
    cursor.execute("SELECT date, SUM(amount) FROM orders GROUP BY date ORDER BY date")
    return cursor.fetchall()

def get_inactive_customers():
    cursor.execute("""
        SELECT * FROM customers
        WHERE customer_id NOT IN (
            SELECT DISTINCT customer_id FROM orders
        )
    """)
    return cursor.fetchall()
