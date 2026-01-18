from PySide6.QtWidgets import QWidget, QVBoxLayout, QApplication, QPushButton, QTextEdit, QMessageBox


class Validador(QWidget):
    def __init__(self):
        super().__init__()

        # título
        self.setWindowTitle("Validador")

        # layout
        layout = QVBoxLayout()
        self.setLayout(layout)

        # botones
        self.boton = QPushButton("Validar")
        self.boton.clicked.connect(self.validar)
        layout.addWidget(self.boton)

        # pantalla
        self.pantalla = QTextEdit()
        layout.addWidget(self.pantalla)

    # método para validar número
    def validar(self):
        try:
            texto = int(self.pantalla.toPlainText())
            if texto > 0:
                return QMessageBox.information(self, "Mensaje", "El número es positivo")
            elif texto < 0:
                return QMessageBox.information(self, "Mensaje", "El número es negativo")
            else:
                return QMessageBox.information(self, "Mensaje", "El número es un cero")
        except Exception:
            return QMessageBox.information(self, "Error", "INDICA UN NÚMERO VÁLIDO")


if __name__ == "__main__":
    app = QApplication([])
    ventana = Validador()
    ventana.show()
    app.exec()