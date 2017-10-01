import psycopg2

try:
    connect_str = "dbname='mis_datos' user='pguser' host='localhost' " + \
                  "password='pass'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    cursor.execute("""SELECT * from datos""")
    rows = cursor.fetchall()
    print(rows)
except Exception as e:
    print("Error, revisa conexion, usuario o base de datos")
    print(e)
