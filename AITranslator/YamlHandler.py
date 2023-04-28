import yaml
import xlrd

#! /usr/bin/python3

from pathlib import Path

class ReadPath():
    """基本路径"""

    BasePath = Path(__file__).resolve().parents[1]
    # print(BasePath)


    def ini_path(self):
        """获取ini文件目录"""

        ini_path = ReadPath.BasePath/"data"/"test.ini"
        # print(ini_path)
        return ini_path

    def excel_path(self):
        """获取excel文件目录"""

        excel_path = ReadPath.BasePath/"data"/"test.xlsx"
        # print(excel_path)
        return excel_path

    def yaml_path(self):
        """获取yaml目录"""

        yaml_path = ReadPath.BasePath/"data"/"test.yaml"
        # print(yaml_path)
        return yaml_path


class YamlUtils(object):

    def __init__(self, filePath):
        self.fs = open(filePath, encoding="utf-8")

    def getAllConfigs(self):

        test_data = yaml.safe_load(self.fs)
        # 返回的数据像这样： {'user': ['eric', 'wallace', 'lily'], 'mail': ['12312312@qq.com', '324343@qq.com']}
        return test_data

    def getSection(self, section):
        test_data = yaml.safe_load(self.fs)
        return test_data[section]

    def writeYaml(self, jsonData):
        with open("config.yaml", encoding='utf-8', mode='w') as f:
            try:
                yaml.dump(data=jsonData, stream=f, allow_unicode=True)
            except Exception as e:
                print(e)


class YamlHandler(object):
    def __init__(self, file):
        self.file = file

    def read_yaml(self, encoding="utf-8"):
        """读取yaml文件"""
        with open(self.file, encoding=encoding, mode='r') as f:
            return yaml.load(f.read(), Loader=yaml.FullLoader)

    def write_yaml(self, data, encoding="utf-8"):
        """向yaml写入数据"""
        with open(self.file, encoding=encoding, mode='w') as f:
            return yaml.dump(data, stream=f, allow_unicode=True)

class ExcelData:

    def __init__(self):
        # 打开文件
        self.excel = xlrd.open_workbook("data1111.excel")
        # 通过下表定位表格
        self.sheet = self.excel.sheet_by_index(0)
        # 行和列的数量
        self.rows, self.cols = self.sheet.nrows, self.sheet.ncols

    def read_excel(self):
        # 获取第一行数据的key
        first_row = self.sheet.row_values(0)
        # print(first_row) [编号，method，host,param，result]
        # 定义空列表，用于存放用例数据
        self.result = []
        # 从第一行用例开始循环(1,4),
        for i in range(1, self.rows):
            # 定义空字典，
            info_dict = {}
            # 每次大循环要循环5次(字典理由五列字段)
            for j in range(0, self.cols):
                # j=0,1,2,3,4
                # 添加到字典
                info_dict[first_row[j]] = self.sheet.row_values(i)[j]
            self.result.append(info_dict)
        print(self.result)
        return self.result

# if __name__ == '__main__':
#     ex = ExcelData()
#     ex.read_excel()



class ReadYaml(object):
    def __init__(self):
        self.yaml_path = "data.yaml"
    def read_yaml(self):
        #open方法打开直接读出来
        file = open(self.yaml_path,'r',encoding="utf-8")
        result = file.read()
        #用load方法转字典
        dict = yaml.load(result,Loader=yaml.FullLoader)
        print(dict)
        return


if __name__ == '__main__':
    read = ReadYaml()
    read.read_yaml()