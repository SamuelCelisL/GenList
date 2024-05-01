from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout, QHBoxLayout, QScrollArea)
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore


def generar_cursos():
    # scroll = QScrollArea()
    # scroll.setWidgetResizable(True)  # Hacer el widget interno redimensionable
    # scroll.setHorizontalScrollBarPolicy(
    #     QtCore.Qt.ScrollBarPolicy.ScrollBarAsNeeded)
    # scroll.setVerticalScrollBarPolicy(
    #     QtCore.Qt.ScrollBarPolicy.ScrollBarAlwaysOff)
    # scroll.setStyleSheet("""QWidget{
    #                             background-color: #DBE5D9;
    #                             border: 1px solid black;
    #                             border-radius: 9px;
    #                             }""")

    materias = [
        "Sistemas Inteligentes AR",
        "Fundamentos de programacion paralela y distribuida AR",
        "ingenieria de Software I BR",
        "REDES BB",
        "Fundamentos AR",
        "Halo 2",
        "ER",
        "busca"
    ]
    contenedor_registro = QVBoxLayout()
    contenedor_registro.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
    widget_contenedor_registro = QWidget()
    widget_contenedor_registro.setLayout(contenedor_registro)
    widget_contenedor_registro.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 9px;
                                min-width: 800px;
                                max-height: 500px;
                                min-height: 500px;
                                margin: 1px 1px;
                                }""")

    for materia in materias:
        nombre_materia = QLabel(materia)
        nombre_materia.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        nombre_materia.setStyleSheet("""QLabel{
                        color: black;
                        font-family: sans-serif;
                        font-weight: bold;
                        border: none;
                        min-width: 400px;
                        max-height: 20px;
                        min-height: 20px;
                    }""")
        primer_materia = QHBoxLayout()
        widget_primer_materia = QWidget()
        widget_primer_materia.setLayout(primer_materia)
        widget_primer_materia.setStyleSheet("""QWidget{
                                    background-color: #FFFFFF;
                                    border: 1px solid black;
                                    border-radius: 2px;
                                    max-width: 780px;
                                    min-width: 780px; 
                                    max-height: 50px;
                                    min-height: 50px;
                                    margin: 1px 1px;
                                    }""")
        botonE, botonA = crear_botones()
        primer_materia.addWidget(
            nombre_materia, alignment=Qt.AlignmentFlag.AlignLeft)
        primer_materia.addWidget(botonE, alignment=Qt.AlignmentFlag.AlignRight)
        primer_materia.addWidget(botonA)
        contenedor_registro.addWidget(widget_primer_materia)

    # contenedor_registro.addWidget(widget_contenedor_registro)
    # scroll.setWidget(widget_contenedor_registro)
    # contenedor_registro.addWidget(scroll)
    # widget_contenedor_registro.setLayout(scrollArea)

    # nombre_materia = QLabel("Sistemas Inteligentes AR")
    # nombre_materia.setAttribute(
    #     QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
    # nombre_materia.setStyleSheet("""QLabel{
    #                     color: black;
    #                     font-family: sans-serif;
    #                     font-weight: bold;
    #                     border: none;
    #                     min-width: 400px;
    #                     max-height: 20px;
    #                     min-height: 20px;
    #                 }""")
    # nombre_materia2 = QLabel(
    #     "Fundamentos de programacion paralela y distribuida AR")
    # nombre_materia2.setAttribute(
    #     QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
    # nombre_materia2.setStyleSheet("""QLabel{
    #                     color: black;
    #                     font-family: sans-serif;
    #                     font-weight: bold;
    #                     border: none;
    #                     max-width: 400px;
    #                     min-width: 200px;
    #                     max-height: 20px;
    #                     min-height: 20px;
    #                 }""")

    # nombre_materia3 = QLabel(
    #     "ingenieria de Software I BR")
    # nombre_materia3.setAttribute(
    #     QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
    # nombre_materia3.setStyleSheet("""QLabel{
    #                     color: black;
    #                     font-family: sans-serif;
    #                     font-weight: bold;
    #                     border: none;
    #                     max-width: 400px;
    #                     min-width: 200px;
    #                     max-height: 20px;
    #                     min-height: 20px;
    #                 }""")

    # primer_materia = QHBoxLayout()
    # widget_primer_materia = QWidget()
    # widget_primer_materia.setLayout(primer_materia)
    # widget_primer_materia.setStyleSheet("""QWidget{
    #                             background-color: #FFFFFF;
    #                             border: 1px solid black;
    #                             border-radius: 2px;
    #                             max-width: 780px;
    #                             min-width: 780px;
    #                             max-height: 50px;
    #                             min-height: 50px;
    #                             margin: 1px 1px;
    #                             }""")

    # segunda_materia = QHBoxLayout()
    # widget_segunda_materia = QWidget()
    # widget_segunda_materia.setLayout(segunda_materia)
    # widget_segunda_materia.setStyleSheet("""QWidget{
    #                             background-color: #FFFFFF;
    #                             border: 1px solid black;
    #                             border-radius: 2px;
    #                             max-width: 780px;
    #                             min-width: 780px;
    #                             max-height: 50px;
    #                             min-height: 50px;
    #                             margin: 1px 1px;
    #                             }""")

    # tercera_materia = QHBoxLayout()
    # widget_tercera_materia = QWidget()
    # widget_tercera_materia.setLayout(tercera_materia)
    # widget_tercera_materia.setStyleSheet("""QWidget{
    #                             background-color: #FFFFFF;
    #                             border: 1px solid black;
    #                             border-radius: 2px;
    #                             max-width: 780px;
    #                             min-width: 780px;
    #                             max-height: 50px;
    #                             min-height: 50px;
    #                             margin: 1px 1px;
    #                             }""")

    # botonE, botonA = crear_botones()
    # botonE1, botonA1 = crear_botones()
    # botonE2, botonA2 = crear_botones()

    # primer_materia.addWidget(
    #     nombre_materia, alignment=Qt.AlignmentFlag.AlignLeft)
    # primer_materia.addWidget(botonE1, alignment=Qt.AlignmentFlag.AlignRight)
    # primer_materia.addWidget(botonA1)

    # segunda_materia.addWidget(
    #     nombre_materia2, alignment=Qt.AlignmentFlag.AlignLeft)
    # segunda_materia.addWidget(botonE, alignment=Qt.AlignmentFlag.AlignRight)
    # segunda_materia.addWidget(botonA)

    # tercera_materia.addWidget(
    #     nombre_materia3, alignment=Qt.AlignmentFlag.AlignLeft)
    # tercera_materia.addWidget(botonE2, alignment=Qt.AlignmentFlag.AlignRight)
    # tercera_materia.addWidget(botonA2)

    # Agregar los widget de cada materia ↓
    # contenedor_registro.addWidget(widget_primer_materia)
    # contenedor_registro.addWidget(widget_segunda_materia)
    # contenedor_registro.addWidget(widget_tercera_materia)
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
                    max-width: 100px;
                    max-height: 20px;
                    min-height: 20px;
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
                    max-width: 100px;
                    max-height: 20px;
                    min-height: 20px;
                }
                QPushButton:hover {
                    background-color: #555555;
                }
                QPushButton:pressed {
                    background-color: #222222;
                }
            """)
    return boton_editar, boton_asistencia


if __name__ == '__main__':
    pass
