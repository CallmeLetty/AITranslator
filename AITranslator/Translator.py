from Requestor import Requestor
from Prompt import Prompt
import json, os

class Translator:
    """backEnd"""
    def __init__(self):
        self.__file_path = os.path.join(os.getcwd(), 'output.json')
        self.__requestor = Requestor()
        self.index = 0
        pass

    def sink(self, index):
        self.index = index

    """metaData tuple (key, source)"""
    def config(self, metaData: list, langs: list[str]):
        """配置元数据和翻译语种"""
        self.metaData = metaData
        self.langs = langs
    
    def translate(self) -> str:
        """批量翻译， 返回json文件路径"""
        ## 逐条翻译（Loop）
        result = []
        count = len(self.metaData)
        for i in range(self.index, count):
            key, text = self.metaData[i]
            res = self.__translate(text)
            res["key"] = key
            result.append(res)
            self.index += 1

        self.__writeToFile()
        return self.__file_path
    
    def __writeToFile(self, data):
        """写入到文件中"""
        with open(self.__file_path, 'w') as f:
            json.dump(data, f, allow_unicode=True)

    def __translate(self, entry: str) -> dict:
        """通过gpt接口翻译词条"""
        result = self.__requestor.request(entry, self.langs)
        return result

        

