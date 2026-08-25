import sys

from PySide6.QtWidgets import QApplication, QMainWindow
from ui_files.ui_main_window import Ui_MainWindow
from src.calculator import Calculator


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)
        self.setWindowTitle("Minecraft Materials Calculator")

        calculator = Calculator()
        
        self._create_connections()
        self._create_callbacks()


    def _create_connections(self):
        # project actions
        self.main_window.pushButton_close.clicked.connect(self.close_callback)
        self.main_window.pushButton_open_project.clicked.connect(self.open_project_callback)
        self.main_window.pushButton_export_project.clicked.connect(self.export_project_callback)
        self.main_window.pushButton_save_project.clicked.connect(self.save_project_callback)

        # item requirement actions
        self.main_window.pushButton_reset.clicked.connect(self.reset_requirements_table_callback)
        self.main_window.pushButton_delete.clicked.connect(self.delete_item_callback)
        self.main_window.pushButton_add.clicked.connect(self.add_item_callback)

    def _create_callbacks(self):
        self.close_callback = self.close
        self.open_project_callback = self.open_project
        self.export_project_callback = self.export_project
        self.save_project_callback = self.save_project
        self.reset_requirements_table_callback = self.reset_requirements_table
        self.delete_item_callback = self.delete_item
        self.add_item_callback = self.add_item

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

    def add_item_callback(self):
        self.add_item()

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

    def add_item(self):
        print("Adding...")
        

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()

if __name__ == "__main__":
    main()
