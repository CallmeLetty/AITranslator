# import re
import os, sys
from InputHandle.InputParser import InputParser
from InputHandle.InputParser import Source_Type
from Translator.Translator import Translator
from OutputHandle.JsonDumper import JsonDumper
from OutputHandle.OutputZipper import OutputZipper
from OutputHandle.OutputUploader import OutputUploader


# input: output/$date/$source

source_file = sys.argv[1]
output_dir_path = os.path.dirname(source_file) # output
output_dir_name = output_dir_path.split('/')[1]
output_json_name = 'output.json'
output_json_path = os.path.join(output_dir_path, output_json_name)

print(">> output directory: " + output_dir_path)

input_parser = InputParser(source_file)
translator = Translator(output_json_path)

# 1. 文件解析
langs = input_parser.langs()
entry_list = input_parser.entry_list()
print(">>>> languages:" + str(langs))
print(">>>> entry_list:" + str(entry_list))

# 2. AI翻译
translator.config(entry_list, langs)
translator.translate()

# 3. 文档生成处理
jsonDumper = JsonDumper(output_dir_path,output_json_name)
if input_parser.source_type == Source_Type.CSV:
    jsonDumper.jsonToCsv("output")
elif input_parser.source_type == Source_Type.XLSX:
    jsonDumper.jsonToXlsx("output")

# 4. 压缩
local_zip_path = output_dir_path +'.zip' # 压缩后文件夹的名字
zipper = OutputZipper()
zipper.zip(output_dir_path,local_zip_path)

# 5. 上传
uploader = OutputUploader()
remote_zip = uploader.upload(local_zip_path,output_dir_name)
uploader.notifyToFeishu(remote_zip)