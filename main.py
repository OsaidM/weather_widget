import sys
from PySide6 import QtGui, QtCore, QtWidgets

WINDOW_WIDTH = 300
WINDOW_HEIGHT = 400

app = QtWidgets.QApplication([])

window = QtWidgets.QWidget()
# Get the primary screen
primary_screen = QtWidgets.QApplication.primaryScreen()
# window.setWindowOpacity(0.4)
window.setWindowFlag(QtCore.Qt.FramelessWindowHint, True)
window.setAttribute(QtCore.Qt.WA_TranslucentBackground)
if hasattr(QtCore.Qt, 'AA_EnableHighDpiScaling'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_EnableHighDpiScaling, True)
if hasattr(QtCore.Qt, 'AA_UseHighDpiPixmaps'):
    QtWidgets.QApplication.setAttribute(QtCore.Qt.AA_UseHighDpiPixmaps, True)
if sys.platform == 'win32':
    # window.setStyleSheet("QMainWindow::separator {background-color: red; width: 2px; height: 2px;}")
    window.setStyleSheet("""QWidget {background-color: rgba(0, 0, 0, 0.3); border: 1px solid black; border-radius: 10px;}
                            QLabel {color: white;}""")
else:
    window.setStyleSheet("border-radius: 10px; border-color: red; border-style: solid; border-width: 2px;")

layout = QtWidgets.QVBoxLayout(window)
# Get the screen size
screen_size = primary_screen.availableGeometry()

# Display the screen size in a message box
msg = QtWidgets.QLabel(f"The screen size is {screen_size.width()} x {screen_size.height()}.")

layout.addWidget(msg)
window.move((screen_size.width() - WINDOW_WIDTH) - 20, 100)
window.resize(WINDOW_WIDTH, WINDOW_HEIGHT)
window.show()

app.exec()
