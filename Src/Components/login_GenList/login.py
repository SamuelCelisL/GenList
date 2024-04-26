import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QHBoxLayout, QVBoxLayout)
from PyQt6.QtGui import QPixmap, QFont
from PyQt6 import QtGui, QtCore


class login (QWidget):

    def __init__(self):
        super().__init__()
        self.InicializarUI()

    def InicializarUI(self):
        self.setGeometry(100, 100, 400, 150)
        self.setWindowTitle("Login GenList")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):

        empresa = QPixmap('src/images/LogoempresaA.png')

        font_titulo = QtGui.QFont()
        font_titulo.setBold(True)
        font_titulo.setFamily('sans-sarif')
        font_titulo.setPixelSize(30)

        etiqueta_imagen = QLabel()
        imagen_renden = empresa.scaledToWidth(150)
        etiqueta_imagen.setPixmap(imagen_renden)
        etiqueta_imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        etiqueta_imagen.setStyleSheet("")
        etiqueta_imagen.setStyleSheet("border: none;")

        titulo_inicial = QLabel("GenList")
        titulo_inicial.setFont(font_titulo)
        titulo_inicial.setFixedSize(150, 40)
        titulo_inicial.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo_inicial.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        titulo_inicial.setStyleSheet('color: white')

        usuario_label = QLabel("USUARIO")
        usuario_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        usuario_label.setStyleSheet("""QLabel{
                    color: black;
                    font-family: sans-serif;
                    font-weight: bold;
                    border: none;
                    max-width: 60px;
                }""")
        self.usuario_input = QLineEdit()
        self.usuario_input.setStyleSheet("""QLineEdit{
                    color: black;
                    font-family: sans-serif;
                    border: 1px solid black;
                    border-radius: 9px;
                    max-width: 500px;
                }""")
        self.usuario_input.setFixedWidth(200)
        self.usuario_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.usuario_input.setPlaceholderText(
            "Escribe tu usuario")

        Contra_label = QLabel("CONTRASEÑA")
        Contra_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Contra_label.setFixedWidth(80)
        Contra_label.setStyleSheet("""QLabel{
                    color: black;
                    font-family: sans-serif;
                    font-weight: bold;
                    border: none;
                    max-width: 100px;
                }""")
        self.Contra_input = QLineEdit()
        self.Contra_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.Contra_input.setStyleSheet("""QLineEdit{
                    color: black;
                    font-family: sans-serif;
                    border-radius: 9px;
                    border: 1px solid black;
                    max-width: 500px;
                }""")
        self.Contra_input.setFixedWidth(200)
        self.Contra_input.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.Contra_input.setPlaceholderText("Escribe tu contraseña")

        stilo_credito = """QLabel{
                    color: white;
                    font-family: sans-serif;
                    font-weight: bold;
                    font-size: 20px;
        }"""
        credito = QLabel("Desarrollado por:")
        credito.setAlignment(Qt.AlignmentFlag.AlignCenter)
        credito.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        credito.setStyleSheet(stilo_credito)

        autor1 = QLabel("Juan Pablo Marquez Sanchez")
        autor1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        autor1.setFont(QFont('sans-serif', 10))
        autor1.setStyleSheet('color: white')
        autor1.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        autor2 = QLabel("Samuel Andres Celis Lizcano")
        autor2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        autor2.setFont(QFont('sans-serif', 10))
        autor2.setStyleSheet('color: white')
        autor2.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        autor3 = QLabel("Yorman Rodolfo Rodriguez Jaimes")
        autor3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        autor3.setFont(QFont('sans-serif', 10))
        autor3.setStyleSheet('color: white')
        autor3.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)

        boton_registrar = QPushButton("REGISTRAR")
        boton_registrar.setObjectName("boton_ingresar")
        boton_registrar.setFixedWidth(150)
        boton_registrar.setStyleSheet("""
                    QPushButton {
                        background-color: #444847;
                        color: white;
                        border-radius: 5px;
                        padding: 5px;
                        font-size: 10px;
                        font-weight: bold;
                    }
                    QPushButton:hover {
                        background-color: #555555;
                    }
                    QPushButton:pressed {
                        background-color: #222222;
                    }
                """)
        boton_registrar.clicked.connect(self.registrar_usuario)

        contenedor_principal = QVBoxLayout()
        widget_contenedor_principal = QWidget()
        widget_contenedor_principal.setStyleSheet("""QWidget{
                                    background-color: white;
                                    }""")
        widget_contenedor_principal.setLayout(contenedor_principal)

        # crear layaout
        contenedor_titulo = QHBoxLayout()
        # Cambiar el backgroud
        widget_contenedor_titulo = QWidget()
        diseño_titulo = """background: qlineargradient(x1:0, y1:0, x2:0.707, y2:0.707, stop:0.1 rgba(46, 145, 221, 255),
            stop:0.4 rgba(40, 125, 190, 255),
            stop:0.6 rgba(33, 104, 158, 255));"""
        widget_contenedor_titulo.setLayout(contenedor_titulo)
        widget_contenedor_titulo.setStyleSheet(diseño_titulo)

        # crear layaout
        # Parte de Registro
        contenedor_pre_registro = QHBoxLayout()
        widget_con_pre_registro = QWidget()
        widget_con_pre_registro.setLayout(contenedor_pre_registro)

        contenedor_registro = QVBoxLayout()
        widget_contenedor_registro = QWidget()
        widget_contenedor_registro.setLayout(contenedor_registro)
        widget_contenedor_registro.setStyleSheet("""QWidget{
                                    background-color: #DBE5D9;
                                    border: 1px solid black;
                                    border-radius: 5px;
                                    max-width: 400px;
                                    margin: 1px 1em;
                                    }""")
        contenedor_pre_registro.addWidget(widget_contenedor_registro)
        # Parte Azul ↓
        contenedor_credito = QVBoxLayout()

        diseño_barra_F = "background: qlineargradient(x1: 0, y1: 0, x2: 0.707, y2: 0.707, stop: 0.04 #45DC20, stop: 0.6 #179400)"

        widget_contenedor_credito = QWidget()
        widget_contenedor_credito.setLayout(contenedor_credito)
        widget_contenedor_credito.setStyleSheet(diseño_barra_F)

        # 1 ↓
        contenedor_titulo.addWidget(titulo_inicial)
        # 2 ↓
        contenedor_registro.addWidget(etiqueta_imagen)
        contenedor_registro.addWidget(
            usuario_label, alignment=Qt.AlignmentFlag.AlignCenter)
        contenedor_registro.addWidget(
            self.usuario_input, alignment=Qt.AlignmentFlag.AlignCenter)
        contenedor_registro.addWidget(
            Contra_label, alignment=Qt.AlignmentFlag.AlignCenter)
        contenedor_registro.addWidget(
            self.Contra_input, alignment=Qt.AlignmentFlag.AlignCenter)
        contenedor_registro.addWidget(
            boton_registrar, alignment=Qt.AlignmentFlag.AlignCenter)

        # contenedor_registro.addLayout(contenedor_registro_c)

        contenedor_credito.addWidget(credito)
        contenedor_credito.addWidget(autor1)
        contenedor_credito.addWidget(autor2)
        contenedor_credito.addWidget(autor3)

        fondo = QVBoxLayout()
# Agregar los Qwidget a al Layout original
        contenedor_principal.addWidget(widget_contenedor_titulo)

        contenedor_principal.addWidget(widget_con_pre_registro)

        contenedor_principal.addWidget(widget_contenedor_credito)

# Agregar los layouts a al layoud original
        fondo.addWidget(widget_contenedor_principal)
        app.setStyle("Fusion")
        # Esta linea crea el primer layout ↓
        self.setLayout(fondo)

    def registrar_usuario(self):
        print("HOLA MUNDO")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = login()
    sys.exit(app.exec())
