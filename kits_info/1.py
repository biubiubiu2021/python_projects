from PyQt5.QtWidgets import QApplication, QWidget, QPushButton, QLabel, QInputDialog, QTextBrowser, QTextEdit, QCheckBox, QTableWidget, QTableWidgetItem, QHBoxLayout, QDialog
from PyQt5.QtGui import QColor
import sys

class TableWindow(QDialog):
    def __init__(self, data1, data2):
        super().__init__()
        self.setWindowTitle("Table Window")
        self.setFixedSize(1000,500)
        self.table1 = QTableWidget()
        self.table1.setRowCount(len(data1))
        self.table1.setColumnCount(2)
        self.table1.setHorizontalHeaderLabels(["Ingredient", "Version"])

        for row, (ingredient, version) in enumerate(data1.items()):
            item_ingredient = QTableWidgetItem(ingredient)
            item_version = QTableWidgetItem(version)
            self.table1.setItem(row, 0, item_ingredient)
            self.table1.setItem(row, 1, item_version)
        self.table1.resizeColumnsToContents()
        self.table1.resizeRowsToContents()

        self.table2 = QTableWidget()
        self.table2.setRowCount(len(data2))
        self.table2.setColumnCount(2)
        self.table2.setHorizontalHeaderLabels(["Ingredient", "Version"])

        for row, (ingredient, version) in enumerate(data2.items()):
            item_ingredient = QTableWidgetItem(ingredient)
            item_version = QTableWidgetItem(version)
            self.table2.setItem(row, 0, item_ingredient)
            self.table2.setItem(row, 1, item_version)
        self.table2.resizeColumnsToContents()
        self.table2.resizeRowsToContents()

        self.compareTables()

        layout = QHBoxLayout()
        layout.addWidget(self.table1)
        layout.addWidget(self.table2)
        self.setLayout(layout)

    def compareTables(self):
        for row in range(self.table1.rowCount()):
            ingredient1 = self.table1.item(row, 0).text()
            version1 = self.table1.item(row, 1).text()

            ingredient2 = self.table2.item(row, 0).text()
            version2 = self.table2.item(row, 1).text()

            if ingredient1 == ingredient2 and version1 != version2:
                self.table1.item(row, 1).setBackground(QColor("red"))
                self.table2.item(row, 1).setBackground(QColor("red"))

class Example(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setGeometry(2800, 500, 500, 500)
        self.setWindowTitle("Check kit ingredients")

        self.table_data1 = {'BMC': 'bmc_bhs_23.40-0', 'CPLD': 'bhs_gnr_avc_ap_4v0b_v3', 'CPLD_PFR': '652.1', 'CentOS': 'gnr-bkc-centos-stream-9-installer-minimal-6.2-10.6-34_update', 'IFWI': '2023.41.4.10_2713.d04_bhs_gnr_ap', 'LAN': 'network_drivers_v28_2_gnr_ap', 'QAT': 'qat21.l.1.2.1-00010', 'SAF': 'in_field_scan_app_4.2.12', 'SAF_Blob': 'saf_blob_file_gnr_a0_v2_ww28', 'SGX': '2.19.90.3-centos9', 'SGXFVT_Tool': 'v0.8.10.0-lnx', 'VROC_UEFI': '9.0.0.1028', 'dlb': 'release_ver_8.4.1', 'on_demand_agent': '3.1.0.1'}

        self.table_data2 = {'BMC': 'bmc_bhs_23.2240-0', 'CPLD': 'bhs_gnr_avc_ap_4v0b_v3', 'CPLD_PFR': '652.1', 'CentOS': 'gnr-bkc-centos-stream-9-installer-minimal-6.2-10.6-34_update', 'IFWI': '2023.41.4.10_2713.d04_bhs_gnr_ap', 'LAN': 'network_drivers_v28_2_gnr_ap', 'QAT': 'qat21.l.1.2.1-00010', 'SAF': 'in_field_scan_app_4.2.12', 'SAF_Blob': 'saf_blob_file_gnr_a0_v2_ww28', 'SGX': '2.19.90.3-centos9', 'SGXFVT_Tool': 'v0.8.10.0-lnx', 'VROC_UEFI': '9.0.0.1028', 'dlb': 'release_ver_8.4.1', 'on_demand_agent': '3.1.0.1'}


        self.table = QTableWidget(self)
        self.table.setGeometry(20, 80, 500, 270)
        self.table.setRowCount(len(self.table_data1))
        self.table.setColumnCount(2)
        self.table.setHorizontalHeaderLabels(["Ingredient", "Version"])

        for row, (ingredient, version) in enumerate(self.table_data1.items()):
            item_ingredient = QTableWidgetItem(ingredient)
            item_version = QTableWidgetItem(version)
            self.table.setItem(row, 0, item_ingredient)
            self.table.setItem(row, 1, item_version)

        self.button = QPushButton("Open Table", self)
        self.button.setGeometry(20, 370, 100, 30)
        self.button.clicked.connect(self.openTableWindow)

        self.show()

    def openTableWindow(self):
        window = TableWindow(self.table_data1, self.table_data2)
        window.exec_()

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = Example()
    sys.exit(app.exec_())