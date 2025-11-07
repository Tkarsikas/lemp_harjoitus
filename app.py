from flask import Flask
import mysql.connector
app = Flask(__name__)
@app.route('/')
def home():
 # Connect to MySQL/MariaDB
 conn = mysql.connector.connect(
 host="localhost",
 user="tommi",
 password="moccamaster",
 database="kurssi_LEMP"
 )
 cursor = conn.cursor()
 cursor.execute("SELECT 'Testisivu toimiiiiiii!'")
 result = cursor.fetchone()
 # Clean up
 cursor.close()
 conn.close()
 return f"<h1>{result[0]}</h1>"
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
