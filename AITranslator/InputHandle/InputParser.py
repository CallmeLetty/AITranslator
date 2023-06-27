import os
from enum import Enum

from InputHandle.CsvParser import CsvParser
from InputHandle.ExcelParser import ExcelParser
from InputHandle.AbstractParser import AbstractParser

class Source_Type(Enum):
    XLSX  = 0
    CSV   = 1 

class InputParser(object):
    def __init__(self,source_file):
        ext = os.path.splitext(source_file)[1]

        if ext == ".csv":
            self.parser = CsvParser(source_file)
            self.source_type = Source_Type.CSV
        elif ext == ".xlsx":
            self.parser = ExcelParser(source_file)
            self.source_type = Source_Type.XLSX
    
    def langs(self):
        return self.parser.get_header_row()
    
    """获取所有的key与index的映射"""
    def keys(self):
        if self.source_type == Source_Type.CSV:
            return self.parser.get_column_value(0)
        elif self.source_type == Source_Type.XLSX:
            return self.parser.get_column_value(1)
        
    def entry_list(self):
        keys = self.keys()

        entry_list = []

        for index in range(0, len(keys)):
            key = keys[index]

            # 过滤掉key为空的情况
            if not key: 
                continue

            # 取第一个不为空的值作为source（不关心语言）
            current_row = self.parser.get_row_value(index)
            # if self.source_type == Source_Type.XLSX:
            #     current_row = current_row[1:]
            
            # 过滤掉已经翻译完成的行
            # if None not in current_row:
            #     continue

            for word in current_row:
                if not word:
                    continue

                entry_list.append((key,word))
                break

        return entry_list

if __name__ == '__main__':
    csv_path = '/Users/hg/Downloads/Fasting课程内容-lessonkey.csv'
    # xlsx_path = '/Users/lettyliu/Git/AITranslator/AITranslator/InputHandle/Femometer_V2_0.0.3266.xlsx'
    # parser = InputParser(csv_path)
    inputParser_csv = InputParser(csv_path)
    # inputParser_xlsx = InputParser(xlsx_path)

    csv_keys = inputParser_csv.keys()
    # xlsx_keys = inputParser_xlsx.keys()

    for item in inputParser_csv.entry_list()[:20]:
        print(item)
        print(",")
    # inputParser_xlsx.test()
    # print(inputParser_xlsx.keys())
