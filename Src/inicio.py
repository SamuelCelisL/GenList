import sys
from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (
    QApplication, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton,
    QLineEdit, QMessageBox, QSizePolicy, QScrollArea, QTableWidget, QHeaderView)
from PyQt6.QtGui import QFont, QIcon
from PyQt6 import QtGui, QtCore
from components import login


class inicio (QWidget):

    def __init__(self):
        super().__init__()
        self.InicializarUI()

    def InicializarUI(self):
        screen = app.primaryScreen()
        self.ventana = screen.size()
        # print(self.size)
        # ancho = self.size.width()
        # alto = (self.size.height())*0.20
        # print(alto)
        # self.setGeometry(0, 0, ancho, alto)
        self.setWindowTitle("Login GenList")
        self.setWindowIcon(QIcon('src/images/logo2.ico'))
        self.generar_formulario()
        self.showMaximized()
        self.show()

    def generar_formulario(self):

        self.usuarios = [['adminSamuel', 'adminSamuel'], [
            'adminMarquez', 'adminMarquez'], ['adminYorman', 'adminYorman']]

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
        print(tamaño_fuete_autores)
        print(tamaño_etiqueta_autor)
        print(tamaño_fuente_credito)
        print(tamaño_fuente_credito)
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
        print(credito.height())
        print(autor1.height())

        # autor2 = QLabel("Samuel Andres Celis Lizcano")
        # autor2.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # autor2.setStyleSheet(f"""QLabel{{
        #             color: white;
        #             font-family: sans-serif;
        #             font-size: {tamaño_fuete_autores-2}px;
        # }}""")
        # autor2.setAttribute(
        #     QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)

        # autor3 = QLabel("Yorman Rodolfo Rodriguez Jaimes")
        # autor3.setAlignment(Qt.AlignmentFlag.AlignCenter)
        # autor3.setStyleSheet(f"""QLabel{{
        #             color: white;
        #             font-family: sans-serif;
        #             font-size: {tamaño_fuete_autores-2}px;
        # }}""")
        # autor3.setAttribute(
        #     QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)

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
        # self.boton_registrar.clicked.connect(self.haz_dado_click)
        self.boton_registrar.clicked.connect(self.cambiar_pantalla)

        # Creacion de los botones de las barras de las paginas
        # botones pag1
        self._boton_cerrar_sesion = QPushButton("Cerrar Sesion")
        self._boton_cerrar_sesion.clicked.connect(self.volver_inicio)
        self.boton_crear_curso = QPushButton("Crear Curso")
        self.boton_crear_curso.clicked.connect(self.crear_curso)
        # botones pag2
        self.boton_cancelar = QPushButton("Cancelar")
        self.boton_cancelar.clicked.connect(self.cancelar)
        self.boton_agregar_estudiante = QPushButton("Agregar Estudiante")
        self.boton_agregar_estudiante.clicked.connect(self.b_llenar_curso)
        self.boton_finalizar = QPushButton("Finalizar")
        self.boton_finalizar.clicked.connect(self.finalizar_curso)
        # self.boton_finalizar.clicked.connect()
        # botones pag3
        self.boton_cancelar2 = QPushButton("Cancelar")
        self.boton_cancelar2.clicked.connect(self.volverpag2)
        self.boton_biometria = QPushButton("Biometria")
        self.boton_guardar = QPushButton("Registrar")
        self.boton_guardar.clicked.connect(self.registrar_estudiante)
        # botones pag4
        self.boton_cancelar3 = QPushButton("Cancelar")
        self.boton_cancelar3.clicked.connect(self.volver_pag_cursos)
        self.boton_asistio = QPushButton("Registrar Estudiante")
        self.boton_pdf = QPushButton("Generar PDF")

        # LAYOUT DE LOS CREDITOS ↓↓↓↓
        contenedor_credito = QVBoxLayout()

        diseño_barra_F = F"""QWidget {{
            background: qlineargradient(x1: 0, y1: 0, x2: 0.707, y2: 0.707, stop: 0.04 #45DC20, stop: 0.6 #179400);
            max-height: {self.altoC}px;
        }}"""
        # 110;

        widget_contenedor_credito = QWidget()
        widget_contenedor_credito.setLayout(contenedor_credito)
        widget_contenedor_credito.setStyleSheet(diseño_barra_F)
        # LAYOUT DE LOS CREDITOS ↑↑↑↑

        # AGREGAR ELEMENTOS A LOS LAYOUTS
        # LAYOUT TITULO ↓
        contenedor_titulo.addWidget(titulo_inicial)
        # LAYOUT CREDITO↓
        contenedor_credito.addWidget(credito)
        contenedor_credito.addWidget(autor1)
        # contenedor_credito.addWidget(autor2)
        # contenedor_credito.addWidget(autor3)

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

    def generar_cursos(self, boton_cerrar, boton_crear_curso):
        print("ESTAS EN LA SEGUNDA VENTANA")
        print("Ancho", self.ventana.width())
        print("Alto", self.ventana.height())
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
        scroll_area.setWidget(widget_scroll)

        materias = [
            "Sistemas Inteligentes AR",
            "Fundamentos de computacion paralela y distribuida AR",
            "ingenieria de Software I BR",
            "REDES BR",
            "Fundamentos de programacion AR",
            "Sistemas Inteligentes AR",
            "Fundamentos de computacion paralela y distribuida AR",
            "ingenieria de Software I BR",
            "REDES BR",
            "Fundamentos de programacion AR"
        ]
        contenedor_registro = QVBoxLayout()
        contenedor_registro.setAlignment(QtCore.Qt.AlignmentFlag.AlignTop)
        widget_contenedor_registro = QWidget()
        widget_contenedor_registro.setLayout(contenedor_registro)
        widget_contenedor_registro.setFixedHeight(500)
        # widget_contenedor_registro.setMinimumHeight(1500)
        widget_contenedor_registro.setStyleSheet("""QWidget{
                                    background-color: #DBE5D9;
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
        anchoEtiqueta = int((self.ventana.width()*0.495))
        primer_materia = QHBoxLayout()
        widget_primer_materia = QWidget()
        widget_primer_materia.setLayout(primer_materia)
        widget_primer_materia.setStyleSheet(f"""QWidget{{
                                    background-color: #FFFFFF;
                                    border: 1px solid black;
                                    border-radius: 2px;
                                    min-width: {anchoEtiqueta}px;
                                    max-width: {anchoEtiqueta}px;
                                    max-height: 50px;
                                    min-height: 50px;
                                    margin: 1px 1px;
                                    }}""")
        boton_editar = QPushButton("Editar")
        boton_asistencia = QPushButton("Asistencia")
        botonE, botonA = self.crear_botones(
            boton_editar, boton_asistencia)
        botonA.clicked.connect(self.marcar_asistencia)

        primer_materia.addWidget(
            nombre_materia, alignment=Qt.AlignmentFlag.AlignLeft)
        primer_materia.addWidget(botonE, alignment=Qt.AlignmentFlag.AlignRight)
        primer_materia.addWidget(botonA)
        return widget_primer_materia

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

    def generar_llenado_curso(self, boton_cancelar, boton_agregar_estudiante, boton_finalzar):

        principal_pag2 = QVBoxLayout()
        widget_principal_pag2 = QWidget()
        widget_principal_pag2.setLayout(principal_pag2)

        contenedor_form_curso = QVBoxLayout()
        widget_contenedor_form_curso = QWidget()
        widget_contenedor_form_curso.setStyleSheet(f"""QWidget{{
                                    background-color: #DBE5D9;
                                    border: 1px solid black;
                                    border-radius: 8px;
                                    margin: 1px 1px;
                                    }}""")
        widget_contenedor_form_curso.setSizePolicy(QSizePolicy.Policy.Expanding,
                                                   QSizePolicy.Policy.Expanding)
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
        materia_input = QLineEdit()
        materia_input.setStyleSheet(f"""QLineEdit{{
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
            materia_input, alignment=Qt.AlignmentFlag.AlignLeft)

        anchoTabla = int((self.ventana.width()*0.543))
        table = QTableWidget()
        table.setFixedHeight(350)
        table.setFixedWidth(anchoTabla)
        table.setRowCount(5)  # Establece el número de filas
        table.setColumnCount(3)  # Establece el número de columnas
        # table.setSizePolicy(QSizePolicy.Policy.Expanding,
        #                     QSizePolicy.Policy.Expanding)
        table.setEnabled(False)
        table.setAttribute(
            QtCore.Qt.WidgetAttribute.WA_TranslucentBackground, True)
        table.setHorizontalHeaderLabels(
            ["Nombres y Apellidos", "Documento", "Carrera"])
        table.horizontalHeader().setStyleSheet("""
                    QHeaderView::section {
                        background-color: #DBE5D9;
                        color: black;
                        font-weight: bold;
                        border: none;
                        border-radius: 0px;
                    }
                    QHeaderView {
                        border: none;
                        border-radius: 0px;
                    }
                """)
        table.verticalHeader().setStyleSheet("""
                    QHeaderView::section {
                        background-color: #DBE5D9;
                        color: black;
                        font-weight: bold;
                        border: none;
                        border-radius: 0px;
                        min-height: 30px;
                    }
                    QHeaderView {
                        border: none;
                        border-radius: 0px;
                    }
                """)
        table.setStyleSheet("""
                QTableWidget {
                    background-color: white;
                    color: black;
                    border: none;
                    border-radius: 0px;

                }
                QTableWidget::item {
                    color: black;
                    border: 1px solid black;
                    border-radius: 0px;
                }
                QTableWidget::item:selected {
                    color: black;
                    border: 1px solid transparent;
                }
                            """)
        row_labels = [str(i+1) for i in range(table.rowCount())]
        table.setVerticalHeaderLabels(row_labels)
        table.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeMode.Stretch)
        table.verticalHeader().setSectionResizeMode(
            QHeaderView.ResizeMode.ResizeToContents)

        # for i in range(5):  # Rellena la tabla con datos de ejemplo
        #     for j in range(3):
        #         table.setItem(
        #             i, j, QTableWidgetItem(f"Celda {i+1}, {j+1}"))

        contenedor_form_curso.addWidget(
            widget_contenedor_cabeza, alignment=Qt.AlignmentFlag.AlignTop)
        contenedor_form_curso.addWidget(table)

        principal_pag2.addWidget(widget_contenedor_form_curso)
        principal_pag2.addWidget(self.barra_botones_pag2(
            boton_cancelar, boton_agregar_estudiante, boton_finalzar))
        return widget_principal_pag2

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
        input_nombre_completo = QLineEdit()
        input_nombre_completo.setStyleSheet("""QLineEdit{
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
        input_nombre_completo.setPlaceholderText(
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
        input_documento = QLineEdit()
        input_documento.setPlaceholderText(
            "Escribe el documento del estudiante")
        input_documento.setStyleSheet("""QLineEdit{
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
        input_carrera = QLineEdit()
        input_carrera.setPlaceholderText(
            "Escriba la carrera a la cual el estudiante pertenece")
        input_carrera.setStyleSheet("""QLineEdit{
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
        contenedor_informacion.addWidget(input_nombre_completo)
        contenedor_informacion.addWidget(documento)
        contenedor_informacion.addWidget(input_documento)
        contenedor_informacion.addWidget(carrera)
        contenedor_informacion.addWidget(input_carrera)

        contenedor_camara = QHBoxLayout()
        widget_contenedor_camara = QWidget()
        widget_contenedor_camara.setLayout(contenedor_camara)
        widget_contenedor_camara.setStyleSheet("""QWidget{
                                    background-color: #DBE5D9;
                                    border: 1px solid black;
                                    border-radius: 9px;
                                    margin: 1px 1px;
                                    }""")

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

        contenedor_toma_asistencia.addWidget(
            recomendacion, alignment=Qt.AlignmentFlag.AlignHCenter)
        contenedor_toma_asistencia.addWidget(
            widget_contenedor_cargar_camara, alignment=Qt.AlignmentFlag.AlignHCenter)

        contenedor_pag4.addWidget(widget_contenedor_toma_asistencia)
        contenedor_pag4.addWidget(self.barra_botones_pag2(
            boton_cancelar3, boton_asistio, boton_pdf), alignment=Qt.AlignmentFlag.AlignHCenter)

        return widget_contenedor_pag4

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

    #! FUNCIONES DE DESPLAZAMIENTO Y LLAMADO ↓↓↓

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
        self.contenedor_pre_registro.removeWidget(
            self.widget_contenedor_pre_pre_registro)
        self.widget_contenedor_pre_pre_registro.hide()

        self.widget_cuerpo = self.generar_cursos(
            self._boton_cerrar_sesion, self.boton_crear_curso)

        # Establecer la política de tamaño del widget_cuerpo
        # self.widget_cuerpo.setSizePolicy(
        #     QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)

        self.contenedor_pre_registro.addWidget(
            self.widget_cuerpo, alignment=Qt.AlignmentFlag.AlignCenter)
        self.showMaximized()

    # FUNCIONES DE LOS BOTONES ↓↓ ¦ ↓↓ ¦ ↓↓ ¦
    # funcion boton cerrar sesion pag1

    def volver_inicio(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo)
        self.widget_cuerpo.hide()
        self.showMaximized()
        self.widget_contenedor_pre_pre_registro.show()

    # Boton Asistencia en las materias
    def marcar_asistencia(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo)
        self.widget_cuerpo.hide()
        self.widget_cuerpo_pag4 = self.tomar_asistencia(
            self.boton_cancelar3, self.boton_asistio, self.boton_pdf)
        self.contenedor_pre_registro.addWidget(self.widget_cuerpo_pag4)
        self.showMaximized()

    # Funcion del boton crear curso
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

    # Funcion boton cancelar pag2
    def cancelar(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo_pag2)
        self.widget_cuerpo_pag2.hide()
        self.showMaximized()
        self.widget_cuerpo.show()

    # Funcion boton finalizar en pag2
    def finalizar_curso(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo_pag2)
        self.widget_cuerpo_pag2.hide()
        self.showMaximized()
        self.widget_cuerpo.show()

    # Funcion boton agregar estudiantes pag3
    def b_llenar_curso(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo_pag2)
        self.widget_cuerpo_pag2.hide()
        self.widget_cuerpo_pag3 = self.llenar_curso(
            self.boton_cancelar2, self.boton_biometria, self.boton_guardar)
        self.contenedor_pre_registro.addWidget(self.widget_cuerpo_pag3)
        self.showMaximized()

    # Funcion boton cancelar pag3
    def volverpag2(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo_pag3)
        self.widget_cuerpo_pag3.hide()
        self.showMaximized()
        self.widget_cuerpo_pag2.show()

    # Funcion boton regsitar pag3
    def registrar_estudiante(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo_pag3)
        self.widget_cuerpo_pag3.hide()
        self.showMaximized()
        self.widget_cuerpo_pag2.show()

    # Funcion boton cancelar pag4
    def volver_pag_cursos(self):
        self.contenedor_pre_registro.removeWidget(self.widget_cuerpo_pag4)
        self.widget_cuerpo_pag4.hide()
        self.showMaximized()
        self.widget_cuerpo.show()


if __name__ == '__main__':
    app = QApplication(sys.argv)
    Login = inicio()
    sys.exit(app.exec())
