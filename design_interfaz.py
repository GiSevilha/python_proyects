import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import QMainWindow, QApplication, QMessageBox, QMenu, QFileDialog
from ui.Interfaz import Ui_MainWindow

class Interfaz(QMainWindow):
    def __init__(self):
        super().__init__()

        # Establezca como interfaz la variable que estoy creando
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        # conectar botón
        self.ui.btn.clicked.connect(lambda : self.cambiar_texto("¡El texto ha sido cambiado correctamente!"))

        # decir al objeto texto que contralaremos el menú
        self.ui.texto.setContextMenuPolicy(Qt.CustomContextMenu)
        self.ui.texto.customContextMenuRequested.connect(self.mostrar_menu_contextual)

        # opción abrir dentro del menu
        self.ui.actionAbrir.triggered.connect(self.abrir_archivo)

        # opción salir dentro del menu
        self.ui.actionSalir.triggered.connect(self.close)

        # opción acerca de dentro del menu
        self.ui.actionAcerca_de.triggered.connect(self.mostrar_ayuda)

    def cambiar_texto(self, mensaje):
        # 1. Creamos la pregunta
        respuesta = QMessageBox.question(self, "Confirmación", "¿Estás seguro de que quieres copiar el texto al label?",
        QMessageBox.Yes | QMessageBox.No)

        # 2. Evaluamos la respuesta del usuario
        if respuesta == QMessageBox.Yes:
            contenido = self.ui.texto.toPlainText()
            self.ui.txt.setText(contenido)
        else:
            print("Acción cancelada por el usuario")

    def mostrar_menu_contextual(self, pos):
        menu = QMenu()

        copiar_action = menu.addAction("Copiar")
        pegar_action = menu.addAction("Pegar")
        limpiar_action = menu.addAction("Limpiar")

        copiar_action.triggered.connect(self.copiar)
        pegar_action.triggered.connect(self.pegar)
        limpiar_action.triggered.connect(self.limpiar)

        menu.exec(self.ui.texto.mapToGlobal(pos))

    def copiar(self):
        self.ui.texto.copy()

    def pegar(self):
        self.ui.texto.paste()

    def limpiar(self):
        self.ui.texto.clear()

    def mostrar_ayuda(self):
        QMessageBox.about(self, "Sobre esta app", "Esta es una interfaz de práctica creada con PySide6 y Qt Designer.")

    def abrir_archivo(self):
        # getOpenFileName devuelve una tupla (ruta, filtro)
        nombre_archivo, _ = QFileDialog.getOpenFileName(self, "Abrir Archivo", "",
                                                        "Archivos de texto (*.txt);;Todos los archivos (*)")

        if nombre_archivo:
            print(f"Has seleccionado: {nombre_archivo}")
            # Aquí es donde usarías QFile para leer el contenido si quisieras


if __name__ == "__main__":
    app = QApplication([])
    ventana = Interfaz()
    ventana.show()
    sys.exit(app.exec())
