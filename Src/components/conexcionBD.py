import sqlite3
import os

BasedeDatos = 'src/DataBase/BaseDeDatos.db'
if os.path.isfile(BasedeDatos):
    pass
else:
    conexion = sqlite3.connect(BasedeDatos)
    cursor = conexion.cursor()
    with open('src/DataBase/BaseDeDatos.sql', 'r') as f:
        script_sql = f.read()
    cursor.executescript(script_sql)


def validar_credenciales_profesor(documento_profesor, contrasena):
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()

    # Verificar si el documento del profesor existe
    cursor.execute('''
        SELECT COUNT(*) FROM PROFESORES
        WHERE Documento_Profesor = ?
    ''', (documento_profesor,))
    existe_documento = cursor.fetchone()[0] > 0
    # Si el documento no existe, retornar False
    if not existe_documento:
        cursor.close()
        conexion.close()
        return False
    # Verificar si la contraseña es correcta para el documento proporcionado
    cursor.execute('''
        SELECT COUNT(*) FROM PROFESORES
        WHERE Documento_Profesor = ? AND Contraseña = ?
    ''', (documento_profesor, contrasena))
    contrasena_valida = cursor.fetchone()[0] > 0

    # Retornar True si las credenciales son válidas
    if contrasena_valida:
        cursor.close()
        conexion.close()
        return True


def obtener_id_profesor(documento_profesor):
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()
    # Buscar el ID_Profesor en la base de datos
    cursor.execute('''
        SELECT ID_Profesor
        FROM PROFESORES
        WHERE Documento_Profesor = ?
    ''', (documento_profesor,))
    resultado = cursor.fetchone()

    # Si se encontró un registro, extraer el ID_Profesor
    if resultado:
        profesor_id = resultado[0]
    else:
        profesor_id = None
    # Retornar el ID_Profesor o None
    cursor.close()
    conexion.close()
    return profesor_id
