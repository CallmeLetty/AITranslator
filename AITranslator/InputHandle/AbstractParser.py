from abc import ABC, abstractmethod

class AbstractParser(ABC):
    @abstractmethod
    def get_header_row(self):
        pass
    def get_header_column(self):
        pass
    def get_row_value(self, row_num):
        pass
    def get_column_value(self, col_num):
        pass

 