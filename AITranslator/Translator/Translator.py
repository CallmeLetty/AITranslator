import json, os
import threadpool

from Translator.Requestor import Requestor

class Translator:
    """backEnd"""

    def __init__(self, output: str):
        """
        Parameters
        ----------
        output
            指定输出地址
        """
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
        args_list = [([key, source], None) for key, source in self.metaData]
        requests = threadpool.makeRequests(
            self.__translate, 
            args_list, 
            self.__callback)
        
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
            json.dump(self.result, f, ensure_ascii=False)

    def __translate(self, key: str, source: str) -> dict:
        """通过gpt接口翻译词条"""
        result = self.__requestor.request(source, self.langs)
        result["key"] = key
        return result

if __name__ == '__main__':    
    translator = Translator()
    data = [('lesson2_title', 'The Benefits of Intermittent Fasting')
,
('lesson2_1', 'Many people fast to burn fat and lose weight, but the benefits are much more than that. In brief, it provides you with a healthier body, a sharper mind and a longer life!')
,
('lesson2_2', 'Diabetes and Obesity')
,
('lesson2_3', 'Fasting improves Insulin Resistance and helps keep blood sugar level stable. It prevents obesity caused by a high-fat diet, and improves diabetic retinopathy. Research studies show that obese adult lose weight through intermittent fasting.')
,
('lesson2_4', 'Reduce Diseases')
,
('lesson2_5', 'Intermittent fasting improves multiple indicators of cardiovascular health, including')
,
('lesson2_6', 'blood pressure, resting heart rate, levels of HDL and LDL cholesterol.')
,
('lesson2_7', 'Animal and cell studies also show its positive effects on cutting cancer risk.')
,
('lesson2_8', 'Clear Mind')
,
('lesson2_9', 'Studies discovered that intermittent fasting boosts working memory in animals and verbal memory in adult humans. Fasting also boosts brain function in terms of brain structure and nerve cell growth. So it could help')
,
('lesson2_10', 'improve memory and give you a clear mind.')
,
('lesson2_11', 'A stable blood sugar level also helps avoid violent mood swings.')
,
('lesson2_12', 'Better Sleep')
,
('lesson2_13', 'Some studies say fasting improves sleep by lowering the amount of rapid eye movement (REM) sleep. Other studies suggest fasting might raise the levels of chemicals that make you feel more awake during the day.')
,
('lesson2_14', 'Strong Immune and Longer Life')
,
('lesson2_15', 'The way cells respond to intermittent fasting, leads to')
,
('lesson2_16', 'increased expression of antioxidant defenses, DNA repair and autophagy,')
,
('lesson2_17', 'which are your body’s natural way of cleaning damaged cells and recycling of useful cellular components. These lead to potentially great results, like a stronger immune system and a longer life.')
,
('lesson2_18', 'Other benefits of fasting include clearer skin, easing inflammation and generally feeling good. In fact, fasting is not only a weight-loss method but also a way to lead a healthier lifestyle which you can encourage your friends and family to do alongside you.')
,
('lesson3_title', 'How Does Fasting Help Me Lose Weight?')
]
    translator.config(data, langs=["Chinese", "English", "Japanese"])
    translator.translate()
    