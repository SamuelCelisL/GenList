import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout)
from PyQt6.QtGui import QFont
from PyQt6 import QtGui, QtCore
from login import generar_formulario_login


class inicio (QWidget):

    def __init__(self):
        super().__init__()
        self.InicializarUI()

    def InicializarUI(self):
        self.setGeometry(500, 100, 400, 150)
        self.setWindowTitle("Login GenList")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):

        font_titulo = QtGui.QFont()
        font_titulo.setBold(True)
        font_titulo.setFamily('sans-sarif')
        font_titulo.setPixelSize(30)

        titulo_inicial = QLabel("GenList")
        titulo_inicial.setFont(font_titulo)
        titulo_inicial.setAlignment(Qt.AlignmentFlag.AlignCenter)
        titulo_inicial.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        titulo_inicial.setStyleSheet('color: white')

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

        contenedor_principal = QVBoxLayout()
        widget_contenedor_principal = QWidget()
        widget_contenedor_principal.setStyleSheet("""QWidget{
                                    background-color: white;
                                    min-width: 500px;
                                    }""")
        widget_contenedor_principal.setLayout(contenedor_principal)

        # crear layaout
        contenedor_titulo = QHBoxLayout()
        # Cambiar el backgroud
        widget_contenedor_titulo = QWidget()
        diseño_titulo = """QWidget{background: qlineargradient(x1:0, y1:0, x2:0.707, y2:0.707, stop:0.1 rgba(46, 145, 221, 255),
            stop:0.4 rgba(40, 125, 190, 255),
            stop:0.6 rgba(33, 104, 158, 255));
            max-height: 55px;
            }"""
        widget_contenedor_titulo.setLayout(contenedor_titulo)
        widget_contenedor_titulo.setStyleSheet(diseño_titulo)

        # crear layaout
        # Parte de Registro
        contenedor_pre_registro = QHBoxLayout()
        self.widget_con_pre_registro = QWidget()
        self.widget_con_pre_registro.setLayout(contenedor_pre_registro)

        login_widget = generar_formulario_login(self)
        contenedor_pre_registro.addWidget(login_widget)

        # Parte Azul ↓
        contenedor_credito = QVBoxLayout()

        diseño_barra_F = """QWidget {
            background: qlineargradient(x1: 0, y1: 0, x2: 0.707, y2: 0.707, stop: 0.04 #45DC20, stop: 0.6 #179400);
            max-height: 110px;
        }"""
        widget_contenedor_credito = QWidget()
        widget_contenedor_credito.setLayout(contenedor_credito)
        widget_contenedor_credito.setStyleSheet(diseño_barra_F)

        # 1 ↓
        contenedor_titulo.addWidget(titulo_inicial)
        # 2 ↓

        # contenedor_registro.addLayout(contenedor_registro_c)

        contenedor_credito.addWidget(credito)
        contenedor_credito.addWidget(autor1)
        contenedor_credito.addWidget(autor2)
        contenedor_credito.addWidget(autor3)

        fondo = QVBoxLayout()
# Agregar los Qwidget a al Layout original
        contenedor_principal.addWidget(widget_contenedor_titulo)

        contenedor_principal.addWidget(self.widget_con_pre_registro)

        contenedor_principal.addWidget(widget_contenedor_credito)

# Agregar los layouts a al layoud original
        fondo.addWidget(widget_contenedor_principal)
        app.setStyle("Fusion")
        # Esta linea crea el primer layout ↓
        self.setLayout(fondo)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = inicio()
    sys.exit(app.exec())
