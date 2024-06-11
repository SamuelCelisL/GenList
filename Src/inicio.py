import cv2
import os
import numpy as np
import pickle
import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton,
    QLineEdit, QMessageBox, QSizePolicy, QScrollArea, QTableWidget, QHeaderView, QTableWidgetItem)
from PyQt6.QtGui import QFont, QIcon
from PyQt6 import QtWidgets, QtGui, QtCore
from components import login, conexcionBD
from components import capture_and_save
from components import train_model
from components import recognize


class inicio (QWidget):

    def __init__(self):
        super().__init__()

        self.timer = QtCore.QTimer(self)
        self.timer.timeout.connect(self.update_frame)
        self.cameraLabel = QtWidgets.QLabel()

        self.cap = None
        self.is_capturing = False
        self.is_recognizing = False
        self.model = None
        self.clf = None
        self.InicializarUI()

    def InicializarUI(self):
        screen = app.primaryScreen()
        self.ventana = screen.size()
        self.profesor_id = None
        self.clase_id = None
        self.estudiantes = []
        self.materia_asistencia = None
        self.setWindowTitle("Login GenList")
        self.setWindowIcon(QIcon('src/images/logo2.ico'))
        self.generar_formulario()
        self.showMaximized()
        self.show()

    #! Funcion de inicio de la aplicacion, en esta carga el LOGIN ↓↓↓
    def generar_formulario(self):

        # Creacion de los tamaños de los 3 LAYOUTS DE LA APLICACION
        altoT = (self.ventana.height())*0.08
        self.altoC = (self.ventana.height())*0.10

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

        tamaño_eqtiqueta_credito = int(self.altoC * 0.30)
        tamaño_fuente_credito = tamaño_eqtiqueta_credito - 8
        stilo_credito = f"""QLabel{{
                    background: red;
                    color: white;
                    font-family: sans-serif;
                    font-weight: bold;
                    font-size: {tamaño_fuente_credito}px;
                    min-height: {tamaño_eqtiqueta_credito}px;
                    max-height: {tamaño_eqtiqueta_credito}px;
        }}"""
        credito = QLabel("Desarrollado por:")
        credito.setAlignment(Qt.AlignmentFlag.AlignCenter)
        credito.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        credito.setStyleSheet(stilo_credito)

        tamaño_etiqueta_autor = int((self.altoC*0.30))
        tamaño_fuete_autores = int(tamaño_etiqueta_autor - 0.5)
        autor1 = QLabel("La Secta de Samuel ®")
        autor1.setAlignment(Qt.AlignmentFlag.AlignCenter)
        autor1.setStyleSheet(f"""QLabel{{
                    background: red;
                    color: white;
                    font-family: sans-serif;
                    font-style: oblique;
                    font-size: {tamaño_fuete_autores}px;
                    min-height: {tamaño_etiqueta_autor}px;
                    max-height: {tamaño_etiqueta_autor}px;
        }}""")
        autor1.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)

        contenedor_principal = QVBoxLayout()
        widget_contenedor_principal = QWidget()
        widget_contenedor_principal.setStyleSheet("""QWidget{
                                    background-color: white;
                                    }""")

        widget_contenedor_principal.setLayout(contenedor_principal)

        # LAYOUT DEL TITULO GENLIST ↓↓↓

        contenedor_titulo = QHBoxLayout()
        # Cambiar el backgroud
        widget_contenedor_titulo = QWidget()
        diseño_titulo = f"""QWidget{{background: qlineargradient(x1:0, y1:0, x2:0.707, y2:0.707, stop:0.1 rgba(46, 145, 221, 255),
            stop:0.4 rgba(40, 125, 190, 255),
            stop:0.6 rgba(33, 104, 158, 255));
            max-height: {altoT}px;
            }}"""
        widget_contenedor_titulo.setLayout(contenedor_titulo)
        widget_contenedor_titulo.setStyleSheet(diseño_titulo)
        # LAYOUT DEL TITULO GENLIST ↑↑↑

        # Crear Layout Parte de Registro

        self.contenedor_pre_registro = QVBoxLayout()
        self.widget_con_pre_registro = QWidget()
        self.widget_con_pre_registro.setLayout(self.contenedor_pre_registro)

        self.contenedor_pre_pre_registro = QHBoxLayout()
        self.widget_contenedor_pre_pre_registro = QWidget()
        self.widget_contenedor_pre_pre_registro.setLayout(
            self.contenedor_pre_pre_registro)

        self.contenedor_pre_registro.addWidget(
            self.widget_contenedor_pre_pre_registro)

        # CAMBIO DE PANTALLA CENTRAL
        # boton login
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

        #! Creacion de los botones de las barras de las paginas
        # todo botones pag2
        self._boton_cerrar_sesion = QPushButton("Cerrar Sesion")
        self._boton_cerrar_sesion.clicked.connect(self.volver_inicio)
        self.boton_crear_curso = QPushButton("Crear Curso")
        self.boton_crear_curso.clicked.connect(self.crear_curso)
        # todo botones pag3
        self.boton_cancelar = QPushButton("Cancelar")
        self.boton_cancelar.clicked.connect(self.cancelar)
        self.boton_agregar_estudiante = QPushButton("Agregar Estudiante")
        self.boton_agregar_estudiante.clicked.connect(self.b_llenar_curso)
        self.boton_finalizar = QPushButton("Finalizar")
        self.boton_finalizar.clicked.connect(self.train)
        self.boton_finalizar.clicked.connect(self.finalizar_curso)
        # todo botones pag4
        self.boton_cancelar2 = QPushButton("Cancelar")
        self.boton_cancelar2.clicked.connect(self.volverpag2)
        self.boton_biometria = QPushButton("Biometria")
        self.boton_biometria.clicked.connect(self.capture)
        self.boton_guardar = QPushButton("Registrar")
        self.boton_guardar.clicked.connect(self.creacion_vector)
        self.boton_guardar.clicked.connect(self.registrar_estudiante)
        # todo botones pag5
        self.boton_cancelar3 = QPushButton("Cancelar")
        self.boton_cancelar3.clicked.connect(self.volver_pag_cursos)
        self.boton_asistio = QPushButton("Registrar Estudiante")
        self.boton_pdf = QPushButton("Generar PDF")

        #! LAYOUT DE LOS CREDITOS ↓↓↓↓
        contenedor_credito = QVBoxLayout()

        diseño_barra_F = F"""QWidget {{
            background: qlineargradient(x1: 0, y1: 0, x2: 0.707, y2: 0.707, stop: 0.04 #45DC20, stop: 0.6 #179400);
            max-height: {self.altoC}px;
        }}"""
        # 110;

        widget_contenedor_credito = QWidget()
        widget_contenedor_credito.setLayout(contenedor_credito)
        widget_contenedor_credito.setStyleSheet(diseño_barra_F)
        #! LAYOUT DE LOS CREDITOS ↑↑↑↑

        # AGREGAR ELEMENTOS A LOS LAYOUTS
        # LAYOUT TITULO ↓
        contenedor_titulo.addWidget(titulo_inicial)
        # LAYOUT CREDITO↓
        contenedor_credito.addWidget(credito)
        contenedor_credito.addWidget(autor1)

        fondo = QVBoxLayout()
    # Agregar los Qwidget a al Layout original
        contenedor_principal.addWidget(widget_contenedor_titulo)

        contenedor_principal.addWidget(
            self.widget_con_pre_registro)

        contenedor_principal.addWidget(widget_contenedor_credito)

    # Agregar los layouts a al layoud original
        fondo.addWidget(widget_contenedor_principal)
        app.setStyle("Fusion")
        # Esta linea crea el primer layout ↓
        self.setLayout(fondo)

    #! Funcion para crear la ventana 2, Clase Docente↓↓↓
    def generar_cursos(self, boton_cerrar, boton_crear_curso):

        materias = conexcionBD.obtener_nombres_clases(self.profesor_id)
        general = QVBoxLayout()
        widget_general = QWidget()
        widget_general.setLayout(general)

        # Creamos el ScrollArea y lo configuramos
        altoScroll = int((self.ventana.height())*0.55)
        anchoScroll = int((self.ventana.width()*0.52))
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setFixedHeight(altoScroll)
        scroll_area.setFixedWidth(anchoScroll)
        scroll_area.setSizePolicy(
            QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        general.addWidget(scroll_area)
        scroll_area.setStyleSheet("""QScrollArea{
                                  border: 1px solid black;
                                  border-radius: 5px;
        }""")

        # Creamos el widget que irá dentro del ScrollArea
        widget_scroll = QWidget()
        widget_scroll.setStyleSheet("""QWidget{
                                    background: #DBE5D9;
                                    }""")
        scroll_area.setWidget(widget_scroll)

        contenedor_registro = QVBoxLayout()
        contenedor_registro.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        widget_contenedor_registro = QWidget()
        widget_contenedor_registro.setLayout(contenedor_registro)
        widget_contenedor_registro.setFixedHeight(500)
        # widget_contenedor_registro.setMinimumHeight(1500)
        widget_contenedor_registro.setStyleSheet("""QWidget{
                                    border: 1px solid black;
                                    border-radius: 9px;
                                    margin: 1px 1px;
                                    }""")

        for materia in materias:
            widget1 = self.crear_materias(materia)
            contenedor_registro.addWidget(widget1)

        widget_scroll.setLayout(contenedor_registro)
        general.addWidget(self.barra_botones_pag1(
            boton_cerrar, boton_crear_curso))
        return widget_general

    #! Funcion utilizada en generar cursos, para crear los label de Clase↓↓↓
    def crear_materias(self, materia):
        nombre_materia = QLabel(materia)
        nombre_materia.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        nombre_materia.setStyleSheet("""QLabel{
                        color: black;
                        font-family: sans-serif;
                        font-weight: bold;
                        border: none;
                        min-width: 400px;
                        max-width: 400px;
                        max-height: 20px;
                        min-height: 20px;
                    }""")
        anchoEtiqueta = int((self.ventana.width()*0.49))
        primer_materia = QHBoxLayout()
        widget_primer_materia = QWidget()
        widget_primer_materia.setLayout(primer_materia)
        widget_primer_materia.setStyleSheet(f"""QWidget{{
                                    background: #FFFFFF;
                                    border: 1px solid black;
                                    border-radius: 2px;
                                    min-width: {anchoEtiqueta}px;
                                    max-width: {anchoEtiqueta}px;
                                    max-height: 50px;
                                    min-height: 50px;
                                    margin: 1px 1px;
                                    }}""")
        boton_editar = QPushButton("Borrar")
        boton_asistencia = QPushButton("Asistencia")
        botonE, botonA = self.crear_botones(
            boton_editar, boton_asistencia)
        botonE.clicked.connect(
            lambda checked, id=materia: self.borrar_materias(id))
        botonA.clicked.connect(
            lambda checked, id=materia: self.marcar_asistencia(id))

        primer_materia.addWidget(
            nombre_materia, alignment=Qt.AlignmentFlag.AlignLeft)
        primer_materia.addWidget(botonE, alignment=Qt.AlignmentFlag.AlignRight)
        primer_materia.addWidget(botonA)
        return widget_primer_materia

    #! Funcion utilizada en crear materis, para dar estilo a los botones de opciones↓↓↓
    def crear_botones(self, boton_editar, boton_asistencia):

        boton_editar.setStyleSheet("""
                    QPushButton {
                        background-color: #F75A50;
                        color: white;
                        border-radius: 5px;
                        padding: 5px;
                        font-size: 20px;
                        font-weight: bold;
                        min-width: 100px;
                        max-width: 100px;
                        max-height: 20px;
                        min-height: 20px;
                    }
                    QPushButton:hover {
                        background-color: #555555;
                    }
                    QPushButton:pressed {
                        background-color: #222222;
                    }
                """)

        boton_asistencia.setStyleSheet("""
                    QPushButton {
                        background-color: #0A6EB0;
                        color: white;
                        border-radius: 5px;
                        padding: 5px;
                        font-size: 20px;
                        font-weight: bold;
                        min-width: 100px;
                        max-width: 100px;
                        max-height: 20px;
                        min-height: 20px;
                    }
                    QPushButton:hover {
                        background-color: #555555;
                    }
                    QPushButton:pressed {
                        background-color: #222222;
                    }
                """)
        return boton_editar, boton_asistencia

    #! Funcion para crear la ventana 3, creacion de la clase↓↓↓
    def generar_llenado_curso(self, boton_cancelar, boton_agregar_estudiante, boton_finalzar):

        principal_pag2 = QVBoxLayout()
        widget_principal_pag2 = QWidget()
        widget_principal_pag2.setLayout(principal_pag2)

        anchoContenedor = int((self.ventana.width()*0.553))
        contenedor_form_curso = QVBoxLayout()
        widget_contenedor_form_curso = QWidget()
        widget_contenedor_form_curso.setStyleSheet(f"""QWidget{{
                                    background-color: #DBE5D9;
                                    border: 1px solid black;
                                    border-radius: 8px;
                                    margin: 1px 1px;
                                    max-width: {anchoContenedor}px;
                                    min-width: {anchoContenedor}px;
                                    }}""")
        # widget_contenedor_form_curso.setSizePolicy(QSizePolicy.Policy.Expanding,
        #                                            QSizePolicy.Policy.Expanding)
        widget_contenedor_form_curso.setLayout(contenedor_form_curso)

        texto_informacion_materia = QLabel("Nombre del curso y grupo : ")
        texto_informacion_materia.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        texto_informacion_materia.setStyleSheet("""QLabel{
                                    border: none;
                                    font-family: sans-serif;
                                    font-weight: bold;
                                    color: black;
                                    max-width: 180px;
                                    min-width: 180px;
                                    max-height: 60px;
                                    min-height: 60px;
                                    }""")
        anchomateria = int((self.ventana.width()*0.3252))
        self.materia_input = QLineEdit()
        self.materia_input.setStyleSheet(f"""QLineEdit{{
                            color: black;
                            font-family: sans-serif;
                            font-weight: bold;
                            border-radius: 8px;
                            border: 1px solid black;
                            min-height: 40px;
                            max-height: 40px;
                            max-width: {anchomateria}px;
                            min-width: {anchomateria}px;
        }}""")
        self.materia_input.setPlaceholderText(
            "Ejemplo: Sistemas Inteligentes AR")
        contenedor_cabeza = QHBoxLayout()
        contenedor_cabeza.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        widget_contenedor_cabeza = QWidget()
        widget_contenedor_cabeza.setStyleSheet("""QWidget{
                                    min-width: 800px;
                                    max-height: 80px;
                                    min-height: 80px;
                                    border: none;
                                    }""")
        widget_contenedor_cabeza.setLayout(contenedor_cabeza)
        contenedor_cabeza.addWidget(
            texto_informacion_materia)
        contenedor_cabeza.addWidget(
            self.materia_input, alignment=Qt.AlignmentFlag.AlignLeft)

        anchoTabla = int((self.ventana.width()*0.533))
        table = QTableWidget()
        table.setFixedHeight(350)
        # table.setFixedWidth(anchoTabla)
        table.setRowCount(6)  # Establece el número de filas
        table.setColumnCount(3)  # Establece el número de columnas
        table.setSizePolicy(QSizePolicy.Policy.Expanding,
                            QSizePolicy.Policy.Expanding)
        table.setEnabled(False)
        table.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        # anchoTituloTabla = int((self.ventana.width()*0.50))
        anchoTituloTabla = int(anchoTabla - 12)
        anchoTituloTabla1 = int(anchoTabla/3)
        # header = table.horizontalHeader()
        # header.resizeSection(1, anchoTituloTabla1)
        table.setHorizontalHeaderLabels(
            ["Nombres y Apellidos", "Documento", "Carrera"])
        table.horizontalHeader().setStyleSheet(f"""
                    QHeaderView::section {{
                        background-color: #DBE5D9;
                        color: black;
                        font-weight: bold;
                        border: none;
                        border-radius: 0px;
                        min-height: 30px;
                        min-width: {anchoTituloTabla}px;
                        max-width: {anchoTituloTabla}px; 

                    }}
                    QHeaderView {{
                        border: none;
                        border-radius: 0px;
                        min-width: {anchoTituloTabla}px;
                        max-width: {anchoTituloTabla}px; 

                    }}
                """)
        table.verticalHeader().setStyleSheet(f"""
                    QHeaderView::section {{
                        background-color: #DBE5D9;
                        color: black;
                        font-weight: bold;
                        border: none;
                        border-radius: 0px;
                        min-height: 30px;
                        min-width: {10}px;
                        max-width: {10}px;
                    }}
                    QHeaderView {{
                        border: none;
                        border-radius: 0px;
                        min-width: {10}px;
                        max-width: {10}px;
                    }}
                """)
        table.setStyleSheet(f"""
                QTableWidget {{
                    background-color: white;
                    color: black;
                    border: none;
                    border-radius: 0px;
                    min-width: {anchoTabla}px;
                    max-width: {anchoTabla}px;            

                }}
                QTableWidget::item {{
                    color: black;
                    border: 1px solid black;
                    border-radius: 0px;
                    min-width: {anchoTituloTabla}px;
                    max-width: {anchoTituloTabla}px;               
                          
                }}
                QTableWidget::item:selected {{
                    color: black;
                    border: 1px solid transparent;
                }}
                            """)

        # table.setColumnWidth(0, anchoTituloTabla)
        # table.setColumnWidth(1, anchoTituloTabla)
        # table.setColumnWidth(2, anchoTituloTabla)

        row_labels = [str(i+1) for i in range(table.rowCount())]
        table.setVerticalHeaderLabels(row_labels)
        # header.setSectionResizeMode(QHeaderView.ResizeMode.ResizeToContents)
        table.horizontalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.Stretch)
        table.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)

    # todo Insetar informacion en la tabla ↓↓↓
        # for i in range(5):  # Rellena la tabla con datos de ejemplo
        #     for j in range(3):
        #         table.setItem(
        #             i, j, QTableWidgetItem(f"Celda {i+1}, {j+1}"))
        # Primer bucle for para recorrer las sublistas (listas dentro de la lista principal)
        for i in range(len(self.estudiantes)):
            for j in range(3):
                # print(self.estudiantes[i][j])
                table.setItem(i, j, QTableWidgetItem(self.estudiantes[i][j]))
    # todo Insertar informacion en la tabla ↑↑↑
        contenedor_form_curso.addWidget(
            widget_contenedor_cabeza, alignment=Qt.AlignmentFlag.AlignTop)
        contenedor_form_curso.addWidget(table)

        principal_pag2.addWidget(widget_contenedor_form_curso)
        principal_pag2.addWidget(self.barra_botones_pag2(
            boton_cancelar, boton_agregar_estudiante, boton_finalzar))
        return widget_principal_pag2

    #! Funcion para crear la ventana 4, creacion de estudiante ↓↓↓
    def llenar_curso(self, boton_cancelar2, boton_biometria, boton_registrar):

        contenedro_pag3 = QVBoxLayout()
        widget_contendor_pag3 = QWidget()
        widget_contendor_pag3.setLayout(contenedro_pag3)

        contenedor_llenado_informacion = QHBoxLayout()
        widget_contenedor_llenado_informacion = QWidget()
        widget_contenedor_llenado_informacion.setLayout(
            contenedor_llenado_informacion)

        contenedor_informacion = QVBoxLayout()
        widget_contenedor_informacion = QWidget()
        widget_contenedor_informacion.setLayout(contenedor_informacion)
        widget_contenedor_informacion.setStyleSheet("""QWidget{
                                    max-width: 500px;
                                    min-width: 500px;
                                    margin: 1px 1px;
                                    }""")

        nombre_completo = QLabel("Nombre Completo")
        nombre_completo.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        nombre_completo.setStyleSheet("""QLabel{
                            color: black;
                            font-family: sans-serif;
                            font-size: 20px;
                            font-weight: bold;
                            border: none;
                            min-width: 250px;
                            max-width: 250px;
                            max-height: 20px;
                            min-height: 20px;
                        }""")
        self.input_nombre_completo = QLineEdit()
        self.input_nombre_completo.setStyleSheet("""QLineEdit{
                            color: black;
                            font-family: sans-serif;
                            font-size: 15px;
                            border: 1px solid black;
                            border-radius: 8px;
                            min-width: 400px;
                            max-width: 400px;
                            max-height: 50px;
                            min-height: 50px;
                        }""")
        self.input_nombre_completo.setPlaceholderText(
            "Escribe el nombre completo del estudiante")

        documento = QLabel("Numero de Documento")
        documento.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        documento.setStyleSheet("""QLabel{
                            color: black;
                            font-family: sans-serif;
                            font-size: 20px;
                            font-weight: bold;
                            border: none;
                            min-width: 250px;
                            max-width: 250px;
                            max-height: 20px;
                            min-height: 20px;
                        }""")
        self.input_documento = QLineEdit()
        self.input_documento.setPlaceholderText(
            "Escribe el documento del estudiante")
        self.input_documento.setStyleSheet("""QLineEdit{
                            color: black;
                            font-family: sans-serif;
                            font-size: 15px;
                            border: 1px solid black;
                            border-radius: 8px;
                            min-width: 400px;
                            max-width: 400px;
                            max-height: 50px;
                            min-height: 50px;
                        }""")
        carrera = QLabel("Carrera del Estudiante")
        carrera.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        carrera.setStyleSheet("""QLabel{
                            color: black;
                            font-family: sans-serif;
                            font-size: 20px;
                            font-weight: bold;
                            border: none;
                            min-width: 250px;
                            max-width: 250px;
                            max-height: 20px;
                            min-height: 20px;
                        }""")
        self.input_carrera = QLineEdit()
        self.input_carrera.setPlaceholderText(
            "Escriba la carrera a la cual el estudiante pertenece")
        self.input_carrera.setStyleSheet("""QLineEdit{
                            color: black;
                            font-family: sans-serif;
                            font-size: 15px;
                            border: 1px solid black;
                            border-radius: 8px;
                            min-width: 400px;
                            max-width: 400px;
                            max-height: 50px;
                            min-height: 50px;
                        }""")
        contenedor_informacion.addWidget(nombre_completo)
        contenedor_informacion.addWidget(self.input_nombre_completo)
        contenedor_informacion.addWidget(documento)
        contenedor_informacion.addWidget(self.input_documento)
        contenedor_informacion.addWidget(carrera)
        contenedor_informacion.addWidget(self.input_carrera)

        contenedor_camara = QHBoxLayout()

        widget_contenedor_camara = QWidget()
        widget_contenedor_camara.setLayout(contenedor_camara)
        widget_contenedor_camara.setStyleSheet("""QWidget{
                                    background-color: #DBE5D9;
                                    border: 1px solid black;
                                    border-radius: 9px;
                                    margin: 1px 1px;
                                    }""")

        contenedor_camara.addWidget(self.cameraLabel)

        contenedor_llenado_informacion.addWidget(widget_contenedor_informacion)
        contenedor_llenado_informacion.addWidget(widget_contenedor_camara)

        contenedro_pag3.addWidget(widget_contenedor_llenado_informacion)
        anchoBarra3 = int((self.ventana.width()*0.944))
        auxiliar = self.barra_botones_pag2(
            boton_cancelar2, boton_biometria, boton_registrar)
        auxiliar.setStyleSheet(f"""QWidget{{
                                    background-color: #DBE5D9;
                                    border: 1px solid black;
                                    border-radius: 9px;
                                    min-width: {anchoBarra3}px;
                                    max-width: {anchoBarra3}px;
                                    margin: 1px 1px;
                                    max-height: 60px;
                                    min-height: 60px;
                                    }}""")
        contenedro_pag3.addWidget(
            auxiliar, alignment=Qt.AlignmentFlag.AlignHCenter)

        return widget_contendor_pag3

    #! Funcion para crear la ventana 5, toma de asistencia del estudiante↓↓↓
    def tomar_asistencia(self, boton_cancelar3, boton_asistio, boton_pdf):

        contenedor_pag4 = QVBoxLayout()
        widget_contenedor_pag4 = QWidget()
        widget_contenedor_pag4.setLayout(contenedor_pag4)

        contenedor_toma_asistencia = QVBoxLayout()
        widget_contenedor_toma_asistencia = QWidget()
        widget_contenedor_toma_asistencia.setLayout(contenedor_toma_asistencia)

        recomendacion = QLabel(
            "IMPORTANTE: Solo debe salir en camara la persona a registrar")
        # recomendacion.setAttribute(
        #     QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        recomendacion.setStyleSheet("""QLabel{
                            color: black;
                            font-family: sans-serif;
                            font-size: 20px;
                            font-weight: bold;
                            border: none;
                            min-width: 630px;
                            max-width: 630px;
                            max-height: 30px;
                            min-height: 30px;
                        }""")

        anchoCamara = int((self.ventana.width()*0.553))

        contenedor_cargar_camara = QHBoxLayout()
        widget_contenedor_cargar_camara = QWidget()
        widget_contenedor_cargar_camara.setLayout(contenedor_cargar_camara)
        widget_contenedor_cargar_camara.setStyleSheet(f"""QWidget{{
                                    background-color: #DBE5D9;
                                    border: 1px solid black;
                                    border-radius: 9px;
                                    min-width: {anchoCamara}px;
                                    max-width: {anchoCamara}px;
                                    margin: 1px 1px;
                                    }}""")

        contenedor_cargar_camara.addWidget(self.cameraLabel)

        contenedor_toma_asistencia.addWidget(
            recomendacion, alignment=Qt.AlignmentFlag.AlignHCenter)
        contenedor_toma_asistencia.addWidget(
            widget_contenedor_cargar_camara, alignment=Qt.AlignmentFlag.AlignHCenter)

        contenedor_pag4.addWidget(widget_contenedor_toma_asistencia)
        contenedor_pag4.addWidget(self.barra_botones_pag2(
            boton_cancelar3, boton_asistio, boton_pdf), alignment=Qt.AlignmentFlag.AlignHCenter)

        return widget_contenedor_pag4

    #! Funcion para crear la barra de opciones de la ventana 2↓↓↓
    def barra_botones_pag1(self, boton_cerrar, boton_crear_curso):

        # Creacion de contenerdor de datos y acciones basicas
        anchoBarra = int((self.ventana.width()*0.52))
        contenedor_ayuda = QHBoxLayout()
        widget_contenedor_ayuda = QWidget()
        widget_contenedor_ayuda.setStyleSheet(f"""QWidget{{
                                    background-color: #DBE5D9;
                                    border: 1px solid black;
                                    border-radius: 9px;
                                    min-width: {anchoBarra}px;
                                    margin: 1px 1px;
                                    max-height: 60px;
                                    min-height: 60px;
                                    }}""")
        widget_contenedor_ayuda.setLayout(contenedor_ayuda)

        boton_cerrar.setFixedWidth(150)
        boton_cerrar.setStyleSheet("""
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

        boton_crear_curso.setFixedWidth(150)
        boton_crear_curso.setStyleSheet("""
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

        contenedor_ayuda.addWidget(
            boton_crear_curso, alignment=Qt.AlignmentFlag.AlignLeft)
        contenedor_ayuda.addWidget(
            boton_cerrar, alignment=Qt.AlignmentFlag.AlignRight)
        return widget_contenedor_ayuda

    #! Funcion para crear la barra de opciones de la ventana 3,4,5↓↓↓
    def barra_botones_pag2(self, boton_cancelar, boton_agregar_estudiante, boton_finalzar):

        # Creacion de contenerdor de datos y acciones basicas
        anchoBarra2 = int((self.ventana.width()*0.553))
        contenedor_ayuda = QHBoxLayout()
        widget_contenedor_ayuda = QWidget()
        widget_contenedor_ayuda.setStyleSheet(f"""QWidget{{
                                    background-color: #DBE5D9;
                                    border: 1px solid black;
                                    border-radius: 9px;
                                    min-width: {anchoBarra2}px;
                                    max-width: {anchoBarra2}px;
                                    margin: 1px 1px;
                                    max-height: 60px;
                                    min-height: 60px;
                                   }}""")
        widget_contenedor_ayuda.setLayout(contenedor_ayuda)

        boton_cancelar.setFixedWidth(150)
        boton_cancelar.setStyleSheet("""
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

        boton_agregar_estudiante.setFixedWidth(150)
        boton_agregar_estudiante.setStyleSheet("""
                    QPushButton {
                        background-color: #43AB3A;
                        color: white;
                        border-radius: 5px;
                        padding: 1px;
                        font-size: 15px;
                        font-weight: bold;
                        min-width: 150px;
                        max-width: 150px;
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

        boton_finalzar.setFixedWidth(150)
        boton_finalzar.setStyleSheet("""
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
        contenedor_ayuda.addWidget(
            boton_cancelar, alignment=Qt.AlignmentFlag.AlignLeft)
        contenedor_ayuda.addWidget(
            boton_agregar_estudiante, alignment=Qt.AlignmentFlag.AlignCenter)
        contenedor_ayuda.addWidget(
            boton_finalzar, alignment=Qt.AlignmentFlag.AlignRight)

        return widget_contenedor_ayuda

    #! FUNCIONES DE VALIDACIONES ↓↓↓
    # todo Funcion boton Registrar/Login pag1
    def haz_dado_click(self):
        aprobacion = False
        usuario = int(self.usuario_input.text())
        contraseña = self.Contra_input.text()
        # print(usuario)
        aprobacion = conexcionBD.validar_credenciales_profesor(
            usuario, contraseña)
        if aprobacion is True:
            self.profesor_id = conexcionBD.obtener_id_profesor(usuario)
            self.usuario_input.clear()
            self.Contra_input.clear()
            self.cambiar_pantalla()

        else:
            self.mensaje_emergente.setWindowTitle("Mensaje de ERROR")
            self.mensaje_emergente.setText("Datos Incorrectos.")
            self.mensaje_emergente.setIcon(QMessageBox.Icon.Warning)
            self.mensaje_emergente.exec()
            self.usuario_input.clear()
            self.Contra_input.clear()

    # todo Funcion boton Registrar acomodar con lo WhatsApp ↓↓ pag4
    def creacion_vector(self):

        nombreEstudiante = self.input_nombre_completo.text()
        documentoEstudiante = self.input_documento.text()
        carreraEstudiante = self.input_carrera.text()

        datos_estudiante = [nombreEstudiante,
                            documentoEstudiante, carreraEstudiante]

        self.estudiantes.append(datos_estudiante)

    #! FUNCIONES DE LOS BOTONES ↓↓ ¦ ↓↓ ¦ ↓↓ ¦
    # ? funcion boton registrar del Login pag1
    def cambiar_pantalla(self):
        self.contenedor_pre_registro.removeWidget(
            self.widget_contenedor_pre_pre_registro)
        self.widget_contenedor_pre_pre_registro.hide()

        self.widget_cuerpo = self.generar_cursos(
            self._boton_cerrar_sesion, self.boton_crear_curso)

        self.contenedor_pre_registro.addWidget(
            self.widget_cuerpo, alignment=Qt.AlignmentFlag.AlignCenter)
        self.showMaximized()

    # ?funcion boton cerrar sesion pag2
    def volver_inicio(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo)
        self.widget_cuerpo.hide()
        self.showMaximized()
        self.widget_contenedor_pre_pre_registro.show()

    # ? Boton Asistencia en las materias pag2
    def marcar_asistencia(self, materia):
        self.materia_asistencia = materia
        self.descargarModel()
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo)
        self.widget_cuerpo.hide()
        self.widget_cuerpo_pag4 = self.tomar_asistencia(
            self.boton_cancelar3, self.boton_asistio, self.boton_pdf)
        self.contenedor_pre_registro.addWidget(self.widget_cuerpo_pag4)
        self.start_recognition()
        self.showMaximized()

    # ? Bototn Editar en las materias pag2
    def borrar_materias(self, materia):
        id_clase_borrar = conexcionBD.obtener_id_clase(materia)
        conexcionBD.eliminar_datos_por_clase_id(id_clase_borrar)
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo)
        self.widget_cuerpo.hide()
        self.cambiar_pantalla()

    # ? Funcion del boton crear curso pag2
    def crear_curso(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo)
        self.widget_cuerpo.hide()
        self.widget_cuerpo_pag2 = self.generar_llenado_curso(
            self.boton_cancelar, self.boton_agregar_estudiante, self.boton_finalizar)
        # self.widget_cuerpo_pag2.setSizePolicy(
        #     QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        self.contenedor_pre_registro.addWidget(
            self.widget_cuerpo_pag2, alignment=Qt.AlignmentFlag.AlignCenter)
        self.showMaximized()

    # ? Funcion boton cancelar pag3
    def cancelar(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo_pag2)
        self.widget_cuerpo_pag2.hide()
        self.showMaximized()
        self.widget_cuerpo.show()

    # ? Funcion boton finalizar en pag3
    def finalizar_curso(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo_pag2)
        self.widget_cuerpo_pag2.hide()
        self.showMaximized()
        nombre_clase = self.materia_input.text()
        conexcionBD.insertar_clase(nombre_clase, self.profesor_id)
        clase_id = conexcionBD.obtener_id_clase(nombre_clase)
        for i in range(len(self.estudiantes)):
            conexcionBD.insertar_estudiante(int(
                self.estudiantes[i][1]), self.estudiantes[i][0], self.estudiantes[i][2], clase_id)
        datos_biometricos = self.convertir()

        conexcionBD.insertar_datos_biometricos(datos_biometricos, clase_id)
        self.estudiantes = []
        self.cambiar_pantalla()
        # self.widget_cuerpo.show()

    # ?Funcion boton agregar estudiantes pag3
    def b_llenar_curso(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo_pag2)
        self.widget_cuerpo_pag2.hide()
        self.widget_cuerpo_pag3 = self.llenar_curso(
            self.boton_cancelar2, self.boton_biometria, self.boton_guardar)
        self.contenedor_pre_registro.addWidget(self.widget_cuerpo_pag3)
        self.showMaximized()

    # ? Funcion boton cancelar pag4
    def volverpag2(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo_pag3)
        self.widget_cuerpo_pag3.hide()
        self.showMaximized()
        self.widget_cuerpo_pag2.show()

    # ? Funcion boton regsitar pag4
    def registrar_estudiante(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo_pag3)
        self.widget_cuerpo_pag3.hide()
        self.showMaximized()
        self.crear_curso()
        # self.widget_cuerpo_pag2.show()

    # ? Funcion boton cancelar pag5
    def volver_pag_cursos(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo_pag4)
        self.widget_cuerpo_pag4.hide()
        self.stop_camera()
        self.showMaximized()
        self.widget_cuerpo.show()

    # ! FUNCIONES DE RECONOCIMIENTO FACIAL ↓↓ ¦ ↓↓ ¦ ↓↓ ¦

    # ? Conversor de Modelo a LONGBLOB
    def convertir(self):
        # Carga los datos del archivo
        with open('src/Models/ModeloFaceFrontalData2024.pkl', 'rb') as f:
            data = pickle.load(f)

        # Serializa los datos
        pickled_data = pickle.dumps(data)
        return pickled_data

    def descargarModel(self):
        id_clase = conexcionBD.obtener_id_clase(self.materia_asistencia)
        pickled_data = conexcionBD.obtener_datos_biometricos(id_clase)
        data = pickle.loads(pickled_data)
        # Guarda los datos en un archivo .pkl
        with open('ModeloFaceFrontalData2024.pkl', 'wb') as f:
            pickle.dump(data, f)

    # ? Captura de imagenes
    def capture(self):
        # personName, ok = QtWidgets.QInputDialog.getText(self, 'Input Dialog', 'Ingrese el nombre de la persona:')
        personName = self.input_documento.text()
        self.start_camera()
        self.is_capturing = True
        self.personName = personName
        self.model = cv2.dnn.readNetFromTorch('openface.nn4.small2.v1.t7')

    # ? Entrenado de Modelo
    def train(self):
        train_model.train_model()
        # QtWidgets.QMessageBox.information(self, "Entrenamiento", "Modelo entrenado y guardado exitosamente.")

    # ? Iniciador de reconocimiento
    def start_recognition(self):
        self.start_camera()
        self.is_recognizing = True
        self.load_model()

    # ? Identificador de Personas para Asistencia
    def identify_person(self):
        if self.is_recognizing and self.cap:
            ret, frame = self.cap.read()
            if ret:
                results = recognize.recognize_face(frame, self.clf, self.model)
                for (x, y, w, h, label) in results:
                    if label == 'Desconocido':
                        message = 'Desconocido'
                    else:
                        personName = self.get_person_name(label)
                        message = f'Persona reconocida: {personName}'
                    QtWidgets.QMessageBox.information(
                        self, "Reconocimiento", message)
                    return

    # ? Iniciador de Camara
    def start_camera(self):
        if self.cap is None:
            self.cap = cv2.VideoCapture(0, cv2.CAP_DSHOW)
        self.timer.start(30)

    # ? Detencion de Camara
    def stop_camera(self):
        self.timer.stop()
        if self.cap is not None:
            self.cap.release()
            self.cap = None

    # ? Actualizacion de Frame osea imagen
    def update_frame(self):
        ret, frame = self.cap.read()
        if ret:
            frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            image = QtGui.QImage(
                frame, frame.shape[1], frame.shape[0], frame.strides[0], QtGui.QImage.Format.Format_RGB888)
            self.cameraLabel.setPixmap(QtGui.QPixmap.fromImage(image))

            if self.is_capturing:
                capture_and_save.capture_and_save(
                    self.personName, self.cameraLabel, self.model)
                self.is_capturing = False
            elif self.is_recognizing:
                self.display_recognition(frame)
        else:
            self.stop_camera()

    # ? Muestra la camara de reconocimiento
    def display_recognition(self, frame):
        results = recognize.recognize_face(frame, self.clf, self.model)
        for (x, y, w, h, label) in results:
            if label == 'Desconocido':
                cv2.putText(frame, 'Desconocido', (x, y-20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 0, 255), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 0, 255), 2)
            else:
                personName = str(self.get_person_name(label))
                cv2.putText(frame, personName, (x, y-20),
                            cv2.FONT_HERSHEY_SIMPLEX, 0.8, (0, 255, 0), 1, cv2.LINE_AA)
                cv2.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
        frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        image = QtGui.QImage(
            frame, frame.shape[1], frame.shape[0], frame.strides[0], QtGui.QImage.Format.Format_RGB888)
        self.cameraLabel.setPixmap(QtGui.QPixmap.fromImage(image))

    # ? Carga modelo
    def load_model(self):
        model_path = os.path.join(os.path.dirname(os.path.dirname(
            os.path.realpath(__file__))), 'src', 'Models', 'ModeloFaceFrontalData2024.pkl')
        with open(model_path, 'rb') as f:
            self.clf = pickle.load(f)
        self.model = cv2.dnn.readNetFromTorch('openface.nn4.small2.v1.t7')

    # ? Obtencion de Persona
    def get_person_name(self, label):
        dataPath = os.path.join(os.path.dirname(
            os.path.dirname(os.path.realpath(__file__))), 'src', 'Data')
        peopleList = os.listdir(dataPath)
        return peopleList[label]

    # ? Apagador de Camara
    def closeEvent(self, event):
        self.stop_camera()
        event.accept()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = inicio()
    sys.exit(app.exec())
