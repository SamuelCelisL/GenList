import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QMessageBox)
from PyQt6.QtGui import QFont
from PyQt6 import QtGui, QtCore
from components import login, informacion, datos_y_opciones, nuevo_curso


class inicio (QWidget):

    def __init__(self):
        super().__init__()
        self.InicializarUI()

    def InicializarUI(self):
        # self.setGeometry(500, 100, 400, 150)
        self.setWindowTitle("Login GenList")
        self.generar_formulario()
        self.show()

    def generar_formulario(self):

        self.usuarios = [['adminSamuel', 'adminSamuel'], [
            'adminMarquez', 'adminMarquez'], ['adminYorman', 'adminYorman']]

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
        self.contenedor_pre_pre_registro = QHBoxLayout()
        self.widget_contenedor_pre_pre_registro = QWidget()
        self.widget_contenedor_pre_pre_registro.setLayout(
            self.contenedor_pre_pre_registro)

        self.contenedor_pre_registro = QVBoxLayout()
        self.widget_con_pre_registro = QWidget()
        self.widget_con_pre_registro.setLayout(self.contenedor_pre_registro)

        self.contenedor_pre_registro.addWidget(
            self.widget_contenedor_pre_pre_registro)

        # CAMBIO DE PANTALLA CENTRAL
        self.boton_registrar = QPushButton("REGISTRAR")
        self.usuario_input = QLineEdit()
        self.Contra_input = QLineEdit()
        self.login_widget = login.generar_formulario_login(
            self.boton_registrar, self.usuario_input, self.Contra_input)

        self.contenedor_pre_pre_registro.addWidget(
            self.login_widget)
        self.mensaje_emergente = QMessageBox()
        self.boton_registrar.clicked.connect(self.haz_dado_click)
        # self.boton_registrar.clicked.connect(self.cambiar_pantalla)

        # Creacion de botones de cerrar sesion y crear curso
        self.boton_cerrar = QPushButton("Cerrar Sesion")
        self.boton_cerrar.clicked.connect(self.volver_inicio)
        self.boton_crear_curso = QPushButton("Crear Curso")
        self.boton_crear_curso.clicked.connect(self.crear_curso)
        # Parte Azul ↓
        contenedor_credito = QVBoxLayout()

        diseño_barra_F = """QWidget {
            background: qlineargradient(x1: 0, y1: 0, x2: 0.707, y2: 0.707, stop: 0.04 #45DC20, stop: 0.6 #179400);
            max-height: 110px;
        }"""
        # 110;
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

    def haz_dado_click(self):
        usuario = []
        aprobacion = False
        usuario.append(self.usuario_input.text())
        usuario.append(self.Contra_input.text())
        # print(usuario)
        aprobacion = self.validiar_usuario(usuario)
        if aprobacion is None:
            self.Contra_input.clear()
        else:
            if aprobacion is True:
                self.usuario_input.clear()
                self.Contra_input.clear()
                usuario.clear()
                # print(usuario)
                self.cambiar_pantalla()
            else:
                self.mensaje_emergente.setWindowTitle("Mensaje de ERROR")
                self.mensaje_emergente.setText("Datos Incorrectos.")
                self.mensaje_emergente.setIcon(QMessageBox.Icon.Warning)
                self.mensaje_emergente.exec()
                self.usuario_input.clear()
                self.Contra_input.clear()

    def validiar_usuario(self, usuario):
        for i, sublist in enumerate(self.usuarios):
            if sublist[0] == usuario[0]:
                if sublist[1] == usuario[1]:
                    aprobacion = True
                    return aprobacion
                else:
                    self.mensaje_emergente.setWindowTitle("Mensaje de ERROR")
                    self.mensaje_emergente.setText("Contraseña Incorrecta.")
                    self.mensaje_emergente.setIcon(
                        QMessageBox.Icon.Warning)
                    self.mensaje_emergente.exec()
                    aprobacion = None
                    return aprobacion
            else:
                aprobacion = False

        return aprobacion

    def cambiar_pantalla(self):
        self.contenedor_pre_pre_registro.removeWidget(self.login_widget)
        self.login_widget.hide()
        self.widget_contenedor_pre_pre_registro.hide()
        self.informacion_widget = informacion.generar_cursos()
        self.contenedor_pre_registro.addWidget(
            self.informacion_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.datos_y_opc_widget = datos_y_opciones.generar_espacio_datos(
            self.boton_cerrar, self.boton_crear_curso)
        self.contenedor_pre_registro.addWidget(
            self.datos_y_opc_widget, alignment=Qt.AlignmentFlag.AlignCenter)

    def volver_inicio(self):
        self.contenedor_pre_pre_registro.removeWidget(self.informacion_widget)
        self.informacion_widget.hide()
        self.contenedor_pre_pre_registro.removeWidget(self.datos_y_opc_widget)
        self.datos_y_opc_widget.hide()
        self.login_widget.show()
        # self.contenedor_pre_pre_registro.removeWidget(self.cursos_widget)
        # self.cursos_widget.hide()
        self.widget_contenedor_pre_pre_registro.show()
        self.contenedor_pre_pre_registro.addWidget(self.login_widget)

    def crear_curso(self):
        self.contenedor_pre_pre_registro.removeWidget(self.informacion_widget)
        self.informacion_widget.hide()
        self.contenedor_pre_pre_registro.removeWidget(self.datos_y_opc_widget)
        self.datos_y_opc_widget.hide()
        self.cursos_widget = nuevo_curso.generar_llenado_curso()
        self.contenedor_pre_registro.addWidget(
            self.cursos_widget, alignment=Qt.AlignmentFlag.AlignCenter)
        self.datos_y_opc_widget = datos_y_opciones.generar_espacio_datos(
            self.boton_cerrar, self.boton_crear_curso)
        self.contenedor_pre_registro.addWidget(
            self.datos_y_opc_widget, alignment=Qt.AlignmentFlag.AlignCenter)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = inicio()
    sys.exit(app.exec())
