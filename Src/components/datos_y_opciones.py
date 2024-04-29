from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QPushButton, QVBoxLayout)
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore


def generar_espacio_datos(boton_cerrar, boton_crear_curso):
    usuario = QPixmap('src/images/logousuario.png')

    etiqueta_imagen_usuario = QLabel()
    etiqueta_imagen_usuario.setAttribute(
        QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
    imagen_renden = usuario.scaledToWidth(65)
    etiqueta_imagen_usuario.setPixmap(imagen_renden)
    etiqueta_imagen_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
    etiqueta_imagen_usuario.setStyleSheet("""QLabel{
                        border: none;
                        max-width: 85px;
                        min-width: 85px;
                        max-height: 60px;
                    }""")

    nombre_docente = QLabel("Jose Gerardo Chacon Rangel")
    # Creacion de contenerdor de datos y acciones basicas
    contenedor_ayuda = QVBoxLayout()
    widget_contenedor_ayuda = QWidget()
    widget_contenedor_ayuda.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 8px;
                                max-width: 400px;
                                min-width: 100px;
                                margin: 1px 1px;
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
                    min-width: 80px;
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
                    min-width: 80px;
                }
                QPushButton:hover {
                    background-color: #555555;
                }
                QPushButton:pressed {
                    background-color: #222222;
                }
            """)
    contenedor_ayuda.addWidget(
        etiqueta_imagen_usuario)
    contenedor_ayuda.addWidget(
        nombre_docente, alignment=Qt.AlignmentFlag.AlignCenter)
    contenedor_ayuda.addWidget(
        boton_crear_curso, alignment=Qt.AlignmentFlag.AlignCenter)
    contenedor_ayuda.addWidget(
        boton_cerrar, alignment=Qt.AlignmentFlag.AlignCenter)

    return widget_contenedor_ayuda


if __name__ == '__main__':
    pass
