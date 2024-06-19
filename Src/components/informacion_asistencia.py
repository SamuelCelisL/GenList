from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QVBoxLayout, QHBoxLayout)
from PyQt6.QtGui import QPixmap, QIcon, QIntValidator


class informacion_asistencia_clase(QWidget):

    def __init__(self, boton_volver_cursos, boton_empezar_reconocimiento, aula_input, tema_input):
        super().__init__()
        self.setWindowTitle("Asistencia GenList")
        self.setWindowIcon(QIcon('src/images/logo2.ico'))
        self.informacion_clase(boton_volver_cursos, boton_empezar_reconocimiento,
                               aula_input, tema_input)
        self.setGeometry(480, 200, 300, 280)
        self.show()

    def informacion_clase(self, boton_volver_cursos, boton_empezar_reconocimiento, aula_input, tema_input):

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

        etiqueta_aula = QLabel("Aula")
        etiqueta_aula.setAlignment(Qt.AlignmentFlag.AlignCenter)
        etiqueta_aula.setStyleSheet("""QLabel{
                            color: black;
                            font-family: sans-serif;
                            font-weight: bold;
                            border: none;
                            max-width: 60px;
                        }""")

        aula_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        aula_input.setStyleSheet("""QLineEdit{
                            color: black;
                            font-family: sans-serif;
                            border: 1px solid black;
                            border-radius: 9px;
                            min-width: 100px;
                            max-width: 100px;
                        }""")
        aula_input.setPlaceholderText(
            "GM 208-1")

        etiqueta_tema = QLabel("Tema")
        etiqueta_tema.setAlignment(Qt.AlignmentFlag.AlignCenter)
        etiqueta_tema.setStyleSheet("""QLabel{
                            color: black;
                            font-family: sans-serif;
                            font-weight: bold;
                            border: none;
                            max-width: 60px;
                        }""")

        tema_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        tema_input.setStyleSheet("""QLineEdit{
                            color: black;
                            font-family: sans-serif;
                            border: 1px solid black;
                            border-radius: 9px;
                            min-width: 180px;
                            max-width: 180px;
                        }""")
        tema_input.setPlaceholderText(
            "Ejemplo: Tema I")

        boton_volver_cursos.setStyleSheet("""
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

        boton_empezar_reconocimiento.setStyleSheet("""
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
            etiqueta_aula, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_form_usuario.addWidget(
            aula_input, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_form_usuario.addWidget(
            etiqueta_tema, alignment=Qt.AlignmentFlag.AlignCenter)
        layout_form_usuario.addWidget(
            tema_input, alignment=Qt.AlignmentFlag.AlignCenter)

        # todo agregar botones de movimiento
        layout_botones.addWidget(
            boton_volver_cursos, alignment=Qt.AlignmentFlag.AlignLeft)
        layout_botones.addWidget(
            boton_empezar_reconocimiento, alignment=Qt.AlignmentFlag.AlignRight)

        layout_fondo.addWidget(widget_layout_form_usuario,
                               alignment=Qt.AlignmentFlag.AlignCenter)
        layout_fondo.addWidget(widget_layout_botones)

        layout_inicial = QVBoxLayout()
        layout_inicial.addWidget(widget_layout_fondo)

        self.setLayout(layout_inicial)
