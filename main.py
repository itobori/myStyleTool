try:
	from PySide6 import QtCore, QtGui, QtWidgets
	from shiboken6 import wrapInstance
except:
	from PySide2 import QtCore, QtGui, QtWidgets
	from shiboken2 import wrapInstance

# from PySide2 import QtCore, QtGui, QtWidgets
# from shiboken2 import wrapInstance
import maya.OpenMayaUI as omui

ROOT_RESOURCE_DIR = 'C:/Users/itobo/OneDrive/เอกสาร/maya/2024/scripts/myStlyeTool/recouse'

class MyStyleToolDialog(QtWidgets.QDialog):
	def __init__(self,parent=None):
		super().__init__(parent)
		self.setWindowTitle('My Tool')
		self.resize(300,300)

		self.mainLayout = QtWidgets.QVBoxLayout()
		self.setLayout(self.mainLayout)
		self.setStyleSheet('background-color: #C92448;')

		self.imageLabel = QtWidgets.QLabel()
		self.imagePixmap = QtGui.QPixmap(f"{ROOT_RESOURCE_DIR}/image/Spiderman-Logo.png")
		scaled_pixmap = self.imagePixmap.scaled(
			QtCore.QSize(164,164),
			QtCore.Qt.KeepAspectRatio,
			QtCore.Qt.SmoothTransformation
		)

		self.imageLabel.setPixmap(scaled_pixmap)
		self.imageLabel.setAlignment(QtCore.Qt.AlignCenter)


		self.mainLayout.addWidget(self.imageLabel)

		self.nameLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.nameLayout)
		self.nameLabel = QtWidgets.QLabel('name')
		self.nameLineEdit = QtWidgets.QLineEdit()
		self.nameLineEdit.setStyleSheet(
			'''
				QLineEdit {
					color : back;
					background-color: white;
					font-size: 29px;
					font-weight: bold;


				}
			'''
			)
		self.nameLayout.addWidget(self.nameLabel)
		self.nameLayout.addWidget(self.nameLineEdit)


		self.buttonLayout = QtWidgets.QHBoxLayout()
		self.mainLayout.addLayout(self.buttonLayout)
		self.createButton = QtWidgets.QPushButton('Create')
		self.createButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #023EA6;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					padding: 8px;
					font-family : Dino Care;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: #40CAFF;

				}
				QPushButton:pressed {
					background-color: white;
				}

			'''
		)
		self.cancleButton = QtWidgets.QPushButton('Cancle')
		self.cancleButton.setStyleSheet(
			'''
				QPushButton {
					background-color: #80001F;
					color: white;
					border-radius: 10px;
					font-size: 16px;
					padding: 8px;
					font-family : Dino Care;
					font-weight: bold;
				}
				QPushButton:hover {
					background-color: #FF0000;

				}
				QPushButton:pressed {
					background-color: white;
				}

			'''
		)
		self.buttonLayout.addWidget(self.createButton)
		self.buttonLayout.addWidget(self.cancleButton)


		self.mainLayout.addStretch()

def run():
	global ui
	try:
		ui.close()
	except:
		pass

	ptr = wrapInstance(int(omui.MQtUtil.mainWindow()),QtWidgets.QWidget)	
	ui = MyStyleToolDialog(parent=ptr)
	ui.show()	
