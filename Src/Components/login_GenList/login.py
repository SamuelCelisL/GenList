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
        self.usuario_input.setFixedWidth(300)
        self.usuario_input.setStyleSheet("""QLineEdit{
                    color: black;
                    font-family: sans-serif;
                    border: 1px solid black;
                    max-width: 300px;
                }""")
        self.usuario_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

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
        self.Contra_input.setFixedWidth(300)
        self.Contra_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.Contra_input.setStyleSheet("""QLineEdit{
                    color: black;
                    font-family: sans-serif;
                    border: 1px solid black;
                    max-width: 300px;
                }""")
        self.Contra_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        cretido = QLabel("Desarrollado por:")
        cretido.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cretido.setFont(QFont('Times New Roman', 20))
        cretido.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        cretido.setStyleSheet('color: white')

        autor1 = QLabel("Juan Pablo Marquez Sanchez")
        autor1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        autor1.setFont(QFont('Times New Roman', 10))
        autor1.setStyleSheet('color: white')
        autor1.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        autor2 = QLabel("Samuel Andres Celis Lizcano")
        autor2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        autor2.setFont(QFont('Times New Roman', 10))
        autor2.setStyleSheet('color: white')
        autor2.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        autor3 = QLabel("Yorman Rodolfo Rodriguez Jaimes")
        autor3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        autor3.setFont(QFont('Times New Roman', 10))
        autor3.setStyleSheet('color: white')
        autor3.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)

        boton_registrar = QPushButton("REGISTRAR")
        boton_registrar.setObjectName("boton_ingresar")
        boton_registrar.setFixedWidth(150)
        boton_registrar.setStyleSheet("""
                    QPushButton {
                        background-color: #0074D9;
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
        # gradient_titulo = QtGui.QLinearGradient(0, 0, 0, 400)
        # gradient_titulo.setColorAt(0.1, QtGui.QColor(46, 145, 221))
        # gradient_titulo.setColorAt(0.4, QtGui.QColor(40, 125, 190))
        # gradient_titulo.setColorAt(0.6, QtGui.QColor(33, 104, 158))
        diseño_titulo = """background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0.1 rgba(46, 145, 221, 255), 
            stop:0.4 rgba(40, 125, 190, 255), 
            stop:0.6 rgba(33, 104, 158, 255));"""
        widget_contenedor_titulo.setLayout(contenedor_titulo)
        widget_contenedor_titulo.setStyleSheet(diseño_titulo)

        # crear layaout
        # Parte de Registro
        contenedor_registro = QVBoxLayout()
        widget_contenedor_registro = QWidget()
        widget_contenedor_registro.setLayout(contenedor_registro)
        widget_contenedor_registro.setStyleSheet("""QWidget{
                                    background-color: white;
                                    border: 1px solid black;
                                    }""")
        widget_contenedor_registro.setGeometry(0, 0, 400, 500)

        contenedor_logo = QHBoxLayout()
        contenedor_usuario = QHBoxLayout()
        contenedor_imput_usuario = QHBoxLayout()
        contenedor_contraseña = QHBoxLayout()
        contenedor_imput_contra = QHBoxLayout()
        # Parte Azul ↓
        contenedor_credito = QVBoxLayout()

        # gradient_barra_F = QtGui.QLinearGradient(0, 0, 0, 400)
        # gradient_barra_F.setColorAt(0.0, QtGui.QColor(33, 104, 158))
        # gradient_barra_F.setColorAt(1.0, QtGui.QColor(0, 0, 0))
        diseño_barra_F = "background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(33, 104, 158, 255), stop: 1 rgba(0, 0, 0, 255))"

        widget_contenedor_credito = QWidget()
        widget_contenedor_credito.setLayout(contenedor_credito)
        widget_contenedor_credito.setStyleSheet(diseño_barra_F)
        contenedor_texto_credito = QHBoxLayout()
        contenedor_autor1 = QHBoxLayout()
        contenedor_autor2 = QHBoxLayout()
        contenedor_autor3 = QHBoxLayout()

        # 1 ↓
        contenedor_titulo.addWidget(titulo_inicial)
        # 2 ↓
        contenedor_logo.addWidget(etiqueta_imagen)
        contenedor_usuario.addWidget(usuario_label)
        contenedor_imput_usuario.addWidget(self.usuario_input)
        contenedor_contraseña.addWidget(Contra_label)
        contenedor_imput_contra.addWidget(self.Contra_input)
        # 1-#↓
        contenedor_texto_credito.addWidget(cretido)
        contenedor_autor1.addWidget(autor1)
        contenedor_autor2.addWidget(autor2)
        contenedor_autor3.addWidget(autor3)

        contenedor_registro.addLayout(contenedor_logo)
        contenedor_registro.addLayout(contenedor_usuario)
        contenedor_registro.addLayout(contenedor_imput_usuario)
        contenedor_registro.addLayout(contenedor_contraseña)
        contenedor_registro.addLayout(contenedor_imput_contra)
        contenedor_registro.addWidget(
            boton_registrar, alignment=Qt.AlignmentFlag.AlignCenter)

        # contenedor_registro.addLayout(contenedor_registro_c)

        contenedor_credito.addLayout(contenedor_texto_credito)
        contenedor_credito.addLayout(contenedor_autor1)
        contenedor_credito.addLayout(contenedor_autor2)
        contenedor_credito.addLayout(contenedor_autor3)

        fondo = QVBoxLayout()
# Agregar los Qwidget a al Layout original
        contenedor_principal.addWidget(widget_contenedor_titulo)
        # contenedor_principal.addLayout(contenedor_titulo)
        contenedor_principal.addWidget(widget_contenedor_registro)
        # contenedor_principal.addLayout(contenedor_registro)
        # contenedor_principal.addWidget(
        #     boton_registrar, alignment=Qt.AlignmentFlag.AlignCenter)
        contenedor_principal.addWidget(widget_contenedor_credito)
        # contenedor_principal.addLayout(contenedor_credito)

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
