from flask import Flask, jsonify
import mysql.connector
app = Flask(__name__)
def get_time():
 # Connect to MySQL/MariaDB
 conn = mysql.connector.connect(
 host="localhost",
 user="tommi",
 password="moccamaster",
 database="kurssi_LEMP"
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
    <body style="font-family: Arial; text-align: center; margin-top: 100px; bachkground-color: #f0f0f0;">
        <h1>MySQL Server Time</h1>
        <h2 id="clock">Loading...</h2>
    </body>
    </html>
    '''
if __name__ == '__main__':
 app.run(host='0.0.0.0', port=5000)
