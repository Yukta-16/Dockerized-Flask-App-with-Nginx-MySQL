from flask import Flask, jsonify
import mysql.connector
import os

app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to Dockerized Flask App with MySQL & Nginx!"

@app.route('/users')
def get_users():
    try:
        db = mysql.connector.connect(
            host=os.getenv("DB_HOST", "mysql"),
            user=os.getenv("DB_USER", "root"),
            password=os.getenv("DB_PASSWORD", "root"),
            database=os.getenv("DB_NAME", "flaskdb")
        )
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users;")
        users = cursor.fetchall()
        return jsonify(users)
    except Exception as e:
        return jsonify({"error": str(e)})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
