# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'reader.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtCore import QDate
from PyQt5.QtWidgets import *
import time
import sys
import os
import subprocess
import urllib.request
from bs4 import BeautifulSoup


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(579, 568)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.centralwidget)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.verticalLayout = QtWidgets.QVBoxLayout()
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.groupBox.setFont(font)
        self.groupBox.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.groupBox.setObjectName("groupBox")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.frame_2 = QtWidgets.QFrame(self.groupBox)
        self.frame_2.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame_2.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame_2.setObjectName("frame_2")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.frame_2)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.lineEdit_2 = QtWidgets.QLineEdit(self.frame_2)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.horizontalLayout_2.addWidget(self.lineEdit_2)
        self.pushButton = QtWidgets.QPushButton(self.frame_2)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.gridLayout_3.addWidget(self.frame_2, 1, 0, 1, 1)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox)
        self.pushButton_2.setMinimumSize(QtCore.QSize(60, 40))
        self.pushButton_2.setMaximumSize(QtCore.QSize(60, 40))
        self.pushButton_2.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.pushButton_2.setObjectName("pushButton_2")
        self.gridLayout_3.addWidget(self.pushButton_2, 2, 0, 1, 1)
        self.frame = QtWidgets.QFrame(self.groupBox)
        self.frame.setFrameShape(QtWidgets.QFrame.StyledPanel)
        self.frame.setFrameShadow(QtWidgets.QFrame.Raised)
        self.frame.setObjectName("frame")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.frame)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.lineEdit = QtWidgets.QLineEdit(self.frame)
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout.addWidget(self.lineEdit)
        self.label_2 = QtWidgets.QLabel(self.frame)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_2.setFont(font)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.gridLayout_3.addWidget(self.frame, 0, 0, 1, 1)
        self.verticalLayout.addWidget(self.groupBox)
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.gridLayout = QtWidgets.QGridLayout(self.tab)
        self.gridLayout.setObjectName("gridLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab)
        font = QtGui.QFont()
        font.setPointSize(14)
        self.tableWidget.setFont(font)
        self.tableWidget.setTabletTracking(False)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(2)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        font = QtGui.QFont()
        font.setPointSize(14)
        item.setFont(font)
        self.tableWidget.setHorizontalHeaderItem(1, item)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(True)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(220)
        self.tableWidget.horizontalHeader().setHighlightSections(True)
        self.tableWidget.horizontalHeader().setSortIndicatorShown(True)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(True)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(True)
        self.tableWidget.verticalHeader().setSortIndicatorShown(True)
        self.tableWidget.verticalHeader().setStretchLastSection(True)
        self.gridLayout.addWidget(self.tableWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.tab_2)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.listWidget = QtWidgets.QListWidget(self.tab_2)
        self.listWidget.setObjectName("listWidget")
        self.gridLayout_2.addWidget(self.listWidget, 0, 0, 1, 1)
        self.tabWidget.addTab(self.tab_2, "")
        self.verticalLayout.addWidget(self.tabWidget)
        self.gridLayout_4.addLayout(self.verticalLayout, 0, 0, 1, 1)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actiondd = QtWidgets.QAction(MainWindow)
        self.actiondd.setObjectName("actiondd")

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    # 自动生成代码 用来设置窗体中控件默认值
    def retranslateUi(self, MainWindow):
        # 当前年份 月份
        tm_mon = time.localtime().tm_mon
        tm_mon = tm_mon if tm_mon > 9 else '0' + str(tm_mon)
        strDate = str(time.localtime().tm_year) + '-' + str(tm_mon)

        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.groupBox.setTitle(_translate("MainWindow", "抓取设置"))
        self.label.setText(_translate("MainWindow", "请选择抓取数："))
        # 设置默认期数
        self.lineEdit.setText(_translate("MainWindow", strDate))
        self.label_2.setText(_translate("MainWindow", "（期数范围01-24）"))
        # 设置默认路径为当前项目路径
        self.lineEdit_2.setText(_translate("MainWindow", os.getcwd()))
        self.label_3.setText(_translate("MainWindow", "请选择保存路径："))
        self.pushButton.setText(_translate("MainWindow", "选择"))
        self.pushButton_2.setText(_translate("MainWindow", "确定"))
        # 获取表格的第一列
        item = self.tableWidget.horizontalHeaderItem(0)
        # 设置表格第一列的标题
        item.setText(_translate("MainWindow", "期数"))
        # 获取表格的第二列
        item = self.tableWidget.horizontalHeaderItem(1)
        # 设置表格第二列的标题
        item.setText(_translate("MainWindow", "名称"))

        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "按期数显示"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "按名称显示"))
        self.actiondd.setText(_translate("MainWindow", "dd "))

        # 为选择按钮绑定事件
        self.pushButton.clicked.connect(self.msg)
        # 确定按钮
        self.pushButton_2.clicked.connect(self.getDatas)

    # 从网页提取数据
    def urlTosoup(self, url):
        response = urllib.request.urlopen(url)
        html = response.read()
        soup = BeautifulSoup(html, 'html.parser')
        return soup

    # 抓取数据
    def getData(self, url, path):
        soup = self.urlTosoup(url)
        link = soup.select('.maglisttitle a')
        path = path + '/' + self.date + '/'
        # 路径是否存在
        if not os.path.isdir(path):
            # 创建路径
            os.mkdir(path)
        for item in link:
            # 获取遍历到的具体文章地址
            articleUrl = self.baseurl + item['href']
            # 生成BeautifulSoup对象
            articleSoup = self.urlTosoup(articleUrl)
            # 获取文章标题
            title = str(articleSoup.find("h1")).lstrip("<h1>").rstrip("</h1>")
            # 获取文章作者
            author = articleSoup.find(id="pub_date").get_text().strip()
            # 设置文章保存路径（包括文章名）
            fileName = path + title + '.txt'
            # 打开或者创建文件
            newFile = open(fileName, "w")
            # 向文件中写入标题并换行
            newFile.write("<<" + title + ">>\n\n")
            # 向文件中写入作者并换行
            newFile.write(author + "\n\n")
            # 获取文章所有内容
            content = articleSoup.select(".blkContainerSblkCon p")
            # 遍历获取到的内容
            for c in content:
                # 获取文章内容
                text = c.text
                # 向文件中写入内容
                newFile.write(text)
            # 关闭文件
            newFile.close()
        QMessageBox.about(None, "提示", self.date + "的读者文章保存完成")

    # 抓取文章
    def getDatas(self):
        try:
            try:
                # 记录用户选择的期数
                self.date = self.lineEdit.text()
                self.baseurl = 'http://www.52duzhe.com/' + self.date.replace('-', '_') + '/'
                urlList = self.baseurl + 'index.html'
                print(urlList)
                self.getData(urlList, self.lineEdit_2.text())
            except Exception as e:
                print(e)
            self.getFiles()
            self.bindList()
            self.bindTable()
            # 绑定列表单击方法
            self.listWidget.itemClicked.connect(self.itemClick)
            # 绑定表格单击方法
            self.tableWidget.itemClicked.connect(self.tableClick)
        except Exception:
            QMessageBox.about(None, "提示", "没有数据请重新设置期数...")

    # 将文件显示在Table中
    def bindTable(self):
        for i in range(0, len(self.list)):
            # 添加新行
            self.tableWidget.insertRow(i)
            # 设置第一列为期数
            self.tableWidget.setItem(i, 0, QtWidgets.QTableWidgetItem(self.lineEdit.text()))
            # 设置第二列为文件名
            self.tableWidget.setItem(i, 1, QtWidgets.QTableWidgetItem(self.list[i]))

    # 按名称和图标显示《读者》文章
    def bindList(self):
        for i in range(0, len(self.list)):
            # 创建列表项
            self.item = QtWidgets.QListWidgetItem(self.listWidget)
            # 设置列表图标
            self.item.setIcon(QtGui.QIcon('note.ico'))
            # 显示5个字符
            self.item.setText(str(self.list[i][0:5]) + '...')
            # 设置提示文字
            self.item.setToolTip(self.list[i])
            # 设置是否选中
            self.item.setFlags(QtCore.Qt.ItemIsSelectable | QtCore.Qt.ItemIsEnabled)

    # 列表单击
    def itemClick(self, item):
        open_file(self.lineEdit_2.text() + '/' + self.lineEdit.text() + '/' + item.toolTip())

    # 表格单击
    def tableClick(self, item):
        open_file(self.lineEdit_2.text() + '/' + self.lineEdit.text() + '/' + item.text())

    # 获取指定路径下的所有文件
    def getFiles(self):
        self.list = os.listdir(self.lineEdit_2.text() + '/' + self.lineEdit.text())

    # 选择保存路径
    def msg(self):
        try:
            # 选择的文件夹绝对路径
            # 参数
            # 2 对话框标题
            # 3 对话框打开后默认的路径
            self.dir_path = QFileDialog.getExistingDirectory(None, "选择路径", os.getcwd())
            # 显示选择的保存路径
            self.lineEdit_2.setText(self.dir_path)

            self.getFiles()
            self.bindList()
            self.bindTable()
            # 绑定列表单击方法
            self.listWidget.itemClicked.connect(self.itemClick)
            # 绑定表格单击方法
            self.tableWidget.itemClicked.connect(self.tableClick)
        except Exception as e:
            print(e)


def open_file(filename):
    if sys.platform == "win32":
        os.startfile(filename)
    else:
        opener = "open" if sys.platform == "darwin" else "xdg-open"
        subprocess.call([opener, filename])


if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
