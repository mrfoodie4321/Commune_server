# class Server(BaseHTTPRequestHandler):
# def do_GET(self):
# self.send_response(200)
# self.send_header("Content-type", "text/html")
# self.end_headers()
# print("hi")

# def do_POST(self):
# self.send_response(200)
# self.send_header("Context-type", "text/html")
# self.end_headers()


# connection = sqlite3.connect("commune.db")
# print(connection.total_changes)

# cursor = connection.cursor()
# cursor.execute("CREATE TABLE companies(name TEXT, type TEXT, resources TEXT, email TEXT, phone number TEXT)")
# cursor.execute("INSERT INTO companies VALUES ('FEED MY STARVING CHILDREN', 'FOOD SHELTER', 'volunteering activities', '?', '?')")
# cursor.execute("INSERT INTO companies VALUES ('MCDONALDS', 'RESTAURANT', 'part time jobs', '?', '?')")
# rows = cursor.execute("SELECT name, type, resources, email, phone number FROM companies").fetchall()
# print(rows)
import sqlite3
from sqlite3 import Error


def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by db_file
    :param db_file: database file
    :return: Connection object or None
    """
    # conn = sqlite3.connect(db_file)
    # return conn
    conn = None
    try:
        conn = sqlite3.connect(db_file)
        return conn
    except Error as e:
        print(e)

    return conn


def create_table(conn, create_table_sql):
    """ create a table from the create_table_sql statement
    :param conn: Connection object
    :param create_table_sql: a CREATE TABLE statement
    :return:
    """
    # c = conn.cursor()
    # c.execute(create_table_sql)
    try:
        c = conn.cursor()
        c.execute(create_table_sql)
    except Error as e:
        print(e)


def main():
    database = r"C:\Users\User\PycharmProjects\Commune_server\users.db"

    sql_create_school_table = """CREATE TABLE IF NOT EXISTS school (
                                        zip INTEGER PRIMARY KEY,
                                        name TEXT,
                                        type TEXT,
                                        location TEXT
                                        );"""



    sql_create_companies_table = """CREATE TABLE IF NOT EXISTS companies (
                                    zip INTEGER PRIMARY KEY,
                                    school_zip INTEGER,
                                    name TEXT,
                                    type TEXT,
                                    resource TEXT,
                                    email TEXT,
                                    phone number TEXT
                                );"""

    def insert_to_table(c):
        c.execute("INSERT INTO sql_create_school_table('Stevenson', 'high school', 'Lincolnshire IL', '60069')")
        c.execute("INSERT INTO sql_create_school_table('Twin Groves', 'middle school', 'Buffalo Grove', '60089')")
        c.execute("INSERT INTO sql_create_companies_table('Jazzmans', 'coffee restaurant', '?', '?', '?', '60069')")
        c.execute("INSERT INTO aql_create_companies_table('Culvers', 'fast food restaurant', '?', '?', '?', '?')")

    # create a database connection
    conn = create_connection(database)

    # create tables
    if conn is not None:
        # create school table
        create_table(conn, sql_create_school_table)

        # create companies table
        create_table(conn, sql_create_companies_table)

    else:
        print("Error! cannot create the database connection.")

        # find_companies_near_school()


if __name__ == '__main__':
    main()