from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout)
from PyQt6.QtGui import QPixmap, QIcon, QIntValidator
from PyQt6 import QtCore


class crear_usuario(QWidget):

    def __init__(self, boton_volver_login, boton_crear_usuario, crear_usuario_input, crear_contra_input, confirmar_contra_input, nombre_usuario_input):
        super().__init__()
        self.setWindowTitle("Crear Usuario GenList")
        self.setWindowIcon(QIcon('src/images/logo2.ico'))
        self.usuario(boton_volver_login, boton_crear_usuario,
                     crear_usuario_input, crear_contra_input, confirmar_contra_input, nombre_usuario_input)
        self.setGeometry(580, 200, 400, 380)
        self.show()

    def usuario(self, boton_volver_login, boton_crear_usuario, crear_usuario_input, crear_contra_input, confirmar_contra_input, nombre_usuario_input):

        layout_form_usuario = QVBoxLayout()
        widget_layout_form_usuario = QWidget()
        widget_layout_form_usuario.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 9px;
                                max-width: 300px;
                                min-width: 200px;
                                margin: 1px 1px;
                                }""")
        Logo = QPixmap('src/images/logo2Png.png')

        etiqueta_imagen = QLabel()
        imagen_renden = Logo.scaledToWidth(50)
        etiqueta_imagen.setPixmap(imagen_renden)
        etiqueta_imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        etiqueta_imagen.setStyleSheet("border: none;")

        etiqueta_nombre_usuario = QLabel("Nombre de Usuario")
        etiqueta_nombre_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        etiqueta_nombre_usuario.setStyleSheet("""QLabel{
                            color: black;
                            font-family: sans-serif;
                            font-weight: bold;
                            border: none;
                            max-width: 60px;
                        }""")

        nombre_usuario_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        nombre_usuario_input.setStyleSheet("""QLineEdit{
                            color: black;
                            font-family: sans-serif;
                            border: 1px solid black;
                            border-radius: 9px;
                            min-width: 180px;
                            max-width: 180px;
                        }""")
        nombre_usuario_input.setPlaceholderText(
            "Ejemplo: Samuel Celis")

        etiqueta_usuario = QLabel("Documento")
        etiqueta_usuario.setAlignment(Qt.AlignmentFlag.AlignCenter)
        etiqueta_usuario.setStyleSheet("""QLabel{
                            color: black;
                            font-family: sans-serif;
                            font-weight: bold;
                            border: none;
                            max-width: 60px;
                        }""")

        int_validator = QIntValidator(0, 2147483647)
        crear_usuario_input.setValidator(int_validator)
        crear_usuario_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        crear_usuario_input.setStyleSheet("""QLineEdit{
                            color: black;
                            font-family: sans-serif;
                            border: 1px solid black;
                            border-radius: 9px;
                            min-width: 180px;
                            max-width: 180px;
                        }""")
        crear_usuario_input.setPlaceholderText(
            "Numero de Documento")
        etiqueta_contraseña = QLabel("Contraseña")
        etiqueta_contraseña.setAlignment(Qt.AlignmentFlag.AlignCenter)
        etiqueta_contraseña.setStyleSheet("""QLabel{
                            color: black;
                            font-family: sans-serif;
                            font-weight: bold;
                            border: none;
                            max-width: 100px;
                        }""")
        crear_contra_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        crear_contra_input.setStyleSheet("""QLineEdit{
                            color: black;
                            font-family: sans-serif;
                            border: 1px solid black;
                            border-radius: 9px;
                            min-width: 180px;
                            max-width: 180px;
                        }""")
        crear_contra_input.setEchoMode(QLineEdit.EchoMode.Password)
        crear_contra_input.setPlaceholderText(
            "Escribe tu Contraseña")
        etiqueta_confirmacion = QLabel("Confirma Contraseña")
        etiqueta_confirmacion.setAlignment(Qt.AlignmentFlag.AlignCenter)
        etiqueta_confirmacion.setStyleSheet("""QLabel{
                            color: black;
                            font-family: sans-serif;
                            font-weight: bold;
                            border: none;
                            max-width: 150px;
                        }""")
        confirmar_contra_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        confirmar_contra_input.setStyleSheet("""QLineEdit{
                            color: black;
                            font-family: sans-serif;
                            border: 1px solid black;
                            border-radius: 9px;
                            min-width: 180px;
                            max-width: 180px;
                        }""")
        confirmar_contra_input.setEchoMode(QLineEdit.EchoMode.Password)
        confirmar_contra_input.setPlaceholderText(
            "Confirma tu Contraseña")
        boton_volver_login.setStyleSheet("""
                    QPushButton {
                        background: qlineargradient(x1: 0, y1: 0, x2: 0.707, y2: 0.707, stop: 0.04 #B22222, stop: 0.6 #FF0000);
                        color: white;
                        border-radius: 5px;
                        padding: 1px;
                        font-size: 15px;
                        font-weight: bold;
                        min-width: 100px;
                        max-width: 100px;
                        max-height: 40px;
                        min-height: 40px;
                        border: 1px solid black;
                    }
                    QPushButton:hover {
                        background-color: #555555;
                    }
                    QPushButton:pressed {
                        background-color: #222222;
                    }
                """)

        boton_crear_usuario.setStyleSheet("""
                    QPushButton {
                        background: qlineargradient(x1:0, y1:0, x2:0.707, y2:0.707, stop:0.1 rgba(46, 145, 221, 255),
                    stop:0.4 rgba(40, 125, 190, 255),
                    stop:0.6 rgba(33, 104, 158, 255));
                        color: white;
                        border-radius: 5px;
                        padding: 1px;
                        font-size: 15px;
                        font-weight: bold;
                        min-width: 100px;
                        max-width: 100px;
                        max-height: 40px;
                        min-height: 40px;
                        border: 1px solid black;
                    }
                    QPushButton:hover {
                        background-color: #555555;
                    }
                    QPushButton:pressed {
                        background-color: #222222;
                    }
                """)

        layout_fondo = QVBoxLayout()
        widget_layout_fondo = QWidget()
        widget_layout_fondo.setStyleSheet("""QWidget{
                                          background-color: white;
                                          }""")
        widget_layout_fondo.setLayout(layout_fondo)
        widget_layout_form_usuario.setLayout(layout_form_usuario)

        layout_botones = QHBoxLayout()
        widget_layout_botones = QWidget()
        widget_layout_botones.setLayout(layout_botones)

        # todo Agregar elementos de formulario de crear
        layout_form_usuario.addWidget(
            etiqueta_imagen, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_form_usuario.addWidget(
            etiqueta_nombre_usuario, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_form_usuario.addWidget(
            nombre_usuario_input, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_form_usuario.addWidget(
            etiqueta_usuario, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_form_usuario.addWidget(
            crear_usuario_input, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_form_usuario.addWidget(
            etiqueta_contraseña, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_form_usuario.addWidget(
            crear_contra_input, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_form_usuario.addWidget(
            etiqueta_confirmacion, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_form_usuario.addWidget(
            confirmar_contra_input, alignment=Qt.AlignmentFlag.AlignCenter)

        # todo agregar botones de movimiento
        layout_botones.addWidget(
            boton_volver_login, alignment=Qt.AlignmentFlag.AlignLeft)
        layout_botones.addWidget(
            boton_crear_usuario, alignment=Qt.AlignmentFlag.AlignRight)

        layout_fondo.addWidget(widget_layout_form_usuario,
                               alignment=Qt.AlignmentFlag.AlignCenter)
        layout_fondo.addWidget(widget_layout_botones)

        layout_inicial = QVBoxLayout()
        layout_inicial.addWidget(widget_layout_fondo)

        self.setLayout(layout_inicial)
