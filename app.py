from flask import Flask, jsonify
import mysql.connector
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
def get_time():
 # Connect to MySQL/MariaDB
 conn = mysql.connector.connect(
 host=os.getenv("DB_HOST"),
 user=os.getenv("DB_USER"),
 password=os.getenv("DB_PASS"),
 database=os.getenv("DB_NAME")
 
 /*host="localhost",
 user="tommi",
 password="moccamaster",
 database="kurssi_LEMP"
 */
 )
 cursor = conn.cursor()
 cursor.execute("SELECT NOW();")
 result = cursor.fetchone()
 # Clean up
 cursor.close()
 conn.close()
 return str(result[0])

@app.route('/time')
def api_time():
    return jsonify({"time": get_time()})

@app.route('/')
def home():
    return '''
    <html>
    <head>
        <title>MySQL Clock</title>
        <script>
            async function updateClock() {
                const response = await fetch('/time');
                const data = await response.json();
                document.getElementById('clock').innerText = data.time;
            }

            // Päivitä kello heti ja sen jälkeen joka sekunti
            setInterval(updateClock, 1000);
            window.onload = updateClock;
        </script>
    </head>
    <body style="font-family: Arial; text-align: center; margin-top: 100px; background-color: pink;">
        <h1>MySQL Server Time</h1>
        <h2 id="clock">Loading...</h2>
        <img src="/static/ursos-fritando-bear.gif" alt="animated gif" style="width: 600px;" />
    </body>
    </html>
    '''
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
