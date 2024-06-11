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
        WHERE Documento_Profesor = ? AND Contrasena = ?
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

#!HOJA DE WORD 2


def insertar_clase(nombre_clase, profesor_id, datos):
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()

    # Preparar la sentencia SQL para insertar la clase
    cursor.execute('''
        INSERT INTO CLASES (Nombre_Clase, Profesor_ID, Datos_clase)
        VALUES (?, ?, ?)
    ''', (nombre_clase, profesor_id, datos))

    # Guardar los cambios en la base de datos
    conexion.commit()
    cursor.close()
    conexion.close()


def obtener_id_clase(nombre_clase):
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()

    # Buscar el ID_Clase en la base de datos
    cursor.execute('''
        SELECT ID_Clase
        FROM CLASES
        WHERE Nombre_Clase = ?
    ''', (nombre_clase,))
    resultado = cursor.fetchone()

    # Si se encontró un registro, extraer el ID_Clase
    if resultado:
        clase_id = resultado[0]
    else:
        clase_id = None

    # Retornar el ID_Clase o None
    cursor.close()
    conexion.close()
    return clase_id

def obtener_json_clase(id_clase):
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()

    # Buscar el ID_Clase en la base de datos
    cursor.execute('''
        SELECT Datos_clase
        FROM CLASES
        WHERE ID_Clase = ?
    ''', (id_clase,))
    resultado = cursor.fetchone()

    # Si se encontró un registro, extraer el ID_Clase
    if resultado:
        datos = resultado[0]
    else:
        datos = None

    # Retornar el ID_Clase o None
    cursor.close()
    conexion.close()
    return datos

#!Hoja de WORD 3


def insertar_estudiante(documento_estudiante, nombre_estudiante, carrera_estudiante, clase_id):
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()

    # Preparar la sentencia SQL para insertar el estudiante
    cursor.execute('''
        INSERT INTO ESTUDIANTES (Documento_Estudiante, Nombre_Estudiante, Carrera_Estudiante, Clase_ID)
        VALUES (?, ?, ?, ?)
    ''', (documento_estudiante, nombre_estudiante, carrera_estudiante, clase_id))

    # Guardar los cambios en la base de datos
    conexion.commit()
    cursor.close()
    conexion.close()


def insertar_datos_biometricos(datos_biometricos, clase_id):
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()
    # Preparar la sentencia SQL para insertar los datos biométricos
    cursor.execute('''
        INSERT INTO DATOS_BIOMETRICOS (Datos_Biometricos, Clase_ID)
        VALUES (?, ?)
    ''', (datos_biometricos, clase_id))
    # Guardar los cambios en la base de datos
    conexion.commit()
    cursor.close()
    conexion.close()


def obtener_datos_biometricos(clase_id):
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()

    cursor.execute('''
        SELECT Datos_Biometricos
        FROM DATOS_BIOMETRICOS
        WHERE Clase_ID = ?
    ''', (clase_id,))
    resultado = cursor.fetchone()

    if resultado:
        datos_biometricos = resultado[0]
    else:
        datos_biometricos = None

    cursor.close()
    conexion.close()
    return datos_biometricos

#! Funciones de WhatsApp


def obtener_nombres_clases(profesor_id):
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()

    # Buscar los nombres de las clases del profesor
    cursor.execute('''
        SELECT Nombre_Clase
        FROM CLASES
        WHERE Profesor_ID = ?
    ''', (profesor_id,))
    resultado = cursor.fetchall()

    # Extraer los nombres de las clases del resultado
    nombres_clases = []
    for registro in resultado:
        nombres_clases.append(registro[0])

    # Retornar el array con los nombres de las clases
    cursor.close()
    conexion.close()
    return nombres_clases


def obtener_estudiante_por_posicion(clase_id, posicion):
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()

    # Buscar los datos del estudiante en la posición especificada
    cursor.execute('''
        SELECT Documento_Estudiante, Nombre_Estudiante, Carrera_Estudiante
        FROM ESTUDIANTES
        WHERE Clase_ID = ?
        ORDER BY ID_Estudiante
        LIMIT 1 OFFSET ? - 1
    ''', (clase_id, posicion))
    resultado = cursor.fetchone()

    # Extraer los datos del estudiante del resultado
    if resultado:
        estudiante = (resultado[0], resultado[1], resultado[2])
    else:
        estudiante = None

    # Retornar el array con los datos del estudiante o None si no se encuentra
    cursor.close()
    conexion.close()
    return estudiante


def obtener_estudiantes_de_una_clase(clase_id, estudiantes):
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()

    # Obtener la cantidad total de estudiantes en la clase
    cursor.execute(
        'SELECT COUNT(*) FROM ESTUDIANTES WHERE Clase_ID = ?', (clase_id,))
    total_estudiantes = cursor.fetchone()[0]

    # Recorrer los estudiantes de la clase y agregarlos a la lista
    for posicion in range(1, total_estudiantes + 1):
        estudiante = obtener_estudiante_por_posicion(clase_id, posicion)
        if estudiante:
            estudiantes.append(estudiante)

    # Retornar la lista de estudiantes actualizada
    cursor.close()
    conexion.close()
    return estudiantes


def eliminar_datos_por_clase_id(clase_id):
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()

    # Eliminar estudiantes de la clase especificada
    cursor.execute('DELETE FROM ESTUDIANTES WHERE Clase_ID = ?', (clase_id,))
    conexion.commit()  # Confirmar los cambios

    # Verificar si existen clases sin estudiantes
    cursor.execute(
        'SELECT COUNT(*) FROM CLASES WHERE ID_Clase NOT IN (SELECT Clase_ID FROM ESTUDIANTES)')
    clases_sin_estudiantes = cursor.fetchone()[0]

    if clases_sin_estudiantes:
        # Eliminar clases sin estudiantes
        cursor.execute(
            'DELETE FROM CLASES WHERE ID_Clase NOT IN (SELECT Clase_ID FROM ESTUDIANTES)')
        conexion.commit()

    # Cerrar la conexión a la base de datos
    cursor.close()
    conexion.close()


def editar_contrasena_profesor():
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()

    # Editar la contraseña del profesor
    cursor.execute(
        'UPDATE PROFESORES SET Contrasena = ? WHERE ID_Profesor = ?', ("123", 1))
    conexion.commit()  # Confirmar los cambios

    # Cerrar la conexión a la base de datos
    cursor.close()
    conexion.close()

# ? IMPORTANTE PARA PRESENTAR


def crear_profesor():
    conexion = sqlite3.connect('src/DataBase/BaseDeDatos.db')
    cursor = conexion.cursor()

    # Insertar los datos del nuevo profesor
    cursor.execute('INSERT INTO PROFESORES (Documento_Profesor, Contrasena, Nombre_Profesor) VALUES (?, ?, ?)',
                   (123, "123", "JP Admin"))
    conexion.commit()  # Confirmar los cambios

    # Cerrar la conexión a la base de datos
    cursor.close()
    conexion.close()
