from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QPushButton, QHBoxLayout, QVBoxLayout, QTableWidget, QTableWidgetItem)
from PyQt6 import QtCore


def generar_llenado_curso():

    contenedor_form_curso = QVBoxLayout()
    widget_contenedor_form_curso = QWidget()
    widget_contenedor_form_curso.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 8px;
                                min-width: 800px;
                                margin: 1px 1px;
                                max-height: 500px;
                                min-height: 500px;
                                }""")
    widget_contenedor_form_curso.setLayout(contenedor_form_curso)

    texto_informacion_materia = QLabel("Nombre del curso y grupo : ")
    texto_informacion_materia.setAttribute(
        QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
    texto_informacion_materia.setStyleSheet("""QLabel{
                                border: none;
                                font-family: sans-serif;
                                font-weight: bold;
                                color: black;
                                max-width: 80px;
                                max-height: 60px;
                                min-height: 60px;                                           
                                }""")
    materia_input = QLineEdit()
    materia_input.setStyleSheet("""QLineEdit{
                        color: black;
                        font-family: sans-serif;
                        border-radius: 8px;
                        border: 1px solid black;
                        max-height: 60px;
                        min-height: 60px;
    }""")
# Creacion de una tabla (estamos probando XD)
    tabla = QTableWidget(10, 3)
    tabla.setHorizontalHeaderLabels(
        ["Nombres y Apellidos", "Documento", "Carrera"])
    tabla.setColumnWidth(0, 200)
    tabla.setColumnWidth(1, 80)
    tabla.setColumnWidth(2, 100)

    contenedor_cabeza = QHBoxLayout()
    contenedor_cabeza.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeft)
    widget_contenedor_cabeza = QWidget()
    widget_contenedor_cabeza.setStyleSheet("""QWidget{
                                border: none;           
                                }""")
    widget_contenedor_cabeza.setLayout(contenedor_cabeza)

    # Agregar los elementos al primer layout
    contenedor_cabeza.addWidget(
        texto_informacion_materia, alignment=Qt.AlignmentFlag.AlignLeft)
    contenedor_cabeza.addWidget(
        materia_input)
    # Agregar los elementos al segundo layout

    # Agregar las cosas al layout principal que es el que se va a mostrar
    contenedor_form_curso.addWidget(widget_contenedor_cabeza)
    # contenedor_form_curso.addWidget(tabla)

    return widget_contenedor_form_curso
