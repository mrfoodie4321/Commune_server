import sqlite3
from http.server import BaseHTTPRequestHandler, HTTPServer


class Server(BaseHTTPRequestHandler):
    def do_GET(self):
        self.send_response(200)
        self.send_header("Content-type", "text/html")
        self.end_headers()
        print("hi")

    #def do_POST(self):


connection = sqlite3.connect("commune.db")
print(connection.total_changes)

cursor = connection.cursor()
#cursor.execute("CREATE TABLE companies(name TEXT, type TEXT, resources TEXT, email TEXT, phone number TEXT)")
cursor.execute("INSERT INTO companies VALUES ('FEED MY STARVING CHILDREN', 'FOOD SHELTER', 'volunteering activities', '?', '?')")
cursor.execute("INSERT INTO companies VALUES ('MCDONALDS', 'RESTAURANT', 'part time jobs', '?', '?')")
rows = cursor.execute("SELECT name, type, resources, email, phone number FROM companies").fetchall()
print(rows)