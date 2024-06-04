import mysql.connector


def connect_to_database():
    try:
        connection = mysql.connector.connect(
            host='localhost',  # usualmente es 'localhost' para XAMPP
            user='root',  # reemplaza 'tu_usuario' con tu nombre de usuario de MySQL
            password='',  # reemplaza 'tu_contraseña' con tu contraseña de MySQL
            # reemplaza con el nombre de tu base de datos
            database='pruebas_recofacial'
        )

        if connection.is_connected():
            print('Conexión exitosa a la base de datos')
            return connection
    except Exception as e:
        print('Error al conectar a la base de datos:', e)


def close_connection(connection):
    if connection.is_connected():
        connection.close()
        print('La conexión a la base de datos se ha cerrado')


# Ejemplo de uso
connection = connect_to_database()
# Aquí puedes realizar tus operaciones con la base de datos
close_connection(connection)
