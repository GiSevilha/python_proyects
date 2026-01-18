from PySide6.QtCore import Qt
from PySide6.QtGui import QAction, QIcon, QKeySequence
from PySide6.QtWidgets import QMainWindow, QApplication, QPushButton, QMessageBox, QWidget, QVBoxLayout, QMenuBar, \
    QMenu, QToolBar


class MenuBar(QMainWindow):
    def __init__(self):
        super().__init__()

        # título
        self.setWindowTitle("Aplicación Menu Bar")
        self.setGeometry(100, 100, 600, 400)

        # crear un widget central con un layout principal
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        layout = QVBoxLayout()
        central_widget.setLayout(layout)

        # crear menu
        menu = QMenuBar()
        self.setMenuBar(menu)

        # crear opciones dentro del menu
        file_menu = QMenu("Archivo")
        edit_menu = QMenu("Editar")
        menu.addMenu(file_menu)
        menu.addMenu(edit_menu)
        new_action = QAction("Nuevo", self)
        new_action.triggered.connect(lambda: self.mensaje("Nuevo seleccionado."))
        open_action = QAction("Abrir", self)
        open_action.triggered.connect(lambda: self.mensaje("Abrir seleccionado."))
        save_action = QAction("Guardar", self)
        save_action.triggered.connect(lambda: self.mensaje("Guardar seleccionado."))
        exit_action = QAction("Salir", self)
        exit_action.triggered.connect(lambda: self.mensaje("Salir seleccionado."))
        exit_action.setShortcut(QKeySequence("Ctrl+Q"))
        restaurar_action = QAction("Restaurar", self)
        restaurar_action.triggered.connect(lambda: self.mensaje("Restaurado."))

        edit_menu.addAction(restaurar_action)
        file_menu.addAction(new_action)
        file_menu.addAction(open_action)
        file_menu.addAction(save_action)
        file_menu.addAction(exit_action)

        # botón
        self.boton = QPushButton("Presioname")
        self.boton.clicked.connect(lambda: self.mensaje("El botón ha sido presionado"))
        layout.addWidget(self.boton)

        # menu contextual
        self.setContextMenuPolicy(Qt.CustomContextMenu)
        self.customContextMenuRequested.connect(self.show_context_menu)

        # barra de herramientas
        toolbar = QToolBar("Barra de herramientas", self)
        self.addToolBar(toolbar)
        toolbar_action = QAction(QIcon.fromTheme("help-browser"), "Mostrar mensaje", self)
        toolbar_action_dos = QAction(QIcon.fromTheme("folder"), "Abrir carpeta", self)
        toolbar_action_dos.setShortcut(QKeySequence("Ctrl+F"))
        toolbar_action.setShortcut(QKeySequence("Ctrl+M"))
        toolbar_action_dos.triggered.connect(lambda: self.mensaje("¡Carpeta abierta con suceso!"))
        toolbar_action.triggered.connect(lambda: self.mensaje("Mensaje desde la barra de herramientas"))
        toolbar.addAction(toolbar_action)
        toolbar.addAction(toolbar_action_dos)

    # método para crear pop up de aviso
    def mensaje(self, message):
        error = QMessageBox.information(self, "Mensaje", message)

    def show_context_menu(self, position):
        context_menu = QMenu()
        context_action = QAction("Accion contextual", self)
        context_menu.addAction(context_action)

        context_menu.exec(self.mapToGlobal(position))


if __name__ == "__main__":
    app = QApplication([])
    window = MenuBar()
    window.show()
    app.exec()