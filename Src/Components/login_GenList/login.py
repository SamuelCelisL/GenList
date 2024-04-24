import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QApplication, QWidget, QLabel, QLineEdit,
                             QPushButton, QHBoxLayout, QVBoxLayout)
from PyQt6.QtGui import QPixmap, QFont


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

        # prendia ajustar la imagen al Label ↓
        # Etiqueta_imagen.setScaledContents(True)
        # Etiqueta_imagen.setPixmap(QPixmap(escudoUP))
        # escudoUP = QPixmap('escudounipamplona.png')
        empresa = QPixmap('Src/Images/LogoempresaA.png')
        Etiqueta_imagen = QLabel()
        imagen_renden = empresa.scaledToWidth(150)
        Etiqueta_imagen.setPixmap(imagen_renden)
        Etiqueta_imagen.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Etiqueta_imagen.setStyleSheet("border: none;")

        Titulo_inicial = QLabel("GenList")
        Titulo_inicial.setFont(QFont('Times New Roman', 30))
        Titulo_inicial.setAlignment(Qt.AlignmentFlag.AlignCenter)
        Titulo_inicial.setStyleSheet('color: white')

        usuario_label = QLabel("USUARIO")
        usuario_label.setFixedWidth(60)
        usuario_label.setStyleSheet("border: none;")
        self.usuario_input = QLineEdit()
        self.usuario_input.setFixedWidth(300)
        self.usuario_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        Contra_label = QLabel("CONTRASEÑA")
        Contra_label.setFixedWidth(80)
        Contra_label.setStyleSheet("border: none;")
        self.Contra_input = QLineEdit()
        self.Contra_input.setFixedWidth(300)
        self.Contra_input.setEchoMode(QLineEdit.EchoMode.Password)
        self.Contra_input.setAlignment(Qt.AlignmentFlag.AlignCenter)

        cretido = QLabel("Desarrollado por:")
        cretido.setAlignment(Qt.AlignmentFlag.AlignCenter)
        cretido.setFont(QFont('Times New Roman', 20))
        cretido.setStyleSheet('color: white')

        autor1 = QLabel("Juan Pablo Marquez Sanchez")
        autor1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        autor1.setFont(QFont('Times New Roman', 10))
        autor1.setStyleSheet('color: white')
        autor2 = QLabel("Samuel Andres Celis Lizcano")
        autor2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        autor2.setFont(QFont('Times New Roman', 10))
        autor2.setStyleSheet('color: white')
        autor3 = QLabel("Yorman Rodolfo Rodriguez Jaimes")
        autor3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        autor3.setFont(QFont('Times New Roman', 10))
        autor3.setStyleSheet('color: white')

        boton_registrar = QPushButton("REGISTRAR")
        # boton_registrar.setStyleSheet("color: rgb(218,218,218);")
        boton_registrar.setFixedWidth(150)
        boton_registrar.setStyleSheet("background-color: #F75A50;")

        Horizontal_layaout_main = QVBoxLayout()

        # crear layaout
        h_layaout_1 = QHBoxLayout()
        # Cambiar el backgroud
        w_h_layaout_1 = QWidget()
        w_h_layaout_1.setLayout(h_layaout_1)
        w_h_layaout_1.setStyleSheet("background-color: #F75A50;")

        # crear layaout
        # Parte de Registro
        v_layaout_2 = QVBoxLayout()
        w_v_layaout_2 = QWidget()
        w_v_layaout_2.setLayout(v_layaout_2)
        w_v_layaout_2.setStyleSheet("background-color: transparent;")
        w_v_layaout_2.setStyleSheet("border: 1px solid black;")
        w_v_layaout_2.setGeometry(0, 0, 400, 500)

        h_layaout_2_1 = QHBoxLayout()
        h_layaout_2_2 = QHBoxLayout()
        h_layaout_2_3 = QHBoxLayout()
        h_layaout_2_4 = QHBoxLayout()
        h_layaout_2_5 = QHBoxLayout()
        # Parte Azul ↓
        v_layaout_3 = QVBoxLayout()
        w_v_layaout_3 = QWidget()
        w_v_layaout_3.setLayout(v_layaout_3)
        w_v_layaout_3.setStyleSheet("background-color: #0A6EB0;")
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
        # v_layaout_2.addWidget(
        #     boton_registrar, alignment=Qt.AlignmentFlag.AlignCenter)

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
        Horizontal_layaout_main.addWidget(
            boton_registrar, alignment=Qt.AlignmentFlag.AlignCenter)
        Horizontal_layaout_main.addWidget(w_v_layaout_3)
        # Horizontal_layaout_main.addLayout(v_layaout_3)
        app.setStyle("Fusion")
        self.setLayout(Horizontal_layaout_main)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = login()
    sys.exit(app.exec())
