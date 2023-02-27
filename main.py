from PyQt5.QtWidgets import QApplication, QMainWindow, QTableWidgetItem, QWidget, QMessageBox, QInputDialog, QFileDialog
from PyQt5 import uic, QtWidgets, QtCore, QtGui, QtWidgets
import sys
import sqlite3
import csv

# при отсутствии базы данных, создается
con = sqlite3.connect("subjects.sqlite")
cur = con.cursor()
request = "SELECT * FROM sqlite_master where type='table';"
tables = cur.execute(request).fetchall()
if not tables:
    requests = []
    requests.append("""CREATE TABLE coefficients (
                    ID          INTEGER PRIMARY KEY AUTOINCREMENT
                                        UNIQUE
                                        NOT NULL,
                    coeff       INTEGER NOT NULL,
                    description STRING  NOT NULL
                );""")
    requests.append("""CREATE TABLE marks (
                    ID         INTEGER PRIMARY KEY AUTOINCREMENT
                                    UNIQUE
                                    NOT NULL,
                    mark       INTEGER NOT NULL,
                    coeff_ID   INTEGER NOT NULL,
                    subject_ID INTEGER NOT NULL
                );""")
    requests.append("""CREATE TABLE subjects (
                    ID   INTEGER PRIMARY KEY AUTOINCREMENT
                                UNIQUE
                                NOT NULL,
                    name STRING  UNIQUE
                                NOT NULL
                );""")
    for i in requests:
        cur.execute(i)
    requests = []
    requests.append("INSERT INTO coefficients VALUES(1, 1, 'Работа на уроке')")
    requests.append("INSERT INTO coefficients VALUES(2, 1, 'Домашняя работа')")
    requests.append("INSERT INTO coefficients VALUES(3, 2, 'Самостоятельная работа')")
    requests.append("INSERT INTO coefficients VALUES(4, 3, 'Контрольная работа')")
    requests.append("INSERT INTO coefficients VALUES(5, 3, 'Диктант')")
    for i in requests:
        cur.execute(i)
        con.commit()


# интерфейс основной формы
class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1012, 605)
        font = QtGui.QFont()
        font.setPointSize(8)
        MainWindow.setFont(font)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.subject_choose_CBox = QtWidgets.QComboBox(self.centralwidget)
        self.subject_choose_CBox.setGeometry(QtCore.QRect(10, 10, 171, 31))
        self.subject_choose_CBox.setObjectName("subject_choose_CBox")
        self.sort_CBox_main = QtWidgets.QComboBox(self.centralwidget)
        self.sort_CBox_main.setGeometry(QtCore.QRect(610, 40, 161, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.sort_CBox_main.setFont(font)
        self.sort_CBox_main.setObjectName("sort_CBox_main")
        self.sort_CBox_main.addItem("")
        self.sort_CBox_main.addItem("")
        self.sort_CBox_main.addItem("")
        self.checkBox = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox.setGeometry(QtCore.QRect(820, 10, 151, 17))
        self.checkBox.setChecked(True)
        self.checkBox.setAutoExclusive(False)
        self.checkBox.setObjectName("checkBox")
        self.checkBox_2 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_2.setGeometry(QtCore.QRect(820, 30, 151, 17))
        self.checkBox_2.setChecked(True)
        self.checkBox_2.setAutoExclusive(False)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_3 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_3.setGeometry(QtCore.QRect(820, 50, 151, 17))
        self.checkBox_3.setChecked(True)
        self.checkBox_3.setAutoExclusive(False)
        self.checkBox_3.setObjectName("checkBox_3")
        self.checkBox_4 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_4.setGeometry(QtCore.QRect(820, 70, 151, 17))
        self.checkBox_4.setChecked(True)
        self.checkBox_4.setAutoExclusive(False)
        self.checkBox_4.setObjectName("checkBox_4")
        self.checkBox_5 = QtWidgets.QCheckBox(self.centralwidget)
        self.checkBox_5.setGeometry(QtCore.QRect(820, 90, 151, 17))
        self.checkBox_5.setChecked(True)
        self.checkBox_5.setAutoExclusive(False)
        self.checkBox_5.setObjectName("checkBox_5")
        self.subj_name_label = QtWidgets.QLabel(self.centralwidget)
        self.subj_name_label.setGeometry(QtCore.QRect(190, 10, 211, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.subj_name_label.setFont(font)
        self.subj_name_label.setObjectName("subj_name_label")
        self.ascending_btn_main = QtWidgets.QPushButton(self.centralwidget)
        self.ascending_btn_main.setGeometry(QtCore.QRect(780, 40, 31, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.ascending_btn_main.setFont(font)
        self.ascending_btn_main.setObjectName("ascending_btn_main")
        self.input_marks_TWidget_main = QtWidgets.QTableWidget(self.centralwidget)
        self.input_marks_TWidget_main.setGeometry(QtCore.QRect(612, 160, 311, 111))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.input_marks_TWidget_main.setFont(font)
        self.input_marks_TWidget_main.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.input_marks_TWidget_main.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.input_marks_TWidget_main.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.input_marks_TWidget_main.setObjectName("input_marks_TWidget_main")
        self.input_marks_TWidget_main.setColumnCount(0)
        self.input_marks_TWidget_main.setRowCount(0)
        self.input_marks_TWidget_main.horizontalHeader().setVisible(False)
        self.input_marks_TWidget_main.horizontalHeader().setDefaultSectionSize(50)
        self.input_marks_TWidget_main.horizontalHeader().setMinimumSectionSize(10)
        self.input_marks_TWidget_main.verticalHeader().setVisible(False)
        self.input_marks_TWidget_main.verticalHeader().setHighlightSections(True)
        self.result_btn_main = QtWidgets.QLabel(self.centralwidget)
        self.result_btn_main.setGeometry(QtCore.QRect(612, 280, 241, 31))
        font = QtGui.QFont()
        font.setPointSize(16)
        self.result_btn_main.setFont(font)
        self.result_btn_main.setText("")
        self.result_btn_main.setObjectName("result_btn_main")
        self.subj_append_btn = QtWidgets.QPushButton(self.centralwidget)
        self.subj_append_btn.setGeometry(QtCore.QRect(420, 10, 171, 31))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.subj_append_btn.setFont(font)
        self.subj_append_btn.setObjectName("subj_append_btn")
        self.appendMarkMain = QtWidgets.QPushButton(self.centralwidget)
        self.appendMarkMain.setGeometry(QtCore.QRect(930, 160, 71, 23))
        self.appendMarkMain.setObjectName("appendMarkMain")
        self.deleteMarkMain = QtWidgets.QPushButton(self.centralwidget)
        self.deleteMarkMain.setGeometry(QtCore.QRect(930, 190, 71, 23))
        self.deleteMarkMain.setObjectName("deleteMarkMain")
        self.delete_btn_main = QtWidgets.QPushButton(self.centralwidget)
        self.delete_btn_main.setGeometry(QtCore.QRect(10, 490, 181, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.delete_btn_main.setFont(font)
        self.delete_btn_main.setObjectName("delete_btn_main")
        self.edit_btn_main = QtWidgets.QPushButton(self.centralwidget)
        self.edit_btn_main.setGeometry(QtCore.QRect(400, 490, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.edit_btn_main.setFont(font)
        self.edit_btn_main.setObjectName("edit_btn_main")
        self.line = QtWidgets.QFrame(self.centralwidget)
        self.line.setGeometry(QtCore.QRect(583, 0, 41, 551))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.append_btn_main = QtWidgets.QPushButton(self.centralwidget)
        self.append_btn_main.setGeometry(QtCore.QRect(200, 490, 191, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.append_btn_main.setFont(font)
        self.append_btn_main.setObjectName("append_btn_main")
        self.type_of_cff_main = QtWidgets.QComboBox(self.centralwidget)
        self.type_of_cff_main.setGeometry(QtCore.QRect(690, 130, 161, 22))
        self.type_of_cff_main.setObjectName("type_of_cff_main")
        self.type_of_cff_main.addItem("")
        self.type_of_cff_main.addItem("")
        self.type_of_cff_main.addItem("")
        self.type_of_cff_main.addItem("")
        self.type_of_cff_main.addItem("")
        self.label_text_main = QtWidgets.QLabel(self.centralwidget)
        self.label_text_main.setGeometry(QtCore.QRect(616, 10, 181, 21))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.label_text_main.setFont(font)
        self.label_text_main.setObjectName("label_text_main")
        self.error_label_2 = QtWidgets.QLabel(self.centralwidget)
        self.error_label_2.setGeometry(QtCore.QRect(860, 130, 141, 21))
        self.error_label_2.setText("")
        self.error_label_2.setObjectName("error_label_2")
        self.tableWidget_main = QtWidgets.QTableWidget(self.centralwidget)
        self.tableWidget_main.setGeometry(QtCore.QRect(10, 50, 581, 431))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tableWidget_main.setFont(font)
        self.tableWidget_main.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget_main.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget_main.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        self.tableWidget_main.setObjectName("tableWidget_main")
        self.tableWidget_main.setColumnCount(0)
        self.tableWidget_main.setRowCount(0)
        self.tableWidget_main.horizontalHeader().setVisible(False)
        self.tableWidget_main.horizontalHeader().setDefaultSectionSize(70)
        self.tableWidget_main.horizontalHeader().setMinimumSectionSize(50)
        self.tableWidget_main.verticalHeader().setVisible(False)
        self.tableWidget_main.verticalHeader().setDefaultSectionSize(34)
        self.drop_btn_main = QtWidgets.QPushButton(self.centralwidget)
        self.drop_btn_main.setGeometry(QtCore.QRect(610, 490, 131, 41))
        font = QtGui.QFont()
        font.setPointSize(11)
        self.drop_btn_main.setFont(font)
        self.drop_btn_main.setFlat(False)
        self.drop_btn_main.setObjectName("drop_btn_main")
        self.clearMarksMain = QtWidgets.QPushButton(self.centralwidget)
        self.clearMarksMain.setGeometry(QtCore.QRect(930, 220, 71, 23))
        self.clearMarksMain.setObjectName("clearMarksMain")
        self.error_label = QtWidgets.QLabel(self.centralwidget)
        self.error_label.setGeometry(QtCore.QRect(610, 80, 161, 16))
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.mark_input_main = QtWidgets.QSpinBox(self.centralwidget)
        self.mark_input_main.setGeometry(QtCore.QRect(610, 130, 71, 22))
        self.mark_input_main.setMinimum(2)
        self.mark_input_main.setMaximum(5)
        self.mark_input_main.setObjectName("mark_input_main")
        self.error_label_3 = QtWidgets.QLabel(self.centralwidget)
        self.error_label_3.setGeometry(QtCore.QRect(20, 540, 321, 16))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.error_label_3.setFont(font)
        self.error_label_3.setText("")
        self.error_label_3.setObjectName("error_label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1012, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Предметы и оценки"))
        self.sort_CBox_main.setItemText(0, _translate("MainWindow", "Порядку"))
        self.sort_CBox_main.setItemText(1, _translate("MainWindow", "Значению"))
        self.sort_CBox_main.setItemText(2, _translate("MainWindow", "Весу оценки"))
        self.checkBox.setText(_translate("MainWindow", "Работа на уроке"))
        self.checkBox_2.setText(_translate("MainWindow", "Домашняя работа"))
        self.checkBox_3.setText(_translate("MainWindow", "Самостоятельная работа"))
        self.checkBox_4.setText(_translate("MainWindow", "Контрольная работа"))
        self.checkBox_5.setText(_translate("MainWindow", "Диктант"))
        self.subj_name_label.setText(_translate("MainWindow", "Name"))
        self.ascending_btn_main.setText(_translate("MainWindow", "↓"))
        self.subj_append_btn.setText(_translate("MainWindow", "Добавить предмет"))
        self.appendMarkMain.setText(_translate("MainWindow", "Добавть"))
        self.deleteMarkMain.setText(_translate("MainWindow", "Удалить"))
        self.delete_btn_main.setText(_translate("MainWindow", "Удалить "))
        self.edit_btn_main.setText(_translate("MainWindow", "Изменить"))
        self.append_btn_main.setText(_translate("MainWindow", "Добавить"))
        self.type_of_cff_main.setItemText(0, _translate("MainWindow", "Работа на уроке"))
        self.type_of_cff_main.setItemText(1, _translate("MainWindow", "Домашняя работа"))
        self.type_of_cff_main.setItemText(2, _translate("MainWindow", "Самостоятельная работа"))
        self.type_of_cff_main.setItemText(3, _translate("MainWindow", "Контрольная работа"))
        self.type_of_cff_main.setItemText(4, _translate("MainWindow", "Диктант"))
        self.label_text_main.setText(_translate("MainWindow", "Сортировать по:"))
        self.drop_btn_main.setText(_translate("MainWindow", "Удалить предмет"))
        self.clearMarksMain.setText(_translate("MainWindow", "Отчистить"))


# интерфейс дополнительной формы
class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(791, 353)
        self.line = QtWidgets.QFrame(Form)
        self.line.setGeometry(QtCore.QRect(290, 0, 16, 361))
        self.line.setFrameShape(QtWidgets.QFrame.VLine)
        self.line.setFrameShadow(QtWidgets.QFrame.Sunken)
        self.line.setObjectName("line")
        self.append_subj_btn = QtWidgets.QPushButton(Form)
        self.append_subj_btn.setGeometry(QtCore.QRect(310, 70, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.append_subj_btn.setFont(font)
        self.append_subj_btn.setObjectName("append_subj_btn")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(310, 10, 111, 16))
        font = QtGui.QFont()
        font.setPointSize(9)
        self.label_3.setFont(font)
        self.label_3.setObjectName("label_3")
        self.append_mark_btn = QtWidgets.QPushButton(Form)
        self.append_mark_btn.setGeometry(QtCore.QRect(10, 90, 111, 23))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.append_mark_btn.setFont(font)
        self.append_mark_btn.setObjectName("append_mark_btn")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(10, 10, 101, 16))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.name_input = QtWidgets.QLineEdit(Form)
        self.name_input.setGeometry(QtCore.QRect(310, 30, 121, 31))
        font = QtGui.QFont()
        font.setPointSize(12)
        self.name_input.setFont(font)
        self.name_input.setObjectName("name_input")
        self.import_btn = QtWidgets.QPushButton(Form)
        self.import_btn.setGeometry(QtCore.QRect(10, 320, 75, 23))
        self.import_btn.setObjectName("import_btn")
        self.delete_mark_btn = QtWidgets.QPushButton(Form)
        self.delete_mark_btn.setGeometry(QtCore.QRect(10, 120, 111, 23))
        self.delete_mark_btn.setObjectName("delete_mark_btn")
        self.error_label = QtWidgets.QLabel(Form)
        self.error_label.setGeometry(QtCore.QRect(10, 60, 271, 21))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.error_label.setFont(font)
        self.error_label.setText("")
        self.error_label.setObjectName("error_label")
        self.error_label_2 = QtWidgets.QLabel(Form)
        self.error_label_2.setGeometry(QtCore.QRect(310, 100, 121, 21))
        self.error_label_2.setText("")
        self.error_label_2.setObjectName("error_label_2")
        self.type_of_cff = QtWidgets.QComboBox(Form)
        self.type_of_cff.setGeometry(QtCore.QRect(140, 30, 141, 22))
        self.type_of_cff.setObjectName("type_of_cff")
        self.type_of_cff.addItem("")
        self.type_of_cff.addItem("")
        self.type_of_cff.addItem("")
        self.type_of_cff.addItem("")
        self.type_of_cff.addItem("")
        self.tableWidget = QtWidgets.QTableWidget(Form)
        self.tableWidget.setGeometry(QtCore.QRect(445, 10, 331, 331))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.tableWidget.setFont(font)
        self.tableWidget.setVerticalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.tableWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAlwaysOff)
        self.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(0)
        self.tableWidget.setRowCount(0)
        self.tableWidget.horizontalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setVisible(False)
        self.mark_input = QtWidgets.QSpinBox(Form)
        self.mark_input.setGeometry(QtCore.QRect(10, 30, 111, 31))
        font = QtGui.QFont()
        font.setPointSize(15)
        self.mark_input.setFont(font)
        self.mark_input.setMinimum(2)
        self.mark_input.setMaximum(5)
        self.mark_input.setProperty("value", 5)
        self.mark_input.setObjectName("mark_input")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Добавление предмета"))
        self.append_subj_btn.setText(_translate("Form", "Добавить предмет"))
        self.label_3.setText(_translate("Form", "Название предмета:"))
        self.append_mark_btn.setText(_translate("Form", "Добавить оценку"))
        self.label.setText(_translate("Form", "Оценка:"))
        self.import_btn.setText(_translate("Form", "csv import"))
        self.delete_mark_btn.setText(_translate("Form", "Удалить"))
        self.type_of_cff.setItemText(0, _translate("Form", "Работа на уроке"))
        self.type_of_cff.setItemText(1, _translate("Form", "Домашняя работа"))
        self.type_of_cff.setItemText(2, _translate("Form", "Самостоятельная работа"))
        self.type_of_cff.setItemText(3, _translate("Form", "Контрольная работа"))
        self.type_of_cff.setItemText(4, _translate("Form", "Диктант"))


# словарь для символьного обозначения коэффицентов оценок
cff_symbols = {
    '1': '₁',
    '2': '₂',
    '3': '₃'
}


# Дополнительная форма
class AnotherWindow(QWidget, Ui_Form):
    def __init__(self):
        self.con = sqlite3.connect("subjects.sqlite")
        super().__init__()
        self.setupUi(self)
        # инициализация списка оценок
        self.mark_list = []
        self.append_mark_btn.clicked.connect(self.mark_append)
        self.delete_mark_btn.clicked.connect(self.mark_delete)
        self.append_subj_btn.clicked.connect(self.subj_append)
        self.import_btn.clicked.connect(self.csv_import)

        self.tableWidget.setColumnCount(5)
        self.tableWidget.setRowCount(1)
        self.tableWidget.resizeColumnsToContents()
        self.tableWidget.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)

    # функция занесения оценки в список
    def mark_append(self):
        cur = self.con.cursor()
        self.tableWidget.setRowCount(len(self.mark_list) // 5 + 1)

        request = f"""SELECT ID FROM coefficients
            WHERE description = '{self.type_of_cff.currentText()}'"""
        cff = cur.execute(request).fetchone()
        # добавление оценки
        self.mark_list.append([int(self.mark_input.text()), int(cff[0])])

        for index, i in enumerate(self.mark_list):
            # получение коэффициента из его ID
            request = f"""SELECT coeff FROM coefficients
                    WHERE ID = '{i[1]}'"""
            cff = cur.execute(request).fetchone()[0]
            # занесение в таблицу
            mark = QTableWidgetItem(f'{i[0]}{cff_symbols[str(cff)]}')
            self.tableWidget.setItem(index // 5, index % 5, mark)
        self.error_label.setText('Оценка добавлена')

    # функция удаления оценки из списка
    def mark_delete(self):
        cur = self.con.cursor()
        rows = list(set([i.row() for i in self.tableWidget.selectedItems()]))
        cols = list(set([i.column() for i in self.tableWidget.selectedItems()]))
        # поверка "Выбранна ли оценка?"
        try:
            ids = self.mark_list[(rows[0]) * 5 + cols[0]]
            request = f"""SELECT coeff FROM coefficients
                        WHERE ID = '{ids[1]}'"""
            cff = cur.execute(request).fetchone()[0]
            valid = QMessageBox.question(
                self, '', f"Действительно удалить оценку: {ids[0]}{cff_symbols[str(cff)]}",
                QMessageBox.Yes, QMessageBox.No)
            # если ответ диалога 'да' то удалить оценку
            if valid == QMessageBox.Yes:
                self.mark_list.pop((rows[0]) * 5 + cols[0])

            self.tableWidget.clear()
            # обновление таблицы после удаления
            for index, i in enumerate(self.mark_list):
                request = f"""SELECT coeff FROM coefficients
                        WHERE ID = '{i[1]}'"""
                cff = cur.execute(request).fetchone()[0]
                mark = QTableWidgetItem(f'{i[0]}{cff_symbols[str(cff)]}')
                self.tableWidget.setItem(index // 5, index % 5, mark)
            self.error_label.setText('Оценка удалена')
        except IndexError:
            self.error_label.setText('Не выбрана оценка')

    def subj_append(self):
        name_db = self.name_input.text()
        # если название введено
        if name_db:
            cur = self.con.cursor()
            request = f"""SELECT name FROM subjects"""
            # получаем все названия предметов
            list_of_names = list(map(lambda x: x[0], cur.execute(request).fetchall()))
            flag = True
            # проверка на занятость имени
            for i in list_of_names:
                if i == name_db:
                    flag = False
                    self.error_label_2.setText('Имя занято')
                    break
            # добавляем если не занято
            if flag:
                request = f"""INSERT INTO subjects(name) VALUES('{name_db}')"""
                cur.execute(request)
                self.error_label_2.setText('Предмет создан')
                self.con.commit()
                request = f"""SELECT ID FROM subjects
                    WHERE name = '{name_db}'"""
                # получение ID предмета для занесения оценок
                id_subj = cur.execute(request).fetchone()[0]
                # занесение предметов
                for i in self.mark_list:
                    request = f"""INSERT INTO marks(mark, coeff_ID, subject_ID) VALUES({i[0]}, {i[1]}, {id_subj})"""
                    cur.execute(request)
                    self.con.commit()
                self.mark_list = []
                self.error_label.setText('')
                self.tableWidget.clear()
                self.name_input.setText('')
            # обновляем список предметов (основная форма)
            w.update_ComboBox()
        else:
            self.error_label_2.setText('Пустое название')

    def csv_import(self):
        # проверка на правильность содержания csv файла
        try:
            cur = self.con.cursor()
            fname = QFileDialog.getOpenFileName(
                self, 'Выбрать картинку', '',
                'Файл (*.csv)')[0]
            with open(fname, encoding="utf8") as csvfile:
                reader = csv.reader(csvfile, delimiter=';', quotechar='"')
                data_read = [row for row in reader]
                print(data_read)
                for index, row in enumerate(data_read):
                    request = f"""SELECT ID FROM coefficients
                                    WHERE description = '{row[1].capitalize()}'"""
                    cff = cur.execute(request).fetchone()[0]
                    self.mark_list.append([int(row[0]), cff])
                # добавляем все елементы файла
                for index, i in enumerate(self.mark_list):
                    request = f"""SELECT coeff FROM coefficients
                            WHERE ID = '{i[1]}'"""
                    cff = cur.execute(request).fetchone()[0]
                    mark = QTableWidgetItem(f'{i[0]}{cff_symbols[str(cff)]}')
                    self.tableWidget.setItem(index // 5, index % 5, mark)
                self.error_label.setText('Оценки из файла добавлены')
        except Exception:
            self.error_label.setText('Неверный формат файла или тип работ')


# Основная форма
class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        self.predict_marks_list = []
        self.con = sqlite3.connect("subjects.sqlite")
        super().__init__()
        self.setupUi(self)
        self.subj_append_btn.clicked.connect(self.show_new_window)
        self.update_ComboBox()
        self.sort_request()
        self.subject_choose_CBox.currentIndexChanged.connect(self.sort_request)
        self.sort_CBox_main.currentIndexChanged.connect(self.sort_request)

        self.tableWidget_main.resizeColumnsToContents()
        self.tableWidget_main.setEditTriggers(QtWidgets.QAbstractItemView.NoEditTriggers)
        self.tableWidget_main.setColumnCount(8)
        self.tableWidget_main.setRowCount(1)
        self.input_marks_TWidget_main.setRowCount(1)

        self.drop_btn_main.clicked.connect(self.drop_subject)
        self.delete_btn_main.clicked.connect(self.delete_mark)
        self.append_btn_main.clicked.connect(self.append_mark)
        self.edit_btn_main.clicked.connect(self.edit_mark)
        self.ascending_btn_main.clicked.connect(self.btn_change_text)
        self.ascending_btn_main.clicked.connect(self.sort_request)
        self.appendMarkMain.clicked.connect(self.mark_append_miniWidget)
        self.deleteMarkMain.clicked.connect(self.mark_delete_miniWidget)
        self.clearMarksMain.clicked.connect(self.mark_clear_miniWidget)

        self.checkBox.stateChanged.connect(self.sort_request)
        self.checkBox_2.stateChanged.connect(self.sort_request)
        self.checkBox_3.stateChanged.connect(self.sort_request)
        self.checkBox_4.stateChanged.connect(self.sort_request)
        self.checkBox_5.stateChanged.connect(self.sort_request)

    # функция вывод среднего балла
    def averageScore(self, input1=[], input2=[]):
        con = sqlite3.connect("subjects.sqlite")
        cur = con.cursor()
        output1 = []
        output2 = []
        # если указан второй список с 'предпологаемыми' оценками
        if input1 and input2:
            for index, i in enumerate(input2):
                request = f"SELECT coeff FROM coefficients WHERE ID = '{i[1]}'"
                cff = cur.execute(request).fetchone()[0]
                output2.append([input2[index][0], cff])

            for index, i in enumerate(input1):
                request = f"SELECT coeff FROM coefficients WHERE ID = '{i[1]}'"
                cff = cur.execute(request).fetchone()[0]
                output1.append([input1[index][0], cff])
                output2.append([input1[index][0], cff])
            # вычисление текущего и нового среднего балла
            old_avg = round(sum(list(map(lambda x: x[0] * x[1], output1))) / sum(list(map(lambda x: x[1], output1))), 2)
            new_avg = round(sum(list(map(lambda x: x[0] * x[1], output2))) / sum(list(map(lambda x: x[1], output2))), 2)
            # возвращяем строку сразу для вывода, т.к. нигде не будет больше использоваться кроме вывода в текстовом виде
            return f'{old_avg} -> {new_avg}'
        # если список на вход без 'предпологаемых' оценок
        elif input1:
            for index, i in enumerate(input1):
                request = f"SELECT coeff FROM coefficients WHERE ID = '{i[1]}'"
                cff = cur.execute(request).fetchone()[0]
                output1.append([input1[index][0], cff])
                # возвращает строку для вывода
            return f'{round(sum(list(map(lambda x: x[0] * x[1], output1))) / sum(list(map(lambda x: x[1], output1))), 2)}'

    # обновление выпадающего меню при жобавлении оценок
    def update_ComboBox(self):
        self.subject_choose_CBox.clear()
        cur = self.con.cursor()
        request = f"""SELECT name FROM subjects"""
        subjects = list(map(lambda x: x[0], cur.execute(request).fetchall()))
        self.subject_choose_CBox.addItem('Не выбрано')
        for i in subjects:
            # занесение в выпадающее меню
            self.subject_choose_CBox.addItem(str(i))

    # Функция, обновляющая вывод в таблицу, в зависимости от выбранных фильров (request на входе и parametrs для сортировки)
    def output_subject(self, request='', parameters=(0, False)):
        cur = self.con.cursor()
        if self.subject_choose_CBox.currentText() != 'Не выбрано':
            self.tableWidget_main.clear()
            self.mark_list = cur.execute(request).fetchall()
            request = f"""SELECT mark, coeff_ID, ID FROM marks
                        WHERE subject_ID = (
                            SELECT ID FROM subjects
                                WHERE name = '{self.subject_choose_CBox.currentText()}')"""
            # Техническая переменная для отображения среднего балла независимо от фильтров (self.all_mark_list)
            self.all_mark_list = cur.execute(request).fetchall()
            if parameters[0] == 1:
                self.mark_list = sorted(self.mark_list, key=lambda x: x[0], reverse=not (parameters[1]))
            elif parameters[0] == 2:
                self.mark_list = sorted(self.mark_list, key=lambda x: x[1], reverse=not (parameters[1]))

            self.tableWidget_main.setRowCount(len(self.mark_list) // 8 + 1)

            # обновление таблицы
            for index, i in enumerate(self.mark_list):
                request = f"""SELECT coeff FROM coefficients
                        WHERE ID = '{i[1]}'"""
                cff = cur.execute(request).fetchone()[0]
                mark = QTableWidgetItem(f'{i[0]}{cff_symbols[str(cff)]}')
                self.tableWidget_main.setItem(index // 8, index % 8, mark)
            self.subj_name_label.setText(self.subject_choose_CBox.currentText() + ':')
            # вывод срднего балла
            self.result_btn_main.setText(self.averageScore(self.all_mark_list, self.predict_marks_list))

        else:
            # отчиска если предмет не выбран
            self.mark_list = []
            self.all_mark_list = []
            self.subj_name_label.setText('<- Выберете предмет')
            self.result_btn_main.setText('')
            self.tableWidget_main.clear()
            self.tableWidget_main.setRowCount(1)

    # удаление выбранного предмета
    def drop_subject(self):
        if self.subject_choose_CBox.currentIndex():
            valid = QMessageBox.question(
                self, '', f"Действительно удалить предмет '{self.subject_choose_CBox.currentText()}'",
                QMessageBox.Yes, QMessageBox.No)

            if valid == QMessageBox.Yes:
                cur = self.con.cursor()
                cur.execute(f"""DELETE FROM marks WHERE subject_ID = (
                                    SELECT ID FROM subjects 
                                        WHERE name = '{self.subject_choose_CBox.currentText()}'       
                                )""")
                cur.execute(f"DELETE FROM subjects WHERE name = '{self.subject_choose_CBox.currentText()}'")
                self.con.commit()
            # после удаления предмета обновляется выпадающее меню предметов и ставится исходное значение
            self.update_ComboBox()
            self.output_subject()
        else:
            self.error_label_3.setText('Не выбран предмет')

    # удаление оценки
    def delete_mark(self):
        # "если оценка выбрана:"
        try:
            self.error_label_3.setText('')
            cur = self.con.cursor()
            rows = list(set([i.row() for i in self.tableWidget_main.selectedItems()]))
            cols = list(set([i.column() for i in self.tableWidget_main.selectedItems()]))
            # получение значения выбранного елемента
            ids = self.mark_list[(rows[0]) * 8 + cols[0]]
            request = f"""SELECT coeff FROM coefficients
                            WHERE ID = '{ids[1]}'"""
            cff = cur.execute(request).fetchone()[0]

            valid = QMessageBox.question(
                self, '', "Действительно удалить оценку: " + f'{ids[0]}{cff_symbols[str(cff)]}',
                QMessageBox.Yes, QMessageBox.No)
            if valid == QMessageBox.Yes:
                cur = self.con.cursor()
                cur.execute(f"DELETE FROM marks WHERE ID = {ids[2]}")
                self.mark_list.pop((rows[0]) * 8 + cols[0])
                self.con.commit()
            # после удаления обновляем результаты через формирование запроса в функции sort_request
            self.sort_request()
        except IndexError:
            self.error_label_3.setText('Не выбрана оценка')

    # добавление оценки в предмет
    def append_mark(self):
        if self.subject_choose_CBox.currentIndex():
            self.error_label_3.setText('')
            cur = self.con.cursor()
            # выбор типа работы
            type_of_work, ok_pressed = QInputDialog.getItem(
                self, "Добаввление отметки", "Ввыберете тип работы:",
                ("Работа на уроке", "Домашняя работа", "Самостоятельная работа", "Контрольная работа", "Диктант"), 1,
                False)
            if ok_pressed:
                request = f"SELECT ID FROM coefficients WHERE description = '{type_of_work}'"
                cff_id = cur.execute(request).fetchone()[0]
                mark, ok_pressed = QInputDialog.getInt(
                    # выбор оценки
                    self, "Добаввление отметки", "Оценка:",
                    5, 2, 5, 1)

                if ok_pressed:
                    request = f"SELECT ID FROM subjects WHERE name = '{self.subject_choose_CBox.currentText()}'"
                    subj_id = cur.execute(request).fetchone()[0]
                    request = f"""INSERT INTO marks (mark, coeff_ID, subject_ID) 
                                    VALUES({mark}, {cff_id}, {subj_id})"""
                    cur.execute(request)
                    self.con.commit()
            # обновление результатов через формирование запроса
            self.sort_request()
        else:
            self.error_label_3.setText('Не выбран предмет')

    # изменение оценки
    def edit_mark(self):
        if self.subject_choose_CBox.currentIndex():
            self.error_label_3.setText('')
            cur = self.con.cursor()
            rows = list(set([i.row() for i in self.tableWidget_main.selectedItems()]))
            cols = list(set([i.column() for i in self.tableWidget_main.selectedItems()]))
            ids = [self.tableWidget_main.item(i, 0).text() for i in rows]
            if ids:
                choosen_mark = self.mark_list[(rows[0]) * 8 + cols[0]]

                type_of_work, ok_pressed = QInputDialog.getItem(
                    # выбор типа работы (для редактирования)
                    self, "Редактирование отметки", "Новый тип работы:",
                    ("Работа на уроке", "Домашняя работа", "Самостоятельная работа", "Контрольная работа", "Диктант"),
                    1, False)
                if ok_pressed:
                    request = f"SELECT ID FROM coefficients WHERE description = '{type_of_work}'"
                    cff_id = cur.execute(request).fetchone()[0]
                    mark, ok_pressed = QInputDialog.getInt(
                        # выбор оценки для редактирования
                        self, "Редактирование отметки", "Новая оценка:",
                        5, 2, 5, 1)

                    if ok_pressed:
                        # обновление оценок
                        request = f"""UPDATE marks
                                        SET mark = {mark},
                                        coeff_ID = {cff_id}
                                        WHERE ID = {choosen_mark[2]}"""
                        cur.execute(request)
                        self.con.commit()
                        # обновление таблицы через формирование запроса
                        self.sort_request()
            else:
                self.error_label_3.setText('Не выбрана оценка')

    # формирование запроса в зависимости от выбранных критериев сортировки
    def sort_request(self):
        if self.sort_CBox_main.currentIndex():
            self.ascending_btn_main.show()
        else:
            self.ascending_btn_main.hide()
        # технический список для записи выбранных ID типов работы
        cff_id_list = []
        # все чекбоксы не объеденены в butttonGroup и проверяются последовательно
        if self.checkBox.isChecked():
            cff_id_list.append('1')
        if self.checkBox_2.isChecked():
            cff_id_list.append('2')
        if self.checkBox_3.isChecked():
            cff_id_list.append('3')
        if self.checkBox_4.isChecked():
            cff_id_list.append('4')
        if self.checkBox_5.isChecked():
            cff_id_list.append('5')
        cur = self.con.cursor()
        # строка для вставки в формирование запроса
        cff = ', '.join(cff_id_list)
        # "если выбран тип работы, то:"
        if len(cff_id_list):
            self.error_label.setText('')
            request = f"""SELECT mark, coeff_ID, ID FROM marks
                        WHERE subject_ID = (
                            SELECT ID FROM subjects
                                WHERE name = '{self.subject_choose_CBox.currentText()}'
                    ) and coeff_ID in ({cff})"""
            # инициализация и занесение в переменную param тип сортировки и критерий убавние/возрастание
            if self.ascending_btn_main.text() == '↓':
                param = (self.sort_CBox_main.currentIndex(), False)
            else:
                param = (self.sort_CBox_main.currentIndex(), True)
            # обновляем табличные данные с сформированным запросом и параметрами (param)
            self.output_subject(request, param)
        elif len(cff_id_list) == 0:
            self.error_label.setText('Не выбран тип работы')
            self.tableWidget_main.clear()

    # смена текста кнопки со стрелочкой
    def btn_change_text(self):
        if self.ascending_btn_main.text() == '↓':
            self.ascending_btn_main.setText('↑')
        else:
            self.ascending_btn_main.setText('↓')

    # добавление оценки в меньшнн окно "предпологаемых оценок" по вышеупомянотому принципу работы
    def mark_append_miniWidget(self):
        cur = self.con.cursor()
        self.input_marks_TWidget_main.setRowCount(len(self.predict_marks_list) // 5 + 1)
        self.input_marks_TWidget_main.setColumnCount(5)
        if self.mark_input_main.text():
            if self.mark_input_main.text() not in ('2', '3', '4', '5'):
                self.error_label_2.setText('Введена неверная оценка')
            else:
                request = f"""SELECT ID FROM coefficients
                    WHERE description = '{self.type_of_cff_main.currentText()}'"""
                cff = cur.execute(request).fetchone()
                self.predict_marks_list.append([int(self.mark_input_main.text()), int(cff[0])])
        else:
            self.error_label_2.setText('Не введена оценка')

        for index, i in enumerate(self.predict_marks_list):
            request = f"""SELECT coeff FROM coefficients
                    WHERE ID = '{i[1]}'"""
            cff = cur.execute(request).fetchone()[0]
            mark = QTableWidgetItem(f'{i[0]}{cff_symbols[str(cff)]}')
            self.input_marks_TWidget_main.setItem(index // 5, index % 5, mark)
        self.error_label_2.setText('Оценка добавлена')
        self.result_btn_main.setText(self.averageScore(input1=self.all_mark_list, input2=self.predict_marks_list))

    # удаление оценки в меньшнн окно "предпологаемых оценок" по вышеупомянотому принципу работы
    def mark_delete_miniWidget(self):
        cur = self.con.cursor()
        rows = list(set([i.row() for i in self.input_marks_TWidget_main.selectedItems()]))
        cols = list(set([i.column() for i in self.input_marks_TWidget_main.selectedItems()]))
        # провернка на наличие выбранного поля (try, exept)
        try:
            ids = self.predict_marks_list[(rows[0]) * 5 + cols[0]]
            request = f"""SELECT coeff FROM coefficients
                            WHERE ID = '{ids[1]}'"""
            cff = cur.execute(request).fetchone()[0]

            self.predict_marks_list.pop((rows[0]) * 5 + cols[0])

            # отчищаем виджет и заного заполняем оценками после удаления
            self.input_marks_TWidget_main.clear()
            for index, i in enumerate(self.predict_marks_list):
                request = f"""SELECT coeff FROM coefficients
                        WHERE ID = '{i[1]}'"""
                cff = cur.execute(request).fetchone()[0]
                mark = QTableWidgetItem(f'{i[0]}{cff_symbols[str(cff)]}')
                self.input_marks_TWidget_main.setItem(index // 5, index % 5, mark)
            self.error_label_2.setText('Оценка удалена')
        except IndexError:
            self.error_label_2.setText('Не выбрана оценка:')
        self.result_btn_main.setText(self.averageScore(self.all_mark_list, self.predict_marks_list))

    # отчищение всего списка
    def mark_clear_miniWidget(self):
        self.input_marks_TWidget_main.clear()
        self.input_marks_TWidget_main.setRowCount(1)
        self.predict_marks_list = []
        self.error_label_2.setText('')
        self.result_btn_main.setText(self.averageScore(self.all_mark_list, self.predict_marks_list))

    # Функция отурытия второй формы
    def show_new_window(self, checked):
        self.w_2 = AnotherWindow()
        self.w_2.show()


app = QApplication(sys.argv)
w = MainWindow()
w.show()
app.exec()