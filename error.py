from PyQt5 import QtWidgets


def error_box(text):
    msg = QtWidgets.QMessageBox()
    msg.setIcon(QtWidgets.QMessageBox.Critical)
    msg.setText("Error")
    msg.setInformativeText(text)
    msg.setWindowTitle("Error")
    msg.exec_()
