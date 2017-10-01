import psycopg2

try:
    connect_str = "dbname='mis_datos' user='pguser' host='localhost' " + \
                  "password='pass'"
    conn = psycopg2.connect(connect_str)
    cursor = conn.cursor()
    cursor.execute("INSERT INTO datos VALUES('Antonio','Mondaca','Tapia',21,'2017-03-19 15:38:54.561004')")
    conn.commit()

except Exception as e:
    print("Error, revisa conexion, usuario o base de datos")
    print(e)
