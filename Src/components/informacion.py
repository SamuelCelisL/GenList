from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout)
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore


def generar_cursos():
    contenedor_registro = QVBoxLayout()
    contenedor_registro.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
    widget_contenedor_registro = QWidget()
    widget_contenedor_registro.setLayout(contenedor_registro)
    widget_contenedor_registro.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 9px;
                                max-width: 800px;
                                min-width: 800px;
                                margin: 1px 1px;
                                }""")
    nombre_materia = QLabel("Sistemas Inteligentes AR")
    nombre_materia.setStyleSheet("""QLabel{
                        background-color: red;
                        color: black;
                        font-family: sans-serif;
                        font-weight: bold;
                        border: none;
                        max-width: 10px;
                    }""")
    nombre_materia2 = QLabel(
        "Fundamentos de programacion paralela y distribuida AR")
    nombre_materia2.setStyleSheet("""QLabel{
                        background-color: red;
                        color: black;
                        font-family: sans-serif;
                        font-weight: bold;
                        border: none;
                        max-width: 100px;
                    }""")

    nombre_materia3 = QLabel(
        "ingenieria de Software I BR")
    nombre_materia3.setStyleSheet("""QLabel{
                        background-color: red;
                        color: black;
                        font-family: sans-serif;
                        font-weight: bold;
                        border: none;
                        max-width: 100px;
                    }""")

    primer_materia = QHBoxLayout()
    widget_primer_materia = QWidget()
    widget_primer_materia.setLayout(primer_materia)
    widget_primer_materia.setStyleSheet("""QWidget{
                                background-color: #FFFFFF;
                                border: 1px solid black;
                                border-radius: 2px;
                                max-width: 750px;
                                min-width: 750px;
                                margin: 1px 1px;
                                }""")

    segunda_materia = QHBoxLayout()
    widget_segunda_materia = QWidget()
    widget_segunda_materia.setLayout(segunda_materia)
    widget_segunda_materia.setStyleSheet("""QWidget{
                                background-color: #FFFFFF;
                                border: 1px solid black;
                                border-radius: 2px;
                                max-width: 750px;
                                min-width: 750px;
                                margin: 1px 1px;
                                }""")

    tercera_materia = QHBoxLayout()
    widget_tercera_materia = QWidget()
    widget_tercera_materia.setLayout(tercera_materia)
    widget_tercera_materia.setStyleSheet("""QWidget{
                                background-color: #FFFFFF;
                                border: 1px solid black;
                                border-radius: 2px;
                                max-width: 750px;
                                min-width: 750px;
                                margin: 1px 1px;
                                }""")

    botonE, botonA = crear_botones()
    botonE1, botonA1 = crear_botones()
    botonE2, botonA2 = crear_botones()
    primer_materia.addWidget(nombre_materia)
    primer_materia.addWidget(botonE1)
    primer_materia.addWidget(botonA1)

    segunda_materia.addWidget(nombre_materia2)
    segunda_materia.addWidget(botonE)
    segunda_materia.addWidget(botonA)

    tercera_materia.addWidget(nombre_materia3)
    tercera_materia.addWidget(botonE2)
    tercera_materia.addWidget(botonA2)

    # Agregar los widget de cada materia ↓
    contenedor_registro.addWidget(widget_primer_materia)
    contenedor_registro.addWidget(widget_segunda_materia)
    contenedor_registro.addWidget(widget_tercera_materia)
    return widget_contenedor_registro


def crear_botones():
    boton_editar = QPushButton("Editar")
    boton_editar.setStyleSheet("""
                QPushButton {
                    background-color: #F75A50;
                    color: white;
                    border-radius: 5px;
                    padding: 5px;
                    font-size: 10px;
                    font-weight: bold;
                    min-width: 100px;
                }
                QPushButton:hover {
                    background-color: #555555;
                }
                QPushButton:pressed {
                    background-color: #222222;
                }
            """)
    boton_asistencia = QPushButton("Asistencia")
    boton_asistencia.setStyleSheet("""
                QPushButton {
                    background-color: #0A6EB0;
                    color: white;
                    border-radius: 5px;
                    padding: 5px;
                    font-size: 10px;
                    font-weight: bold;
                    min-width: 100px;
                }
                QPushButton:hover {
                    background-color: #555555;
                }
                QPushButton:pressed {
                    background-color: #222222;
                }
            """)
    return boton_editar, boton_asistencia
