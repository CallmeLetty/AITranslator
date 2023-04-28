import json
import csv

class JsonDumper(object):
    def __init__(self, workspace_path):
        self.workspace_path = workspace_path

    def dump(self, object):
        res = json.dumps(object,ensure_ascii=False)
        print(res)

    def dumpToFile(self, object,json_name):
        with open(self.workspace_path + json_name, 'w') as json_data:
            json.dump(object, json_data, ensure_ascii=False)

    def jsonToCsv(self,json_name,csv_name):
        json_path = self.workspace_path + json_name
        csv_path = self.workspace_path + csv_name

        with open(json_path, 'r',encoding='utf-8',errors='ignore') as f:
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
        


if __name__ == '__main__':
    list = [{'key': 'AlternateBilling_choosepage_andmore',
            'Chinese': ' 并且还有更多', 
            'English': ' And more', 
            'Turkish': ' Ve daha fazlası'}]
    workspace = "/Users/doublecircle/Code/AI/AITranslator/"
    dumper = JsonDumper(workspace)
    dumper.dumpToFile(list,'data.json')
    dumper.jsonToCsv('data.json','data.csv')