from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QVBoxLayout)
from PyQt6.QtGui import QPixmap
from PyQt6 import QtCore


def generar_formulario_login(boton_registrar, usuario_input, Contra_input, boton_crear_usuario):
    empresa = QPixmap('src/images/logo2Png.png')

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
        "Escribe tu usuario(Documento)")

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
                    background: qlineargradient(x1:0, y1:0, x2:0.707, y2:0.707, stop:0.1 rgba(46, 145, 221, 255),
                    stop:0.4 rgba(40, 125, 190, 255),
                    stop:0.6 rgba(33, 104, 158, 255));
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
    espacio = QLabel()
    espacio.setAlignment(Qt.AlignmentFlag.AlignCenter)
    espacio.setStyleSheet("""QLabel{
                        border: none;
                        max-width: 60px;
                    }""")
    espacio2 = QLabel()
    espacio2.setAlignment(Qt.AlignmentFlag.AlignCenter)
    espacio2.setStyleSheet("""QLabel{
                        border: none;
                        max-width: 60px;
                    }""")
    pregunta_registro = QLabel("¿Aun no te haz registrado?")
    pregunta_registro.setAlignment(Qt.AlignmentFlag.AlignCenter)
    pregunta_registro.setStyleSheet("""QLabel{
                        color: black;
                        font-family: sans-serif;
                        font-weight: bold;
                        border: none;
                        max-width: 60px;
                    }""")
    boton_crear_usuario.setStyleSheet("""
                QPushButton {
                    background: qlineargradient(x1: 0, y1: 0, x2: 0.707, y2: 0.707, stop: 0.04 #45DC20, stop: 0.6 #179400);
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
        espacio, alignment=Qt.AlignmentFlag.AlignCenter)
    contenedor_registro.addWidget(
        usuario_label, alignment=Qt.AlignmentFlag.AlignCenter)
    contenedor_registro.addWidget(
        usuario_input)
    contenedor_registro.addWidget(
        Contra_label)
    contenedor_registro.addWidget(
        Contra_input)
    contenedor_registro.addWidget(
        espacio2, alignment=Qt.AlignmentFlag.AlignCenter)
    contenedor_registro.addWidget(
        boton_registrar, alignment=Qt.AlignmentFlag.AlignCenter)
    # contenedor_registro.addWidget(
    #     espacio2, alignment=Qt.AlignmentFlag.AlignCenter)
    contenedor_registro.addWidget(
        pregunta_registro, alignment=Qt.AlignmentFlag.AlignCenter)
    contenedor_registro.addWidget(
        boton_crear_usuario, alignment=Qt.AlignmentFlag.AlignCenter)

    return widget_contenedor_registro


# if __name__ == '__main__':
#     pass
