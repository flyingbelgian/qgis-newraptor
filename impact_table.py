from qgis.PyQt.QtWidgets import *
from PyQt5.QtWidgets import QDialog
from .new_raptor_dialog_impact import NewRaptorImpactDialog

class DialogTable(NewRaptorImpactDialog):
    def __init__(self):
        super(DialogTable, self).__init__()
        self.setupUi(self)

        self.table_impact.setColumnWidth(1, 150)