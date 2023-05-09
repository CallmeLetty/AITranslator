import csv
from AbstractParser import AbstractParser

class CsvParser(AbstractParser):
    """解析excel文件"""
    def __init__(self,csv_path):
        self.rows = []
        with open(csv_path, encoding='utf-8-sig') as f:
            for row in csv.reader(f, skipinitialspace=True):
                self.rows.append(row)
        f.close()

    def get_header_row(self):
        header_row = self.rows[0]
        header_row.pop(0)
        return header_row
    
    def get_header_column(self):
        header_column = []
        for values in self.rows:
            value = values[0]
            header_column.append(value)
        
        header_column.pop(0)
        return header_column
        
    """获取某一行的数据"""
    def get_row_value(self, row_num):
        row = self.rows[row_num + 1]
        row.pop(0)
        return row

    """获取某一列的数据"""
    def get_column_value(self, col_num):
        column = []
        for values in self.rows:
            value = values[col_num]
            column.append(value)
        
        column.pop(0)
        return column

    # """获取某一个单元格的数据"""
    # def get_cell_value(self, raw_no, col_no):
    #     sh = self.wb[self.sheet_name]
    #     value = sh.cell(raw_no, col_no).value
    #     return value

    # """向某个单元格写入数据"""
    # def write_cell(self, raw_no, col_no, value):
    #     sh = self.wb[self.sheet_name]
    #     sh.cell(raw_no, col_no).value = value
    #     self.wb.save(self.data_path)

if __name__ == '__main__':
    csv_path = '/Users/lettyliu/Git/AITranslator/AITranslator/InputHandle/csv_demo.csv'
    parser = CsvParser(csv_path)
    print(parser.get_header_row())
    print(parser.get_column_value(1))
