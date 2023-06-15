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
        keys_row = list(rows[0].keys())
        keys_row.remove("Name")
        keys_row.insert(0,"Name")
        csv_write.writerow(keys_row)

        for dict in rows:
            # 由于csv是纯文本文件，需要按照keys_row进行排序
            values = []
            for key in keys_row:
                values.append(dict.get(key))

            csv_write.writerow(values) 
            
        f.close()

    def jsonToXlsx(self,xlsx_name):
        xlsx_path = os.path.join(self.json_dir,xlsx_name + '.xlsx')
        print(">> output xlsx path: " + xlsx_path)
        # 打开文件
        with open(self.json_path) as f:
            data = json.load(f)  # 打开 json 文件
        f.close()

        keys_row = list(data[0].keys())
        keys_row.remove("Name")
        keys_row.insert(0,"Name")

        dataFrame = pandas.DataFrame(data,columns=keys_row)
        dataFrame.to_excel(xlsx_path,index=False)


if __name__ == '__main__':    
    output_dir_path = "/Users/lettyliu/Downloads/2023-06-15-09-53-25"
    output_json_name = 'output.json'
    jsonDumper = JsonDumper(output_dir_path,output_json_name)
    jsonDumper.jsonToCsv("output")

    # keys_row = ['English', 'German', 'Japanese', 'French', 'Italian', 'Portuguese', 'Traditional Chinese', 'Name']
