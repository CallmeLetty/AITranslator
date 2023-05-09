# import re
import os
import sys
from InputHandle.InputParser import InputParser
from InputHandle.InputParser import Source_Type
from Translator.Translator import Translator
from OutputHandle.JsonDumper import JsonDumper
from OutputHandle.OutputZipper import OutputZipper

# workspace_path = os.path.dirname(__file__)
source_file = sys.argv[1]
output_dir = os.path.dirname(source_file)
output_json_name = 'output.json'
output_json_path = os.path.join(output_dir, output_json_name)

input_parser = InputParser(source_file)
translator = Translator(output_json_path)

# 1. 文件解析
langs = input_parser.langs()
entry_list = input_parser.entry_list()

# 2. AI翻译
translator.config(entry_list, langs)
translator.translate()

# 3. 文档生成处理
jsonDumper = JsonDumper(output_dir,output_json_name)
if input_parser.source_type == Source_Type.CSV:
    jsonDumper.jsonToCsv("output")
elif input_parser.source_type == Source_Type.XLSX:
    jsonDumper.jsonToXlsx("output")

# 4. 压缩
file_news = output_dir +'.zip' # 压缩后文件夹的名字
zipper = OutputZipper()
zipper.zip_ya(output_dir,file_news)