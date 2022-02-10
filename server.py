from flask import Flask
import psycopg2

app = Flask(__name__)

# postgres connection
conn = psycopg2.connect(
	host="localhost",
	database="postgres",
	user="postgres",
	password="hank",
	port=5432
)

cur = conn.cursor()

if (conn):
	print("Connection established")
else:
	print("Connection failed")

# close the connection
conn.close()

if __name__ == "__main__":
	app.run(host="localhost", port=5000, debug=True)