from PySide6.QtCore import QTimer
from PySide6.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QApplication, QMenuBar, QMenu, QLabel, QPushButton, \
    QMessageBox


class AplicacionIntegradora(QMainWindow):
    def __init__(self):
        super().__init__()

        # título
        self.setWindowTitle("Aplicación Integradora")
        self.setGeometry(200, 200, 300, 200)

        # contador
        self.contador = 0
        self.label = QLabel("Tiempo: 0 s")
        self.label.setStyleSheet("font-size: 20px;")

        # botón principal
        self.boton = QPushButton("Iniciar / Pausar contador")
        self.boton.clicked.connect(self.iniciar_pausar)

        # timer
        self.timer = QTimer()
        self.timer.timeout.connect(self.actualizar_contador)

        # layout central
        contenedor = QWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.label)
        layout.addWidget(self.boton)
        contenedor.setLayout(layout)
        self.setCentralWidget(contenedor)

        # menu
        menu = self.menuBar()

        menu_archivo = menu.addMenu("Archivo")
        menu_ayuda = menu.addMenu("Ayuda")

        opcion_reset = menu_archivo.addAction("Reiniciar contador")
        opcion_reset.triggered.connect(self.reiniciar)

        opcion_salir = menu_archivo.addAction("Salir")
        opcion_salir.triggered.connect(self.close)

        opcion_info = menu_ayuda.addAction("Acerca de")
        opcion_info.triggered.connect(self.mostrar_info)

    # métodos
    def iniciar_pausar(self):
        if self.timer.isActive():
            self.timer.stop()
        else:
            self.timer.start(1000) # 1 segundo

    def actualizar_contador(self):
        self.contador += 1
        self.label.setText(f"Tiempo: {self.contador} s")

    def reiniciar(self):
        self.contador = 0
        self.label.setText("Tiempo: 0 s")
        QMessageBox.information(self, "Reinicio", "El contador ha sido reiniciado")

    def mostrar_info(self):
        QMessageBox.information(
            self, "Acerca de", "Aplicación integradora con menú, botón, contador y QTimer"
        )


if __name__ == "__main__":
    app = QApplication([])
    ventana = AplicacionIntegradora()
    ventana.show()
    app.exec()
