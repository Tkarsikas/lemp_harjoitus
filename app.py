from flask import Flask, jsonify, render_template
import mysql.connector

app = Flask(__name__)

def home():
 # Connect to MySQL/MariaDB
 conn = mysql.connector.connect(
 host="localhost",
 user="tommi",
 password="moccamaster",
 database="kurssi_LEMP"
 )
 
@app.route('/')
def api_time():
    conn = home()
    cur = conn.cursor()
    cur.execute("SELECT NOW();")
    row = cur.fetchone()
    cur.close()
    conn.close()

    if row:
        return jsonify({"time": str(row[0])})
    else:
        return jsonify({"time": None}), 500

if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)


