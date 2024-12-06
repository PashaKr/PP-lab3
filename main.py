from PySide6.QtWidgets import QApplication, QWidget
import sys

if __name__ in '__main__':
    app = QApplication(sys.argv)
    app.setApplicationName('Test your memory!')

    w = QWidget()
    w.show()

    app.exec()