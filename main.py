import json
import math
import sys

from PySide6.QtCore import Qt
from PySide6.QtWidgets import (
    QAbstractItemView,
    QApplication,
    QFileDialog,
    QHeaderView,
    QMainWindow,
    QTableWidgetItem,
)

from src.add_item import AddItem
from src.results import Results
from ui_files.python_files.ui_main_window import Ui_MainWindow


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.main_window = Ui_MainWindow()
        self.main_window.setupUi(self)
        self.setWindowTitle("Minecraft Materials Calculator")

        self.add_item_dialog = None
        self.results = Results()
        self._setup_table_columns()
        self._disable_table_editing()
        self._setup_results_table_columns()

        self._create_callbacks()


    def _setup_table_columns(self):
        header = self.main_window.tableWidget_calculator.horizontalHeader()
        header.setStretchLastSection(False)
        for col in [0, 3]:
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.Stretch)
        for col in [1, 2, 4, 5]:
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.ResizeToContents)


    def _disable_table_editing(self):
        table = self.main_window.tableWidget_calculator
        table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)


    def _setup_results_table_columns(self):
        table = self.main_window.tableWidget_results
        table.setColumnCount(3)
        table.setHorizontalHeaderLabels(["Base item", "Total base items", "Stacks"])
        table.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        header = table.horizontalHeader()
        header.setSectionResizeMode(0, QHeaderView.ResizeMode.Stretch)
        for col in [1, 2]:
            header.setSectionResizeMode(col, QHeaderView.ResizeMode.ResizeToContents)


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
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Open Project", "", "Minecraft Calculator (*.json)"
        )
        if not file_path:
            return
        with open(file_path, "r", encoding="utf-8") as f:
            entries = json.load(f)

        table = self.main_window.tableWidget_calculator
        table.setRowCount(0)
        for entry in entries:
            type = entry.get("type", "")
            material = entry.get("material", "")
            items = entry.get("items", 0)
            self.add_item_to_list(type, material, 0, items)
        self._update_results_table()
        print(f"Opened project from {file_path}")

    def export_project(self):
        print("Exporting project...")

    def save_project(self):
        table = self.main_window.tableWidget_calculator
        entries = []
        for row in range(table.rowCount()):
            item = table.item(row, 0)
            if item is None:
                continue
            data = item.data(Qt.ItemDataRole.UserRole)
            if data is None:
                continue
            entries.append(data)

        file_path, _ = QFileDialog.getSaveFileName(
            self, "Save Project", "", "Minecraft Calculator (*.json)"
        )
        if not file_path:
            return
        if not file_path.lower().endswith(".json"):
            file_path += ".json"
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(entries, f, indent=2)
        print(f"Saved project to {file_path}")

    def reset_requirements_table(self):
        self.main_window.tableWidget_calculator.setRowCount(0)
        self._update_results_table()

    def delete_item(self):
        table = self.main_window.tableWidget_calculator
        row = table.currentRow()
        if row >= 0:
            table.removeRow(row)
            self._update_results_table()

    def open_add_item_dialog(self):
        print("opening")

        if self.add_item_dialog is None:
            self.add_item_dialog = AddItem()
            self.add_item_dialog.item_added.connect(self.add_item_to_list)
        self.add_item_dialog.show()
        
    def add_item_to_list(self, type, material, stacks, items):
        table = self.main_window.tableWidget_calculator
        row = table.rowCount()
        table.insertRow(row)

        stacks_val = float(stacks) if stacks else 0.0
        items_val = float(items) if items else 0.0
        total_items = items_val + stacks_val * 64

        full_stacks = int(total_items // 64)
        remaining = int(total_items % 64)

        multiplier = self.results.get_item_base_multiplier(type, material)
        base_items = math.ceil(total_items * multiplier)
        full_base_stacks = int(base_items // 64)
        remaining_base = int(base_items % 64)

        name = f"{material.capitalize()} {type}"
        base_name_raw = self.results.get_item_base_name(type, material)
        if base_name_raw and base_name_raw.lower() != type.lower() and base_name_raw.lower() != material.lower():
            base_name = f"{material.capitalize()} {base_name_raw}"
        else:
            base_name = material.capitalize()

        table.setItem(row, 0, QTableWidgetItem(name))
        table.setItem(row, 1, QTableWidgetItem(self._format_number(total_items)))
        table.setItem(row, 2, QTableWidgetItem(self._format_stacks(full_stacks, remaining)))
        table.setItem(row, 3, QTableWidgetItem(base_name))
        table.setItem(row, 4, QTableWidgetItem(self._format_number(base_items)))
        table.setItem(row, 5, QTableWidgetItem(self._format_stacks(full_base_stacks, remaining_base)))

        name_item = table.item(row, 0)
        name_item.setData(
            Qt.ItemDataRole.UserRole,
            {"type": type, "material": material, "items": total_items},
        )

        print(f"Added: {name} | {base_name} | {total_items} items | base {base_items}")
        self._update_results_table()

    def _update_results_table(self):
        calc_table = self.main_window.tableWidget_calculator
        totals = {}
        for row in range(calc_table.rowCount()):
            item = calc_table.item(row, 0)
            if item is None:
                continue
            data = item.data(Qt.ItemDataRole.UserRole)
            if data is None:
                continue
            type = data.get("type", "")
            material = data.get("material", "")
            total_items = float(data.get("items", 0))
            if not type or total_items == 0:
                continue
            multiplier = self.results.get_structure_to_base_multiplier(type, material)
            base_name = self.results.get_base_name(type, material)
            key = (material.lower(), base_name)
            totals[key] = totals.get(key, 0.0) + total_items * multiplier

        results_table = self.main_window.tableWidget_results
        results_table.setRowCount(0)
        for (material, base_name), amount in totals.items():
            row = results_table.rowCount()
            results_table.insertRow(row)
            total_base_items = math.ceil(amount)
            full_base_stacks = int(total_base_items // 64)
            remaining_base = int(total_base_items % 64)
            base_name_l = base_name.lower()
            if material and base_name_l and base_name_l == material.lower():
                label = base_name.capitalize()
            else:
                label = f"{material.capitalize()} {base_name}" if material else base_name
            results_table.setItem(row, 0, QTableWidgetItem(label))
            results_table.setItem(row, 1, QTableWidgetItem(self._format_number(total_base_items)))
            results_table.setItem(row, 2, QTableWidgetItem(self._format_stacks(full_base_stacks, remaining_base)))

    def _format_number(self, value):
        if value.is_integer():
            return str(int(value))
        return f"{value:.2f}"

    def _format_stacks(self, full_stacks, remaining):
        if full_stacks == 0:
            return "-"
        if remaining:
            return f"{full_stacks} stacks + {remaining}"
        return f"{full_stacks} stacks"


#=========================================================================================

def main():
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec()

if __name__ == "__main__":
    main()
