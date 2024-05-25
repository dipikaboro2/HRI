import sys
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSlot

def window():
   app = QApplication(sys.argv)
   widget = QWidget()
   
   g_c = QPushButton(widget)
   g_c.setText("CLose\nGripper")
   g_c.move(100,10)
   g_c.clicked.connect(g_c_clicked)

   g_o = QPushButton(widget)
   g_o.setText("Open\nGripper")
   g_o.move(100, 60)
   g_o.clicked.connect(g_o_clicked)

   y_i = QPushButton(widget)
   y_i.setText("y +")
   y_i.move(110, 120)
   y_i.clicked.connect(y_i_clicked)

   y_d = QPushButton(widget)
   y_d.setText("y -")
   y_d.move(110, 160)
   y_d.clicked.connect(y_d_clicked)

   x_i = QPushButton(widget)
   x_i.setText("x +")
   x_i.move(135, 140)
   x_i.clicked.connect(x_i_clicked)

   x_d = QPushButton(widget)
   x_d.setText("x -")
   x_d.move(75, 140)
   x_d.clicked.connect(x_d_clicked)

   z_i = QPushButton(widget)
   z_i.setText("z +")
   z_i.move(190, 130)
   z_i.clicked.connect(z_i_clicked)

   z_d = QPushButton(widget)
   z_d.setText("z -")
   z_d.move(190, 150)
   z_d.clicked.connect(z_d_clicked)

   widget.setGeometry(50,50,320,200)
   widget.setWindowTitle("Sawyer Pose Control")
   widget.show()
   sys.exit(app.exec_())
"""
   j_0_i = QPushButton(widget)
   j_0_i.setText("J0 +")
   j_0_i.move(10,480)
   j_0_i.clicked.connect(j_0_i_clicked)

   j_0_d = QPushButton(widget)
   j_0_d.setText("J0 -")
   j_0_d.move(10, 500)
   j_0_d.clicked.connect(j_0_d_clicked)

   j_1_i = QPushButton(widget)
   j_1_i.setText("J1 +")
   j_1_i.move(10,420)
   j_1_i.clicked.connect(j_1_i_clicked)

   j_1_d = QPushButton(widget)
   j_1_d.setText("J1 -")
   j_1_d.move(10, 440)
   j_1_d.clicked.connect(j_1_d_clicked)

   j_2_i = QPushButton(widget)
   j_2_i.setText("J2 +")
   j_2_i.move(10,360)
   j_2_i.clicked.connect(j_2_i_clicked)

   j_2_d = QPushButton(widget)
   j_2_d.setText("J2 -")
   j_2_d.move(10, 380)
   j_2_d.clicked.connect(j_2_d_clicked)

   j_3_i = QPushButton(widget)
   j_3_i.setText("J3 +")
   j_3_i.move(10, 300)
   j_3_i.clicked.connect(j_3_i_clicked)

   j_3_d = QPushButton(widget)
   j_3_d.setText("J3 -")
   j_3_d.move(10, 320)
   j_3_d.clicked.connect(j_3_d_clicked)

   j_4_i = QPushButton(widget)
   j_4_i.setText("J4 +")
   j_4_i.move(10, 240)
   j_4_i.clicked.connect(j_4_i_clicked)

   j_4_d = QPushButton(widget)
   j_4_d.setText("J4 -")
   j_4_d.move(10, 260)
   j_4_d.clicked.connect(j_4_d_clicked)

   j_5_i = QPushButton(widget)
   j_5_i.setText("J5 +")
   j_5_i.move(10, 180)
   j_5_i.clicked.connect(j_5_i_clicked)

   j_5_d = QPushButton(widget)
   j_5_d.setText("J5 -")
   j_5_d.move(10, 200)
   j_5_d.clicked.connect(j_5_d_clicked)

   j_6_i = QPushButton(widget)
   j_6_i.setText("J6+")
   j_6_i.move(10, 120)
   j_6_i.clicked.connect(j_6_i_clicked)

   j_6_d = QPushButton(widget)
   j_6_d.setText("J6-")
   j_6_d.move(10, 140)
   j_6_d.clicked.connect(j_6_d_clicked)

   """


def j_0_i_clicked():
   print("Command: right_j0 increase")

def j_0_d_clicked():
   print("Command: right_j0 decrease")

def j_1_i_clicked():
   print("Command: right_j1 increase")

def j_1_d_clicked():
   print("Command: right_j1 decrease")

def j_2_i_clicked():
   print("Command: right_j2 increase")

def j_2_d_clicked():
   print("Command: right_j2 decrease")

def j_3_i_clicked():
   print("Command: right_j3 increase")

def j_3_d_clicked():
   print("Command: right_j3 decrease")

def z_i_clicked():
   print("Command: z increase")

def z_d_clicked():
   print("Command: z decrease")

def y_i_clicked():
   print("Command: y increase")

def y_d_clicked():
   print("Command: y decrease")

def x_i_clicked():
   print("Command: x increase")

def x_d_clicked():
   print("Command: x decrease")

def g_c_clicked():
   print("right gripper close")

def g_o_clicked():
   print("right gripper open")


if __name__ == '__main__':
   window()