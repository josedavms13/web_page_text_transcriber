from openpyxl import Workbook
from openpyxl.styles import Border, Side


class Sheet:
    def __init__(self):
        self._available_column = ["B", "C", "D", "E", "F", "G", "H"]
        self._workbook = Workbook()
        self._sheet = self._workbook.active
        self._row = 1

    def get_column_by_importance(self, type_of: int):
        if type_of > len(self._available_column) - 1:
            return self._available_column[len(self._available_column) - 1]
        elif type_of < 0:
            return self._available_column[0]
        else:
            return self._available_column[type_of]

    def get_cell(self, type_of: int) -> str:
        return f"{self.get_column_by_importance(type_of)}{self._row}"

    def set_cell_border(self, cell: str):
        double = Side(border_style="double")
        border = Border(top=double, left=double, right=double, bottom=double)
        cell = self._sheet[cell]
        cell.border= border

    def type_in_cell(self, content: str, cell="", increase_count=True):
        current_cell = cell if len(cell) > 0 else f"C{self._row}"

        print(f"Imprimiendo en {current_cell}: \n"
              f"{content[0:16] + '...' if len(content) >= 15 else content} \n")
        self._sheet[current_cell] = content
        if increase_count:
            self._row += 1

    def type_title(self, content: str):
        self._row += 4
        self.type_in_cell("TITULO PRINCIPAL", self.get_cell(1), False)
        self.type_in_cell(content, self.get_cell(3))
        self._row += 4

    def type_sub_title(self, content: str):
        self._row += 3
        self.type_in_cell("SUB TITULO", self.get_cell(2), False)
        self.type_in_cell(content, self.get_cell(4))
        self._row += 3

    def type_paragraph(self, content: str):
        self._row += 1
        self.type_in_cell("PARRAFO", self.get_cell(4), False)
        self.type_in_cell(content, self.get_cell(6))
        self._row += 1

    def type_as_list(self, content: str):
        self._row += 2
        self.type_in_cell("LISTA", self.get_cell(5), False)
        self.set_cell_border(self.get_cell(6))
        self.type_in_cell(content, self.get_cell(6))
        self._row += 1

    def save(self, filename: str):
        print(f"Guardando en {filename}.xlsx")
        self._workbook.save(filename=f"{filename}.xlsx")
