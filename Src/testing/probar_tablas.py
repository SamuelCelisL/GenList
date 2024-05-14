from PyQt6.QtWidgets import QApplication, QWidget, QTableWidget, QTableWidgetItem, QVBoxLayout
import sys


class Window(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("PyQt6 Table")
        self.create_table()

    def create_table(self):
        self.table = QTableWidget()
        self.table.setRowCount(5)  # Establece el número de filas
        self.table.setColumnCount(3)  # Establece el número de columnas

        for i in range(5):  # Rellena la tabla con datos de ejemplo
            for j in range(3):
                self.table.setItem(
                    i, j, QTableWidgetItem(f"Celda {i+1}, {j+1}"))

        self.layout = QVBoxLayout()
        self.layout.addWidget(self.table)
        self.setLayout(self.layout)


app = QApplication(sys.argv)
window = Window()
window.show()
sys.exit(app.exec())
