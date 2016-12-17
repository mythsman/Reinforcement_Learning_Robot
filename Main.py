import sys
from PyQt5 import QtWidgets
from Robot import Ui_Form
from RL import *
from time import time

class Main(QtWidgets.QWidget, Ui_Form):
	def __init__(self):
		super(Main, self).__init__()
		self.setupUi(self)	
		self.show()

	def calculate(self):
		if self.radioButton.isChecked() or self.radioButton_2.isChecked():
			time1 = time()
			if self.radioButton.isChecked():
				res=value_certain_iteration()
			elif self.radioButton_2.isChecked():
				res=value_random_iteration()
			time2=time()
			show = "Tables:\n"
			show += "%20d%20d%20d%20d%20d%20d\n" % (0, 1, 2, 3, 4, 5)
			for (line_num, line) in enumerate(res[0]):
				show += "Q%-2d: " % (line_num)
				for item in line:
					show += "%.3f:%.3f" % (item[0], item[1]) + "   "
				show += "\n"
			show+= "\nPolicy:\n"
			for item in res[1]:
				show += "%20d" % (item)
			show += "\n\nThe calculation result converges after %d iterations in %.3fms\n" % (
			len(res[0]) - 1, (time2 - time1) * 1000)
			self.plainTextEdit.setPlainText(show)
		else:
			time1 = time()
			if self.radioButton_3.isChecked():
				res=policy_certain_iteration()
			else:
				res=policy_random_iteration()
			time2 = time()
			show=""
			show += "\nRaw policy:\n"
			show += "%20d%20d%20d%20d%20d%20d" % (0,1,1,1,1,0)
			show += "\n\n"
			for (table_num,table) in enumerate(res):
				show += "\nTable %d:\n"%(table_num)
				show += "%20d%20d%20d%20d%20d%20d\n" % (0, 1, 2, 3, 4, 5)
				for (line_num, line) in enumerate(table[0]):
					show += "Q%-2d: " % (line_num)
					for item in line:
						show += "%.3f:%.3f" % (item[0], item[1]) + "   "
					show += "\n"
				show += "\nPolicy %d:\n"%(table_num)
				for item in table[1]:
					show += "%20d" % (item)
				show+="\n\n"
			show += "\n\nThe calculation result converges after %d iterations in %.3fms\n" % (
				len(res[0]) - 1, (time2 - time1) * 1000)
			self.plainTextEdit.setPlainText(show)


app = QtWidgets.QApplication(sys.argv)
main = Main()
sys.exit(app.exec_())
