from PySide6.QtCore import Qt
from PySide6.QtGui import QAction
from PySide6.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QToolBar, QDialog, QLabel, QPushButton, \
    QLineEdit, QMessageBox, QHBoxLayout


# Ventana de diálogo
class DialogoAyuda(QDialog):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ayuda")
        self.setFixedSize(350, 200)

        layout = QVBoxLayout()

        texto = QLabel(
            "Esta aplicación permite:\n\n"
            "- Escribir texto en una caja.\n"
            "- Limpiar el texto usando la barra de herramientas.\n"
            "- Mostrar un mensaje emergente.\n\n"
            "Ejemplo creado con PySide6."
        )
        texto.setAlignment(Qt.AlignCenter)
        boton_cerrar = QPushButton("Cerrar")
        boton_cerrar.clicked.connect(self.close)

        layout.addWidget(texto)
        layout.addWidget(boton_cerrar)
        self.setLayout(layout)


# Ventana principal
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Ejemplo PySide6")
        self.resize(500, 300)

        # Widget central
        self.line_edit = QLineEdit()
        self.line_edit.setPlaceholderText("Escribe algo aquí...")

        contenedor = QWidget()
        layout = QVBoxLayout(contenedor) # para que la caja de texto se ajuste automáticamente al tamaño de la ventana
        layout.addWidget(self.line_edit)
        self.setCentralWidget(contenedor)

        # Crear barra de herramientas
        self.crear_toolbar()

        # Crear menú
        self.crear_menu()

    # Barra de herramientas
    def crear_toolbar(self):
        toolbar = QToolBar("Herramientas")
        self.addToolBar(toolbar)

        # Acción limpiar
        accion_limpiar = QAction("Limpiar", self)
        accion_limpiar.triggered.connect(self.limpiar_texto)
        toolbar.addAction(accion_limpiar)

        # Acción mostrar mensaje
        accion_mensaje = QAction("Mostrar mensaje", self)
        accion_mensaje.triggered.connect(self.mostrar_mensaje)
        toolbar.addAction(accion_mensaje)

    # Menú
    def crear_menu(self):
        menu_bar = self.menuBar()
        menu_ayuda = menu_bar.addMenu("Ayuda")

        accion_ayuda = QAction("Ver ayuda", self)
        accion_ayuda.triggered.connect(self.mostrar_dialogo_ayuda)
        menu_ayuda.addAction(accion_ayuda)

    # Funciones
    def limpiar_texto(self):
        self.line_edit.clear()

    def mostrar_mensaje(self):
        texto = self.line_edit.text()
        if texto.strip() == "":
            texto = "No escribiste ningún texto."
        QMessageBox.information(self,"Mensaje", texto)

    def mostrar_dialogo_ayuda(self):
        dialogo = DialogoAyuda()
        dialogo.exec()


# ejecución principal
if __name__ == "__main__":
    app = QApplication([])
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()
