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

        empresa = QPixmap('Src/Images/LogoempresaA.png')
        font_neg = QtGui.QFont()
        font_neg.setBold(True)

        font_titulo = QtGui.QFont()
        font_titulo.setBold(True)
        font_titulo.setFamily('sans-sarif')
        font_titulo.setPixelSize(30)

        Etiqueta_imagen = QLabel()
        imagen_renden = empresa.scaledToWidth(150)
        Etiqueta_imagen.setPixmap(imagen_renden)
        Etiqueta_imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Etiqueta_imagen.setStyleSheet("")
        Etiqueta_imagen.setStyleSheet("border: none;")

        Titulo_inicial = QLabel("GenList")
        Titulo_inicial.setFont(font_titulo)
        Titulo_inicial.setFixedSize(150, 40)
        Titulo_inicial.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Titulo_inicial.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        Titulo_inicial.setStyleSheet('color: white')

        usuario_label = QLabel("USUARIO")

        # usuario_label.setFixedWidth(60)
        # usuario_label.setFont(QFont('sans-serif', False))
        # usuario_label.setFont(font_neg)
        usuario_label.setStyleSheet("""QLabel{
                    color: black;
                    font-family: sans-serif;
                    font-weight: bold;
                    width: 60px;
                    border: none;
                    max-width: 60px;
                }""")
        self.usuario_input = QLineEdit()
        self.usuario_input.setFixedWidth(300)
        self.usuario_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        Contra_label = QLabel("CONTRASEÑA")
        Contra_label.setFixedWidth(80)
        Contra_label.setStyleSheet("border: none;")
        Contra_label.setFont(font_neg)
        self.Contra_input = QLineEdit()
        self.Contra_input.setFixedWidth(300)
        self.Contra_input.setEchoMode(QLineEdit.EchoMode.Password)
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

        Horizontal_layaout_main = QVBoxLayout()

        # crear layaout
        h_layaout_1 = QHBoxLayout()
        # Cambiar el backgroud
        w_h_layaout_1 = QWidget()
        gradient_titulo = QtGui.QLinearGradient(0, 0, 0, 400)
        gradient_titulo.setColorAt(0.1, QtGui.QColor(46, 145, 221))
        gradient_titulo.setColorAt(0.4, QtGui.QColor(40, 125, 190))
        gradient_titulo.setColorAt(0.6, QtGui.QColor(33, 104, 158))
        diseño_titulo = """background: qlineargradient(x1:0, y1:0, x2:0, y2:1, stop:0.1 rgba(46, 145, 221, 255), 
            stop:0.4 rgba(40, 125, 190, 255), 
            stop:0.6 rgba(33, 104, 158, 255));"""
        w_h_layaout_1.setLayout(h_layaout_1)
        w_h_layaout_1.setStyleSheet(diseño_titulo)

        # crear layaout
        # Parte de Registro
        v_layaout_2 = QVBoxLayout()
        w_v_layaout_2 = QWidget()
        w_v_layaout_2.setLayout(v_layaout_2)
        w_v_layaout_2.setStyleSheet("border: 1px solid black;")
        w_v_layaout_2.setGeometry(0, 0, 400, 500)

        h_layaout_2_1 = QHBoxLayout()
        h_layaout_2_2 = QHBoxLayout()
        h_layaout_2_3 = QHBoxLayout()
        h_layaout_2_4 = QHBoxLayout()
        h_layaout_2_5 = QHBoxLayout()
        # Parte Azul ↓
        v_layaout_3 = QVBoxLayout()

        gradient_barra_F = QtGui.QLinearGradient(0, 0, 0, 400)
        gradient_barra_F.setColorAt(0.0, QtGui.QColor(33, 104, 158))
        gradient_barra_F.setColorAt(1.0, QtGui.QColor(0, 0, 0))
        diseño_barra_F = "background: qlineargradient(x1: 0, y1: 0, x2: 0, y2: 1, stop: 0 rgba(33, 104, 158, 255), stop: 1 rgba(0, 0, 0, 255))"

        w_v_layaout_3 = QWidget()
        w_v_layaout_3.setLayout(v_layaout_3)
        w_v_layaout_3.setStyleSheet(diseño_barra_F)
        h_layaout_3_1 = QHBoxLayout()
        h_layaout_3_2 = QHBoxLayout()
        h_layaout_3_3 = QHBoxLayout()
        h_layaout_3_4 = QHBoxLayout()

        # 1 ↓
        h_layaout_1.addWidget(Titulo_inicial)
        # 2 ↓
        h_layaout_2_1.addWidget(Etiqueta_imagen)
        h_layaout_2_2.addWidget(usuario_label)
        h_layaout_2_3.addWidget(self.usuario_input)
        h_layaout_2_4.addWidget(Contra_label)
        h_layaout_2_5.addWidget(self.Contra_input)
        # 1-#↓
        h_layaout_3_1.addWidget(cretido)
        h_layaout_3_2.addWidget(autor1)
        h_layaout_3_3.addWidget(autor2)
        h_layaout_3_4.addWidget(autor3)

        v_layaout_2.addLayout(h_layaout_2_1)
        v_layaout_2.addLayout(h_layaout_2_2)
        v_layaout_2.addLayout(h_layaout_2_3)
        v_layaout_2.addLayout(h_layaout_2_4)
        v_layaout_2.addLayout(h_layaout_2_5)
        v_layaout_2.addWidget(
            boton_registrar, alignment=Qt.AlignmentFlag.AlignCenter)

        # v_layaout_2.addLayout(v_layaout_2_c)

        v_layaout_3.addLayout(h_layaout_3_1)
        v_layaout_3.addLayout(h_layaout_3_2)
        v_layaout_3.addLayout(h_layaout_3_3)
        v_layaout_3.addLayout(h_layaout_3_4)

# Agregar los layouts a al layoud original
        Horizontal_layaout_main.addWidget(w_h_layaout_1)
        # Horizontal_layaout_main.addLayout(h_layaout_1)
        Horizontal_layaout_main.addWidget(w_v_layaout_2)
        # Horizontal_layaout_main.addLayout(v_layaout_2)
        # Horizontal_layaout_main.addWidget(
        #     boton_registrar, alignment=Qt.AlignmentFlag.AlignCenter)
        Horizontal_layaout_main.addWidget(w_v_layaout_3)
        # Horizontal_layaout_main.addLayout(v_layaout_3)
        app.setStyle("Fusion")
        self.setLayout(Horizontal_layaout_main)

    def registrar_usuario(self):
        print("HOLA MUNDO")


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = login()
    sys.exit(app.exec())
