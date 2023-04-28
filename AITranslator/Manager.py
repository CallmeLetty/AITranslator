# import os
# import openai

import yaml
import re

from PromptConstructor import PromptConstructor
from Requestor import Requestor
from JsonDumper import JsonDumper

workspace_path = "/Users/doublecircle/Code/AI/AITranslator"

result = []

# excel_path = workspace_path + "/Fasting.xlsx"
# excel_path = "/Users/doublecircle/Desktop/test.xlsx"
excel_path = "/Users/doublecircle/Code/AI/AITranslator/Femometer_V2_0.0.3266.xlsx"
# excel_parser = ExcelParser(excel_path)

constructor = PromptConstructor(excel_path)
langs = constructor.langs
sources = constructor.source_map
keys = constructor.keys
#prompt_list = constructor.prompt_list()

requestor = Requestor()
for index, text in enumerate(prompt_list):
    if not text:
        continue

    # print(text)
    res = requestor.request(text)
    
    res = [line for line in res.split('\n') if line.strip() != '']
#1. 并且还有更多
#2. And more
#3. Ve daha fazlası
    item = {"Name": keys[index]}
    for index, line in enumerate(res):
        # res = re.match(r'(.+):\s(.+)', line)
        
        single = re.sub('\d\.', '', line)
        if res:
            item[langs[index]] = single
            # item[res.group(1)] = res.group(2)
    
    result.append(item)

# to json
destination_json = 'data.json'
jsonDumper = JsonDumper(workspace_path)
jsonDumper.dumpToFile(result)
destination_csv = 'data.csv'
jsonDumper.jsonToCsv(destination_json,destination_csv)

# to yaml
# with open(workspace_path + '/output.yaml', 'w') as f:
#     yaml.dump(result, f, allow_unicode=True)

