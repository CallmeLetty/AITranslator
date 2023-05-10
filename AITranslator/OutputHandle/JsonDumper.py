import json
import pandas
import csv
import os

class JsonDumper(object):
    def __init__(self, json_dir,json_name):
        self.json_dir = json_dir
        self.json_path = os.path.join(self.json_dir,json_name)

    def jsonToCsv(self,csv_name):
        csv_path = os.path.join(self.json_dir,csv_name + '.csv')
        print(">> output csv path: " + csv_path)

        with open(self.json_path, 'r',encoding='utf-8',errors='ignore') as f:
            rows = json.load(f)
        
        f = open(csv_path,
                'w',
                encoding='utf-8')
        csv_write = csv.writer(f)

        # 先写入首行
        csv_write.writerow(rows[0].keys())
        
        for dict in rows:
            csv_write.writerow(dict.values()) 

        f.close()

    def jsonToXlsx(self,xlsx_name):
        xlsx_path = os.path.join(self.json_dir,xlsx_name + '.xlsx')
        print(">> output xlsx path: " + xlsx_path)
        # 打开文件
        with open(self.json_path) as f:
            data = json.load(f)  # 打开 json 文件
        f.close()

        dataFrame = pandas.DataFrame(data)
        dataFrame.to_excel(xlsx_path,index=False)
