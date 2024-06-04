from PyQt6.QtWidgets import QApplication, QWidget, QVBoxLayout, QPushButton, QScrollArea, QLabel, QLineEdit
from PyQt6.QtCore import Qt


class Ventana(QWidget):
    def __init__(self, elementos):
        super().__init__()
        self.setWindowTitle('Ventana con Scroll')
        self.setGeometry(100, 100, 500, 400)

        layout_principal = QVBoxLayout(self)
        scroll_area = QScrollArea(self)
        scroll_area.setWidgetResizable(True)
        layout_principal.addWidget(scroll_area)

        self.widget_contenedor = QWidget()
        self.layout_contenedor = QVBoxLayout(self.widget_contenedor)

        for elemento in elementos:
            self.agregar_elemento(elemento)

        scroll_area.setWidget(self.widget_contenedor)

        self.input_nuevo_elemento = QLineEdit(self)
        self.input_nuevo_elemento.setPlaceholderText("Dale Aqui un Nombre")
        boton_agregar = QPushButton('Agregar elemento', self)
        boton_agregar.clicked.connect(self.agregar_nuevo_elemento)

        layout_principal.addWidget(self.input_nuevo_elemento)
        layout_principal.addWidget(boton_agregar)

    def agregar_elemento(self, texto):
        label = QLabel(texto, self)
        boton = QPushButton('Editar', self)
        boton.clicked.connect(self.editar_elemento)
        self.layout_contenedor.addWidget(label)
        self.layout_contenedor.addWidget(boton)

    def agregar_nuevo_elemento(self):
        nuevo_elemento = self.input_nuevo_elemento.text()
        self.agregar_elemento(nuevo_elemento)
        self.input_nuevo_elemento.clear()

    def editar_elemento(self):
        print('Editar elemento')


if __name__ == "__main__":
    app = QApplication([])
    elementos = ['Elemento {}'.format(i) for i in range(1, 4)]
    ventana = Ventana(elementos)
    ventana.show()
    app.exec()
