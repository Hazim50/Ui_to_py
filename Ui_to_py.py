import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QFileDialog
import subprocess

class MyWindow(QWidget):
    def __init__(self):
        super().__init__()

        self.initUI()

    def initUI(self):
        self.setGeometry(300, 300, 250, 150)
        self.setWindowTitle('ui_to_py')

        button = QPushButton('Tıkla', self)
        button.clicked.connect(self.ui_to_py)
        button.move(75, 50)

    def ui_to_py(self):
        dosya_yolu, _ = QFileDialog.getOpenFileName(self, "UI Dosyasını Seç", "", "UI Dosyaları (*.ui)")
        if dosya_yolu:
            self.uiyi_py_cevir(dosya_yolu)
        else:
            print("UI dosyası seçilmedi.")

    def uiyi_py_cevir(self, dosya_yolu):
        py_dosya_adi = dosya_yolu.split(".")[0] + ".py"
        subprocess.run(['pyuic5', '-x', dosya_yolu, '-o', py_dosya_adi])



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MyWindow()
    window.show()
    sys.exit(app.exec_())
