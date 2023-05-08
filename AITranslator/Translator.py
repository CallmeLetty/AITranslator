from Requestor import Requestor
import json, os
from collections import deque
import threadpool
import threading

class Translator:
    """backEnd"""

    def __init__(self, output: str = None):
        """
        Parameters
        ----------
        output
            指定输出地址
        """
        if not output:
            self.file_path = os.path.join(os.getcwd(), 'output.json')
        else:
            self.file_path = output

        self.__requestor = Requestor()
        self.index = 0
        self.queue = deque()
        self.__pool = threadpool.ThreadPool(9) # 核心数 + 1

    def sink(self, index):
        self.index = index

    def config(self, metaData: list[(str, str)], langs: list[str]):
        """配置元数据和翻译语种

        Parameters
        ----------
        metaData
            待翻译数据，(key, source)的元祖列表
        langs
            输出的语种
        """
        self.metaData = metaData
        self.langs = langs
    
    def translate(self) -> str:
        """执行翻译
                
        Retruns
        ----------
        翻译结果的json文件路径
        """
        result = []
        count = len(self.metaData)
        ## 逐条翻译（Loop）
        for i in range(self.index, count):
            key, text = self.metaData[i]
            res = self.__translate(text)
            res["key"] = key
            result.append(res)
            self.index += 1

        self.__writeToFile()

        return self.file_path
    
    def __callback(request, result):
        pass
    
    def __writeToFile(self, data):
        """写入到文件中"""
        with open(self.file_path, 'w') as f:
            json.dump(data, f, allow_unicode=True)

    def __translate(self, entry: str) -> dict:
        """通过gpt接口翻译词条"""
        result = self.__requestor.request(entry, self.langs)
        return result

        

