import json, os
import threadpool
from typing import Tuple

from Requestor import Requestor

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
        self.result = []
        self.__pool = threadpool.ThreadPool(9) # 核心数 + 1

    # 暂时放弃这个功能
    # def sink(self, index):
        # self.index = index

    def config(self, metaData: list[(str, str)], langs: list[str]):
        """配置元数据和翻译语种

        Parameters
        ----------
        metaData
            待翻译数据，(key, source)的元组
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
        requests = threadpool.makeRequests(self.__translate, self.metaData, self.__callback)
        [self.__pool.putRequest(req) for req in requests]
        self.__pool.wait()

        self.__writeToFile()

        return self.file_path
    
    def __callback(self, request, result):
        """多线程"""
        self.result.append(result)
        pass
    
    def __writeToFile(self):
        """写入到文件中"""
        with open(self.file_path, 'w') as f:
            json.dump(self.result, f, allow_unicode=True)

    def __translate(self, entry: Tuple(str, str)) -> dict:
        key, source = entry
        """通过gpt接口翻译词条"""
        result = self.__requestor.request(entry, self.langs)
        result[key] = source
        return result

        

