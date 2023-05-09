import json
import pandas
import csv
import os

class JsonDumper(object):
    def __init__(self, json_dir,json_name):
        self.json_dir = json_dir
        self.json_path = os.path.join(self.json_dir,json_name)

    def jsonToCsv(self,csv_name):
        csv_path = self.json_dir + csv_name + '.csv'

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
        # 打开文件
        with open(self.json_path) as f:
            data = json.load(f)  # 打开 json 文件
        f.close()

        dataFrame = pandas.DataFrame(data)
        dataFrame.to_excel(xlsx_name + '.xlsx',index=False)


if __name__ == '__main__':
    # json_path = "/Users/lettyliu/Git/AITranslator/AITranslator/OutputHandle"
    # json_name = "js_str.json"
    # dumper = JsonDumper(json_path,json_name)
    # dumper.jsonToXlsx("output")

    srmdir_all_folder = "/Users/lettyliu/Git/AITranslator/AITranslator/OutputHandle" # 文件夹路径
    zip_file_path = srmdir_all_folder + '.zip'
    print('原始文件夹路径: ', srmdir_all_folder)

    zip_file = zipfile.ZipFile(zip_file_path, 'w', zipfile.ZIP_DEFLATED)  # 创建空的 zip文件
    zip_file.write(srmdir_all_folder, 'srmdir_all')
    for dirpath, dirnames, filenames in os.walk(srmdir_all_folder):
        fpath = dirpath.replace(srmdir_all_folder, '')  # 获取 相对文件夹的路径
        fpath = fpath and fpath + os.sep or os.sep  # 添加 '/'
        for filename in filenames:
            print(filename)
            zip_file.write(os.path.join(dirpath, filename), 'srmdir_all' + fpath + filename)
                
    zip_file.close()



    f = zipfile.ZipFile("output.zip", 'w', zipfile.ZIP_DEFLATED)
    f.write(srmdir_all_folder,"output.zip")
    f.close()