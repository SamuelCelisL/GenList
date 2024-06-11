from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout)
from PyQt6.QtGui import QPixmap, QIcon
from PyQt6 import QtCore


class crear_usuario(QWidget):

    def __init__(self, boton_volver_login, boton_crear_usuario, crear_usuario_input, crear_contra_input, confirmar_contra_input):
        super().__init__()
        self.setWindowTitle("Login GenList")
        self.setWindowIcon(QIcon('src/images/logo2.ico'))
        self.usuario(boton_volver_login, boton_crear_usuario,
                     crear_usuario_input, crear_contra_input, confirmar_contra_input)
        self.setGeometry(400, 200, 400, 300)
        self.show()

    def usuario(self, boton_volver_login, boton_crear_usuario, crear_usuario_input, crear_contra_input, confirmar_contra_input):

        # crear_usuario_input.text("")
        # crear_contra_input.text("")
        # confirmar_contra_input.text("")

        etiqueta_usuario = QLabel("Usuario")
        etiqueta_usuario.setStyleSheet("""QLabel{
                            color: black;
                            font-family: sans-serif;
                            font-weight: bold;
                            border: none;
                            max-width: 60px;
                        }""")

        crear_usuario_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        crear_usuario_input.setStyleSheet("""QLineEdit{
                            color: black;
                            font-family: sans-serif;
                            border: 1px solid black;
                            border-radius: 9px;
                            max-width: 300px;
                        }""")
        etiqueta_contraseña = QLabel("Contraseña")
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
                            max-width: 300px;
                        }""")
        etiqueta_confirmacion = QLabel("Confirma Contraseña")
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
                            max-width: 300px;
                        }""")
        boton_volver_login.setStyleSheet("""
                    QPushButton {
                        background-color: #F75A50;
                        color: white;
                        border-radius: 5px;
                        padding: 1px;
                        font-size: 15px;
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

        boton_crear_usuario.setStyleSheet("""
                    QPushButton {
                        background-color: #0A6EB0;
                        color: white;
                        border-radius: 5px;
                        padding: 1px;
                        font-size: 15px;
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

        layout_fondo = QVBoxLayout()
        widget_layout_fondo = QWidget()
        widget_layout_fondo.setStyleSheet("""QWidget{
                                          background-color: white;
                                          }""")
        widget_layout_fondo.setLayout(layout_fondo)
        layout_form_usuario = QVBoxLayout()
        widget_layout_form_usuario = QWidget()
        widget_layout_form_usuario.setLayout(layout_form_usuario)

        layout_botones = QHBoxLayout()
        widget_layout_botones = QWidget()
        widget_layout_botones.setLayout(layout_botones)

        # todo Agregar elementos de formulario de crear
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

        layout_fondo.addWidget(widget_layout_form_usuario)
        layout_fondo.addWidget(widget_layout_botones)

        layout_inicial = QVBoxLayout()
        layout_inicial.addWidget(widget_layout_fondo)

        self.setLayout(layout_inicial)
