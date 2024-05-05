from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QPushButton, QHBoxLayout, QVBoxLayout, QStackedLayout)
from PyQt6 import QtCore
from PyQt6.QtGui import QPixmap


def cuerpo_aplicacion():
    cambiador_de_pantalla = QStackedLayout()
    cambiador_de_pantalla.addWidget(generar_cursos)
    cambiador_de_pantalla.addWidget(generar_llenado_curso)


def generar_cursos(boton_cerrar, boton_crear_curso):
    general = QVBoxLayout()
    widget_general = QWidget()
    widget_general.setLayout(general)
    # Tenemos que agregar el Scroll
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

    general.addWidget(widget_contenedor_registro)
    general.addWidget(barra_botones_pag1(
        boton_cerrar, boton_crear_curso))
    return widget_general


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


def generar_llenado_curso(boton_cancelar, boton_agregar_estudiante, boton_finalzar):

    principal_pag2 = QVBoxLayout()
    widget_principal_pag2 = QWidget()
    widget_principal_pag2.setLayout(principal_pag2)

    contenedor_form_curso = QVBoxLayout()
    widget_contenedor_form_curso = QWidget()
    widget_contenedor_form_curso.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 8px;
                                margin: 1px 1px;
                                min-width: 800px;
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
                                max-width: 180px;
                                min-width: 180px;
                                max-height: 60px;
                                min-height: 60px;
                                }""")
    materia_input = QLineEdit()
    materia_input.setStyleSheet("""QLineEdit{
                        color: black;
                        font-family: sans-serif;
                        font-weight: bold;
                        border-radius: 8px;
                        border: 1px solid black;
                        min-height: 40px;
                        max-height: 40px;
                        max-width: 500px;
                        min-width: 500px;
    }""")
    contenedor_cabeza = QHBoxLayout()
    contenedor_cabeza.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
    widget_contenedor_cabeza = QWidget()
    widget_contenedor_cabeza.setStyleSheet("""QWidget{
                                min-width: 800px;
                                max-height: 80px;
                                min-height: 80px;
                                border: none;
                                }""")
    widget_contenedor_cabeza.setLayout(contenedor_cabeza)
    contenedor_cabeza.addWidget(
        texto_informacion_materia)
    contenedor_cabeza.addWidget(
        materia_input, alignment=Qt.AlignmentFlag.AlignLeft)

    contenedor_form_curso.addWidget(
        widget_contenedor_cabeza, alignment=Qt.AlignmentFlag.AlignTop)

    principal_pag2.addWidget(widget_contenedor_form_curso)
    principal_pag2.addWidget(barra_botones_pag2(
        boton_cancelar, boton_agregar_estudiante, boton_finalzar))
    return widget_principal_pag2


def barra_botones_pag1(boton_cerrar, boton_crear_curso):

    # Creacion de contenerdor de datos y acciones basicas
    contenedor_ayuda = QHBoxLayout()
    widget_contenedor_ayuda = QWidget()
    widget_contenedor_ayuda.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 8px;
                                min-width: 800px;
                                margin: 1px 1px;
                                max-height: 60px;
                                min-height: 60px;
                                }""")
    widget_contenedor_ayuda.setLayout(contenedor_ayuda)

    boton_cerrar.setFixedWidth(150)
    boton_cerrar.setStyleSheet("""
                QPushButton {
                    background-color: #444847;
                    color: white;
                    border-radius: 5px;
                    padding: 1px;
                    font-size: 10px;
                    font-weight: bold;
                    min-width: 100px;
                    max-width: 100px;
                    max-height: 40px;
                    min-height: 40px;
                }
                QPushButton:hover {
                    background-color: #555555;
                }
                QPushButton:pressed {
                    background-color: #222222;
                }
            """)

    boton_crear_curso.setFixedWidth(150)
    boton_crear_curso.setStyleSheet("""
                QPushButton {
                    background-color: #444847;
                    color: white;
                    border-radius: 5px;
                    padding: 1px;
                    font-size: 10px;
                    font-weight: bold;
                    min-width: 100px;
                    max-width: 100px;
                    max-height: 40px;
                    min-height: 40px;
                }
                QPushButton:hover {
                    background-color: #555555;
                }
                QPushButton:pressed {
                    background-color: #222222;
                }
            """)

    contenedor_ayuda.addWidget(
        boton_crear_curso, alignment=Qt.AlignmentFlag.AlignLeft)
    contenedor_ayuda.addWidget(
        boton_cerrar, alignment=Qt.AlignmentFlag.AlignRight)
    return widget_contenedor_ayuda


def barra_botones_pag2(boton_cancelar, boton_agregar_estudiante, boton_finalzar):

    # Creacion de contenerdor de datos y acciones basicas
    contenedor_ayuda = QHBoxLayout()
    widget_contenedor_ayuda = QWidget()
    widget_contenedor_ayuda.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 8px;
                                min-width: 800px;
                                margin: 1px 1px;
                                max-height: 60px;
                                min-height: 60px;
                                }""")
    widget_contenedor_ayuda.setLayout(contenedor_ayuda)

    boton_cancelar.setFixedWidth(150)
    boton_cancelar.setStyleSheet("""
                QPushButton {
                    background-color: #444847;
                    color: white;
                    border-radius: 5px;
                    padding: 1px;
                    font-size: 10px;
                    font-weight: bold;
                    min-width: 100px;
                    max-width: 100px;
                    max-height: 40px;
                    min-height: 40px;
                }
                QPushButton:hover {
                    background-color: #555555;
                }
                QPushButton:pressed {
                    background-color: #222222;
                }
            """)

    boton_agregar_estudiante.setFixedWidth(150)
    boton_agregar_estudiante.setStyleSheet("""
                QPushButton {
                    background-color: #444847;
                    color: white;
                    border-radius: 5px;
                    padding: 1px;
                    font-size: 10px;
                    font-weight: bold;
                    min-width: 100px;
                    max-width: 100px;
                    max-height: 40px;
                    min-height: 40px;
                }
                QPushButton:hover {
                    background-color: #555555;
                }
                QPushButton:pressed {
                    background-color: #222222;
                }
            """)

    boton_finalzar.setFixedWidth(150)
    boton_finalzar.setStyleSheet("""
                QPushButton {
                    background-color: #444847;
                    color: white;
                    border-radius: 5px;
                    padding: 1px;
                    font-size: 10px;
                    font-weight: bold;
                    min-width: 100px;
                    max-width: 100px;
                    max-height: 40px;
                    min-height: 40px;
                }
                QPushButton:hover {
                    background-color: #555555;
                }
                QPushButton:pressed {
                    background-color: #222222;
                }
            """)
    contenedor_ayuda.addWidget(
        boton_cancelar, alignment=Qt.AlignmentFlag.AlignLeft)
    contenedor_ayuda.addWidget(
        boton_agregar_estudiante, alignment=Qt.AlignmentFlag.AlignRight)
    contenedor_ayuda.addWidget(
        boton_finalzar, alignment=Qt.AlignmentFlag.AlignRight)

    return widget_contenedor_ayuda
