import psycopg2

from mail import Mailer

connection = None
cursor = None
try:
    connection = psycopg2.connect(user="postgres",password="postgres",host="127.0.0.1",port="5432",database="postgres")
    cursor = connection.cursor()
    cursor.execute("select * from receivers where sent = false")
    rows = cursor.fetchall()
    mailer = Mailer()
    mailer.connect()
    for row in rows:
        receiver = row[0]
        mailer.send(receiver)
        cursor.execute(f"update receivers set sent = true where email = '{receiver}'")
        connection.commit()

except (Exception, psycopg2.Error) as error:
    print("Error while sending emails", error)

finally:
    if cursor is not None:
        cursor.close()
    if connection is not None:
        connection.close()
    print("PostgreSQL connection is closed")