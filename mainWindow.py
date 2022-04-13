# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'new.ui'
#
# Created by: PyQt5 UI code generator 5.9.2
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog, QMessageBox

from wordForms import *
from processedWordClass import *


def find_checked_radiobutton(radio_buttons):
    for item in radio_buttons:
        if item.isChecked():
            checked_radiobutton_text = item.text()
            return checked_radiobutton_text


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(618, 618)
        MainWindow.setMinimumSize(QtCore.QSize(618, 618))
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.centralwidget)
        self.verticalLayout.setObjectName("verticalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setObjectName("tabWidget")
        self.processingTab = QtWidgets.QWidget()
        self.processingTab.setObjectName("processingTab")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.processingTab)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.readFileButton = QtWidgets.QPushButton(self.processingTab)
        self.readFileButton.setObjectName("readFileButton")
        self.verticalLayout_2.addWidget(self.readFileButton)
        self.inputTextEdit = QtWidgets.QTextEdit(self.processingTab)
        self.inputTextEdit.setObjectName("inputTextEdit")
        self.verticalLayout_2.addWidget(self.inputTextEdit)
        self.textProcessButton = QtWidgets.QPushButton(self.processingTab)
        self.textProcessButton.setObjectName("textProcessButton")
        self.verticalLayout_2.addWidget(self.textProcessButton)
        self.outputTable = QtWidgets.QTableWidget(self.processingTab)
        self.outputTable.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.outputTable.setObjectName("outputTable")
        self.outputTable.setColumnCount(4)
        self.outputTable.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.outputTable.setHorizontalHeaderItem(3, item)
        self.outputTable.horizontalHeader().setMinimumSectionSize(144)
        self.outputTable.horizontalHeader().setStretchLastSection(True)
        self.outputTable.verticalHeader().setStretchLastSection(False)
        self.verticalLayout_2.addWidget(self.outputTable)
        self.clearTableButton = QtWidgets.QPushButton(self.processingTab)
        self.clearTableButton.setObjectName("clearTableButton")
        self.verticalLayout_2.addWidget(self.clearTableButton)
        self.tabWidget.addTab(self.processingTab, "")
        self.generationTab = QtWidgets.QWidget()
        self.generationTab.setObjectName("generationTab")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.generationTab)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.generationInputLine = QtWidgets.QLineEdit(self.generationTab)
        self.generationInputLine.setObjectName("generationInputLine")
        self.verticalLayout_3.addWidget(self.generationInputLine)
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.prefixGroupBox = QtWidgets.QGroupBox(self.generationTab)
        self.prefixGroupBox.setEnabled(True)
        self.prefixGroupBox.setCheckable(False)
        self.prefixGroupBox.setObjectName("prefixGroupBox")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.prefixGroupBox)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.noPrefRadio = QtWidgets.QRadioButton(self.prefixGroupBox)
        self.noPrefRadio.setChecked(True)
        self.noPrefRadio.setObjectName("noPrefRadio")
        self.verticalLayout_5.addWidget(self.noPrefRadio)
        self.genPrefRadio = QtWidgets.QRadioButton(self.prefixGroupBox)
        self.genPrefRadio.setObjectName("genPrefRadio")
        self.verticalLayout_5.addWidget(self.genPrefRadio)
        self.negPrefRadio = QtWidgets.QRadioButton(self.prefixGroupBox)
        self.negPrefRadio.setObjectName("negPrefRadio")
        self.verticalLayout_5.addWidget(self.negPrefRadio)
        self.horizontalLayout.addWidget(self.prefixGroupBox)
        self.suffixGroupBox = QtWidgets.QGroupBox(self.generationTab)
        self.suffixGroupBox.setObjectName("suffixGroupBox")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.suffixGroupBox)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.noSuffixRadio = QtWidgets.QRadioButton(self.suffixGroupBox)
        self.noSuffixRadio.setChecked(True)
        self.noSuffixRadio.setObjectName("noSuffixRadio")
        self.verticalLayout_4.addWidget(self.noSuffixRadio)
        self.nounRadio = QtWidgets.QRadioButton(self.suffixGroupBox)
        self.nounRadio.setObjectName("nounRadio")
        self.verticalLayout_4.addWidget(self.nounRadio)
        self.adjectiveRadio = QtWidgets.QRadioButton(self.suffixGroupBox)
        self.adjectiveRadio.setObjectName("adjectiveRadio")
        self.verticalLayout_4.addWidget(self.adjectiveRadio)
        self.verbRadio = QtWidgets.QRadioButton(self.suffixGroupBox)
        self.verbRadio.setObjectName("verbRadio")
        self.verticalLayout_4.addWidget(self.verbRadio)
        self.adverbRadio = QtWidgets.QRadioButton(self.suffixGroupBox)
        self.adverbRadio.setObjectName("adverbRadio")
        self.verticalLayout_4.addWidget(self.adverbRadio)
        self.horizontalLayout.addWidget(self.suffixGroupBox)
        self.verticalLayout_3.addLayout(self.horizontalLayout)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.generateButton = QtWidgets.QPushButton(self.generationTab)
        self.generateButton.setObjectName("generateButton")
        self.verticalLayout_7.addWidget(self.generateButton)
        self.clearOutputButton = QtWidgets.QPushButton(self.generationTab)
        self.clearOutputButton.setObjectName("clearOutputButton")
        self.verticalLayout_7.addWidget(self.clearOutputButton)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.generationOutputTextBrowser = QtWidgets.QTextBrowser(self.generationTab)
        self.generationOutputTextBrowser.setObjectName("generationOutputTextBrowser")
        self.horizontalLayout_2.addWidget(self.generationOutputTextBrowser)
        self.verticalLayout_3.addLayout(self.horizontalLayout_2)
        self.tabWidget.addTab(self.generationTab, "")
        self.helpTab = QtWidgets.QWidget()
        self.helpTab.setObjectName("helpTab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.helpTab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.helpTextBrowser = QtWidgets.QTextBrowser(self.helpTab)
        self.helpTextBrowser.setObjectName("helpTextBrowser")
        self.verticalLayout_6.addWidget(self.helpTextBrowser)
        self.tabWidget.addTab(self.helpTab, "")
        self.verticalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.readFileButton.clicked.connect(self.open_file)
        self.textProcessButton.clicked.connect(self.text_process_button_clicked)
        self.generateButton.clicked.connect(self.generate_button_clicked)
        self.clearTableButton.clicked.connect(self.clear_table_button_clicked)
        self.clearOutputButton.clicked.connect(self.clear_output_button_clicked)

    def open_file(self):
        file_name, _ = QFileDialog.getOpenFileName(None, 'Open file', '', 'Text files (*.txt)')
        with open(file_name) as f:
            self.inputTextEdit.setText(f.read())

    def text_process_button_clicked(self):
        # check if the input is empty
        if self.inputTextEdit.toPlainText() == '':
            QMessageBox.warning(None, 'Warning', 'Please input text first!')
            return
        text = self.inputTextEdit.toPlainText()
        text = text_preprocessing(text)
        text = add_pos_tag(text)
        text = lemmatize_text(text)
        text = list(set(text))
        text.sort()

        processed_words = []
        for word in text:
            processed_words.append(ProcessedWord(word, get_pos_tag(word)[0][1],
                                                 get_prefixes(word, general_prefixes) + get_prefixes(word,
                                                                                                     negative_prefixes),
                                                 get_suffixes(word, noun_suffixes) + get_suffixes(word,
                                                                                                  adjective_suffixes) +
                                                 get_suffixes(word, verb_suffixes) + get_suffixes(word,
                                                                                                  adverb_suffixes)))

        # fill outputTable with processed words
        self.outputTable.setRowCount(len(processed_words))
        for i, word in enumerate(processed_words):
            self.outputTable.setItem(i, 0, QtWidgets.QTableWidgetItem(word.lemma))
            self.outputTable.setItem(i, 1, QtWidgets.QTableWidgetItem(word.pos))
            self.outputTable.setItem(i, 2, QtWidgets.QTableWidgetItem(str(word.correct_prefixes)))
            self.outputTable.setItem(i, 3, QtWidgets.QTableWidgetItem(str(word.correct_suffixes)))

    def generate_button_clicked(self):
        # check if input line is empty
        if self.generationInputLine.text() == '':
            QMessageBox.warning(None, 'Warning', 'Input line is empty!')
            return

        word = self.generationInputLine.text()
        word = text_preprocessing(word)
        word = add_pos_tag(word)
        word = lemmatize_text(word)

        if word == []:
            QMessageBox.warning(None, 'Warning', 'Word is not valid!')
            return

        prefix_param = {
            'no prefix': ' ',
            'general prefix': general_prefixes,
            'negative prefix': negative_prefixes
        }

        suffix_param = {
            'no suffix': ' ',
            'noun': noun_suffixes,
            'adjective': adjective_suffixes,
            'verb': verb_suffixes,
            'adverb': adverb_suffixes
        }

        prefix_group = prefix_param[find_checked_radiobutton(self.prefixGroupBox.findChildren(QtWidgets.QRadioButton))]
        suffix_group = suffix_param[find_checked_radiobutton(self.suffixGroupBox.findChildren(QtWidgets.QRadioButton))]

        generated_words = generate_possible_words(word.pop(0), prefix_group, suffix_group)

        generated_words = [word.strip() for word in generated_words]

        for word in generated_words:
            self.generationOutputTextBrowser.append(word)

    def clear_table_button_clicked(self):
        self.outputTable.setRowCount(0)

    def clear_output_button_clicked(self):
        self.generationOutputTextBrowser.clear()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.readFileButton.setText(_translate("MainWindow", "Read from file"))
        self.textProcessButton.setText(_translate("MainWindow", "Process text"))
        item = self.outputTable.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "Lemmas"))
        item = self.outputTable.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "Pos"))
        item = self.outputTable.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "Prefixes"))
        item = self.outputTable.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "Suffixes"))
        self.clearTableButton.setText(_translate("MainWindow", "Clear table"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.processingTab),
                                  _translate("MainWindow", "Processing"))
        self.prefixGroupBox.setTitle(_translate("MainWindow", "Prefix"))
        self.noPrefRadio.setText(_translate("MainWindow", "no prefix"))
        self.genPrefRadio.setText(_translate("MainWindow", "general prefix"))
        self.negPrefRadio.setText(_translate("MainWindow", "negative prefix"))
        self.suffixGroupBox.setTitle(_translate("MainWindow", "Suffix"))
        self.noSuffixRadio.setText(_translate("MainWindow", "no suffix"))
        self.nounRadio.setText(_translate("MainWindow", "noun"))
        self.adjectiveRadio.setText(_translate("MainWindow", "adjective"))
        self.verbRadio.setText(_translate("MainWindow", "verb"))
        self.adverbRadio.setText(_translate("MainWindow", "adverb"))
        self.generateButton.setText(_translate("MainWindow", "Generate"))
        self.clearOutputButton.setText(_translate("MainWindow", "Clear output"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.generationTab),
                                  _translate("MainWindow", "Generation"))
        self.helpTextBrowser.setHtml(_translate("MainWindow",
                                                "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
                                                "<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
                                                "p, li { white-space: pre-wrap; }\n"
                                                "</style></head><body style=\" font-family:\'Fira Sans Semi-Light\'; font-size:10pt; font-weight:400; font-style:normal;\">\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">This small program is aimed to process text and/or generate some wordforms</p>\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Processing tab is capable of processing text which you can read from file or directly input in the textbox. After pressing process button program will output a table of all recognized wordforms of which we can find at the our given vocabulary  with their lemmas and possible morphemas</p>\n"
                                                "<p style=\"-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\"><br /></p>\n"
                                                "<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Generation tab is meant to generate wordforms using parameters also present in this tab. All you need is to enter a desired word in the text line set some wanted parameters and pres generate button.</p></body></html>"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.helpTab), _translate("MainWindow", "Help"))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
