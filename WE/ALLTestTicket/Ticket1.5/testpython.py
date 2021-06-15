import sys
from PySide.QtCore import *
from PySide.QtGui import *
from PySide.QtDeclarative import QDeclarativeView

# สร้างโปรแกรม  Qt แล้วใช้  QDeclarative แสดง
app = QApplication(sys.argv)
view = QDeclarativeView()

# โยงไฟล์ QML เข้ามาใช้งาน
url = QUrl('view.qml')

# กำหนดค่า view แล้วแสดง
view.setSource(url)
view.show()

sys.exit(app.exec_())
