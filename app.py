from flask import Flask, request, jsonify
import pandas as pd
from models import (
    insert_customers,
    insert_orders,
    get_customer_summary,
    get_top_customers,
    get_inactive_customers,
    get_orders_report
)
from utils import validate_customers, validate_orders
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)

@app.route('/upload/customers', methods=['POST'])
def upload_customers():
    try:
        file = request.files.get('file')
        if not file:
            return jsonify({'error': 'No file uploaded'}), 400

        df = pd.read_csv(file)
        if df.empty:
            return jsonify({'error': 'Uploaded customer file is empty'}), 400

        df = validate_customers(df)
        if df.empty:
            return jsonify({'error': 'No valid customer data found after validation'}), 400

        insert_customers(df)
        return jsonify({'message': 'Customers uploaded successfully'}), 200

    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_NO_REFERENCED_ROW:
            return jsonify({'error': 'Invalid customer_id in data'}), 400
        elif err.errno == errorcode.ER_DUP_ENTRY:
            return jsonify({'error': 'Duplicate customer entry found'}), 409
        else:
            return jsonify({'error': f'Database error: {str(err)}'}), 500

    except Exception as e:
        return jsonify({'error': f'Unexpected error: {str(e)}'}), 500


@app.route('/upload/orders', methods=['POST'])
def upload_orders():
    try:
        file = request.files.get('file')
        if not file:
            return jsonify({'error': 'No file uploaded'}), 400

        df = pd.read_csv(file)
        if df.empty:
            return jsonify({'error': 'Uploaded orders file is empty'}), 400

        from db import get_db_connection
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("SELECT customer_id FROM customers")
        existing_ids = [row[0] for row in cursor.fetchall()]
        cursor.close()
        conn.close()

        df = validate_orders(df, existing_ids)
        if df.empty:
            return jsonify({'error': 'No valid order data found after validation'}), 400

        insert_orders(df)
        return jsonify({'message': 'Orders uploaded successfully'}), 200

    except Exception as e:
        return jsonify({'error': f'Failed to upload orders: {str(e)}'}), 500



@app.route('/customer/<int:id>/summary', methods=['GET'])
def customer_summary(id):
    try:
        result = get_customer_summary(id)
        if result:
            return jsonify({
                'customer_id': result[0],
                'customer_name': result[1],
                'order_count': result[2],
                'total_spent': result[3]
            })
        return jsonify({'error': 'Customer not found'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/top-customers', methods=['GET'])
def top_customers():
    try:
        result = get_top_customers()
        return jsonify([
            {'customer_id': r[0], 'customer_name': r[1], 'total_spent': r[2]}
            for r in result
        ])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/orders/report', methods=['GET'])
def order_report():
    try:
        result = get_orders_report()
        return jsonify([
            {'date': str(r[0]), 'total_revenue': r[1]}
            for r in result
        ])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


@app.route('/inactive-customers', methods=['GET'])
def inactive_customers():
    try:
        result = get_inactive_customers()
        return jsonify([
            {'customer_id': r[0], 'customer_name': r[1], 'location': r[2]}
            for r in result
        ])
    except Exception as e:
        return jsonify({'error': str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
