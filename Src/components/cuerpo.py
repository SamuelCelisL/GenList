from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import (QWidget, QLabel, QLineEdit,
                             QHBoxLayout, QVBoxLayout, QStackedLayout, QTableWidget,
                             QHeaderView, QTableWidgetItem, QAbstractItemView, QScrollArea, QSizePolicy)
from PyQt6 import QtCore


# def cuerpo_aplicacion():
#     cambiador_de_pantalla = QStackedLayout()
#     cambiador_de_pantalla.addWidget(generar_cursos)
#     cambiador_de_pantalla.addWidget(generar_llenado_curso)


def generar_cursos(boton_cerrar, boton_crear_curso, boton_editar, boton_asistencia):
    general = QVBoxLayout()
    widget_general = QWidget()
    widget_general.setLayout(general)

    # Creamos el ScrollArea y lo configuramos
    scroll_area = QScrollArea()
    scroll_area.setWidgetResizable(True)
    scroll_area.setSizePolicy(
        QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)  # Nueva línea
    general.addWidget(scroll_area)

    # Creamos el widget que irá dentro del ScrollArea
    widget_scroll = QWidget()
    scroll_area.setWidget(widget_scroll)

    # Tenemos que agregar el Scroll
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
    widget_contenedor_registro.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 9px;
                                min-width: 1000px;
                                max-height: 500px;
                                min-height: 500px;
                                margin: 1px 1px;
                                }""")

    for materia in materias:
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
        primer_materia = QHBoxLayout()
        widget_primer_materia = QWidget()
        widget_primer_materia.setLayout(primer_materia)
        widget_primer_materia.setStyleSheet("""QWidget{
                                    background-color: #FFFFFF;
                                    border: 1px solid black;
                                    border-radius: 2px;
                                    min-width: 760px;
                                    max-height: 50px;
                                    min-height: 50px;
                                    margin: 1px 1px;
                                    }""")
        botonE, botonA = crear_botones(boton_editar, boton_asistencia)

        primer_materia.addWidget(
            nombre_materia, alignment=Qt.AlignmentFlag.AlignLeft)
        primer_materia.addWidget(botonE, alignment=Qt.AlignmentFlag.AlignRight)
        primer_materia.addWidget(botonA)
        contenedor_registro.addWidget(widget_primer_materia)

    widget_scroll.setLayout(contenedor_registro)
    general.addWidget(barra_botones_pag1(
        boton_cerrar, boton_crear_curso))
    return widget_general


def crear_botones(boton_editar, boton_asistencia):

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


def generar_llenado_curso(boton_cancelar, boton_agregar_estudiante, boton_finalzar):

    principal_pag2 = QVBoxLayout()
    widget_principal_pag2 = QWidget()
    widget_principal_pag2.setLayout(principal_pag2)

    contenedor_form_curso = QVBoxLayout()
    widget_contenedor_form_curso = QWidget()
    widget_contenedor_form_curso.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 8px;
                                margin: 1px 1px;                            
                                }""")
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
    materia_input = QLineEdit()
    materia_input.setStyleSheet("""QLineEdit{
                        color: black;
                        font-family: sans-serif;
                        font-weight: bold;
                        border-radius: 8px;
                        border: 1px solid black;
                        min-height: 40px;
                        max-height: 40px;
                        max-width: 500px;
                        min-width: 500px;
    }""")
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

    table = QTableWidget()
    table.setFixedHeight(400)
    table.setRowCount(5)  # Establece el número de filas
    table.setColumnCount(3)  # Establece el número de columnas
    # table.setSizePolicy(QSizePolicy.Policy.Expanding,
    #                     QSizePolicy.Policy.Expanding)
    table.setHorizontalHeaderLabels(
        ["Nombres y Apellidos", "Documento", "Carrera"])
    table.horizontalHeader().setStyleSheet("""
                QHeaderView::section {
                    background-color: #FFFFFF;
                    color: black;
                    font-weight: bold;
                    border: none;
                    border-radius: 0px;
                }
            """)
    table.verticalHeader().setStyleSheet("""
                QHeaderView::section {
                    background-color: #FFFFFF;
                    color: black;
                    font-weight: bold;
                    border: none;
                    border-radius: 0px;
                    min-height: 30px;
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
    principal_pag2.addWidget(barra_botones_pag2(
        boton_cancelar, boton_agregar_estudiante, boton_finalzar))
    return widget_principal_pag2


def llenar_curso(boton_cancelar2, boton_biometria, boton_registrar):

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
    contenedro_pag3.addWidget(barra_botones_pag2(
        boton_cancelar2, boton_biometria, boton_registrar))

    return widget_contendor_pag3


def tomar_asistencia(boton_cancelar3, boton_asistio, boton_pdf):
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

    contenedor_cargar_camara = QHBoxLayout()
    widget_contenedor_cargar_camara = QWidget()
    widget_contenedor_cargar_camara.setLayout(contenedor_cargar_camara)
    widget_contenedor_cargar_camara.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 9px;
                                min-width: 800px;
                                max-width: 800px;
                                margin: 1px 1px;
                                }""")

    contenedor_toma_asistencia.addWidget(
        recomendacion, alignment=Qt.AlignmentFlag.AlignHCenter)
    contenedor_toma_asistencia.addWidget(
        widget_contenedor_cargar_camara, alignment=Qt.AlignmentFlag.AlignHCenter)

    contenedor_pag4.addWidget(widget_contenedor_toma_asistencia)
    contenedor_pag4.addWidget(barra_botones_pag2(
        boton_cancelar3, boton_asistio, boton_pdf))

    return widget_contenedor_pag4


def barra_botones_pag1(boton_cerrar, boton_crear_curso):

    # Creacion de contenerdor de datos y acciones basicas
    contenedor_ayuda = QHBoxLayout()
    widget_contenedor_ayuda = QWidget()
    widget_contenedor_ayuda.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 9px;
                                min-width: 800px;
                                margin: 1px 1px;
                                max-height: 60px;
                                min-height: 60px;
                                }""")
    widget_contenedor_ayuda.setLayout(contenedor_ayuda)

    boton_cerrar.setFixedWidth(150)
    boton_cerrar.setStyleSheet("""
                QPushButton {
                    background-color: #F75A50;
                    color: white;
                    border-radius: 5px;
                    padding: 1px;
                    font-size: 10px;
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
                    font-size: 10px;
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


def barra_botones_pag2(boton_cancelar, boton_agregar_estudiante, boton_finalzar):

    # Creacion de contenerdor de datos y acciones basicas
    contenedor_ayuda = QHBoxLayout()
    widget_contenedor_ayuda = QWidget()
    widget_contenedor_ayuda.setStyleSheet("""QWidget{
                                background-color: #DBE5D9;
                                border: 1px solid black;
                                border-radius: 9px;
                                min-width: 800px;
                                margin: 1px 1px;
                                max-height: 60px;
                                min-height: 60px;
                                }""")
    widget_contenedor_ayuda.setLayout(contenedor_ayuda)

    boton_cancelar.setFixedWidth(150)
    boton_cancelar.setStyleSheet("""
                QPushButton {
                    background-color: #F75A50;
                    color: white;
                    border-radius: 5px;
                    padding: 1px;
                    font-size: 10px;
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
                    font-size: 10px;
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

    boton_finalzar.setFixedWidth(150)
    boton_finalzar.setStyleSheet("""
                QPushButton {
                    background-color: #0A6EB0;
                    color: white;
                    border-radius: 5px;
                    padding: 1px;
                    font-size: 10px;
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
