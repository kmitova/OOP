from project.table.table import Table


class InsideTable(Table):
    MAX_NUM = 50
    MIN_NUM = 1

    def __init__(self, table_number: int, capacity: int):
        super().__init__(table_number, capacity)

    @property
    def table_number(self):
        return self.__table_number

    @table_number.setter
    def table_number(self, value):
        if value < self.MIN_NUM or value > self.MAX_NUM:
            raise ValueError(f"Inside table's number must be between {self.MIN_NUM} and {self.MAX_NUM} inclusive!")
        self.__table_number = value



