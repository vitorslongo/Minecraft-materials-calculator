import sys

from PySide6.QtWidgets import QApplication, QMainWindow, QTableWidgetItem
from ui_files.python_files.ui_main_window import Ui_MainWindow
from src.add_item import AddItem


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)
        self.setWindowTitle("Minecraft Materials Calculator")

        self.add_item_dialog = None
        # self.results = Results()
        
        self._create_callbacks()


    def _create_callbacks(self):
        # project actions
        self.main_window.pushButton_close.clicked.connect(self.close_callback)
        self.main_window.pushButton_open_project.clicked.connect(self.open_project_callback)
        self.main_window.pushButton_export_project.clicked.connect(self.export_project_callback)
        self.main_window.pushButton_save_project.clicked.connect(self.save_project_callback)

        # item requirement actions
        self.main_window.pushButton_reset.clicked.connect(self.reset_requirements_table_callback)
        self.main_window.pushButton_delete.clicked.connect(self.delete_item_callback)
        self.main_window.pushButton_add.clicked.connect(self.add_callback)


#  ==========================================================================================

    # callbacks
    def close_callback(self):
        self.close()

    def open_project_callback(self):
        self.open_project()

    def export_project_callback(self):
        self.export_project()

    def save_project_callback(self):
        self.save_project()

    def reset_requirements_table_callback(self):
        self.reset_requirements_table()

    def delete_item_callback(self):
        self.delete_item()

    def add_callback(self):
        self.open_add_item_dialog()
        

#  ==========================================================================================

    # methods
    def close(self):
        super().close()

    def open_project(self):
        print("Opening project...")

    def export_project(self):
        print("Exporting project...")

    def save_project(self):
        print("Saving project...")

    def reset_requirements_table(self):
        print("Resetting...")

    def delete_item(self):
        print("Deleting...")

    def open_add_item_dialog(self):
        print("opening")

        if self.add_item_dialog is None:
            self.add_item_dialog = AddItem()
            self.add_item_dialog.item_added.connect(self.add_item_to_list)
        self.add_item_dialog.show()
        
    def add_item_to_list(self, type, material, quantity, quantity_type):
        table = self.main_window.tableWidget_calculator
        row = table.rowCount()
        table.insertRow(row)

        if quantity_type == "stacks":
            stacks = float(quantity)
            items = stacks * 64
        else:
            items = float(quantity)
            stacks = items / 64

        table.setItem(row, 0, QTableWidgetItem(self._format_number(items)))
        table.setItem(row, 1, QTableWidgetItem(self._format_number(stacks)))
        table.setItem(row, 2, QTableWidgetItem(type))
        table.setItem(row, 3, QTableWidgetItem(material))
        print(f"Added: {type} | {material} | {quantity} {quantity_type}")

    def _format_number(self, value):
        if value.is_integer():
            return str(int(value))
        return f"{value:.2f}"
#  ==========================================================================================

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
