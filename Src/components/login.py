from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QVBoxLayout)
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore


def generar_formulario_login(boton_registrar, usuario_input, Contra_input):
    empresa = QPixmap('src/images/LogoempresaA.png')

    etiqueta_imagen = QLabel()
    imagen_renden = empresa.scaledToWidth(150)
    etiqueta_imagen.setPixmap(imagen_renden)
    etiqueta_imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
    etiqueta_imagen.setStyleSheet("border: none;")

    usuario_label = QLabel("USUARIO")
    usuario_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    usuario_label.setStyleSheet("""QLabel{
                        color: black;
                        font-family: sans-serif;
                        font-weight: bold;
                        border: none;
                        max-width: 60px;
                    }""")
    usuario_input.setStyleSheet("""QLineEdit{
                        color: black;
                        font-family: sans-serif;
                        border: 1px solid black;
                        border-radius: 9px;
                        max-width: 200px;
                    }""")
    usuario_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
    usuario_input.setPlaceholderText(
        "Escribe tu usuario")

    Contra_label = QLabel("CONTRASEÑA")
    Contra_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    Contra_label.setStyleSheet("""QLabel{
                        color: black;
                        font-family: sans-serif;
                        font-weight: bold;
                        border: none;
                        max-width: 100px;
                    }""")

    Contra_input.setEchoMode(QLineEdit.EchoMode.Password)
    Contra_input.setStyleSheet("""QLineEdit{
                        color: black;
                        font-family: sans-serif;
                        border-radius: 9px;
                        border: 1px solid black;
                        max-width: 200px;
                    }""")
    Contra_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
    Contra_input.setPlaceholderText("Escribe tu contraseña")

    boton_registrar.setStyleSheet("""
                QPushButton {
                    background-color: #444847;
                    color: white;
                    border-radius: 5px;
                    padding: 5px;
                    font-size: 10px;
                    font-weight: bold;
                    min-width: 100px;
                    max-width: 100px;
                }
                QPushButton:hover {
                    background-color: #555555;
                }
                QPushButton:pressed {
                    background-color: #222222;
                }
            """)

    contenedor_registro = QVBoxLayout()
    contenedor_registro.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
    widget_contenedor_registro = QWidget()
    widget_contenedor_registro.setLayout(contenedor_registro)
    widget_contenedor_registro.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 9px;
                                max-width: 400px;
                                min-width: 200px;
                                margin: 1px 1px;
                                }""")
    contenedor_registro.addWidget(
        etiqueta_imagen)
    contenedor_registro.addWidget(
        usuario_label, alignment=Qt.AlignmentFlag.AlignCenter)
    contenedor_registro.addWidget(
        usuario_input)
    contenedor_registro.addWidget(
        Contra_label)
    contenedor_registro.addWidget(
        Contra_input)
    contenedor_registro.addWidget(
        boton_registrar, alignment=Qt.AlignmentFlag.AlignCenter)

    return widget_contenedor_registro


if __name__ == '__main__':
    pass
