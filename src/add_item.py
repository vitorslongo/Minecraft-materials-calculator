from PySide6.QtCore import Signal
from PySide6.QtWidgets import QDialog
from ui_files.python_files.ui_add_item_dialog import Ui_AddItem


class AddItem(QDialog):
    item_added = Signal(str, str, str, str)  # type, material, stacks, items

    def __init__(self):
        super().__init__()
        self.materials = {}
        self.ui = Ui_AddItem()
        self.ui.setupUi(self)
        self._create_callbacks()

    def _create_callbacks(self):
        self.ui.pushButton_add.clicked.connect(self.add_item_callback)
        self.ui.pushButton_clear.clicked.connect(self.clear_inputs_callback)

    def add_item_callback(self):
        type, material, stacks, items = self.get_item_info()
        self.item_added.emit(type, material, stacks, items)
        self.clear_inputs()

    def clear_inputs_callback(self):
        self.clear_inputs()

    def get_item_info(self):
        type = self.ui.lineEdit_item_type.text()
        material = self.ui.lineEdit_material.text()
        stacks = self.ui.lineEdit_quantity_stacks.text()
        items = self.ui.lineEdit_quantity_items.text()
        return type, material, stacks, items

    def clear_inputs(self):
        self.ui.lineEdit_item_type.clear()
        self.ui.lineEdit_material.clear()
        self.ui.lineEdit_quantity_stacks.clear()
        self.ui.lineEdit_quantity_items.clear()
