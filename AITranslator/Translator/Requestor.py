import os
import re
import openai
from Translator.Prompt import Prompt

class Requestor(object):
    """openai请求"""
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def request(self, entry, langs) -> dict:
        self.langs = langs
        prompt = Prompt.prompt(entry=entry, langs=langs)
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.0,
            max_tokens=3000,
            top_p=0.1,
            n=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            echo=False
        )
        rawData = response.choices[0].text
        return self.__processResponse(rawData)
        
    def __processResponse(self, data):
        """解析返回值"""
        lines = [line for line in data.split('\n') if line.strip() != '']
        result = dict()
        for index, line in enumerate(lines):
            res = re.match(r'(.+)[:：]\s?(.+)', line)
            if index < len(self.langs):
                lang = self.langs[index]
            else:
                print("error: Parse out of bounds")
                break

            if res:
                result[lang] = res.group(2)
            else:
                print("error: \n{}".format(line))
        
        return result
    

if __name__ == '__main__':    
    # p=PromptConstructor("/Users/doublecircle/Desktop/test.xlsx")
    val = "間歇性斷食可以改善多種心血管健康指標，包括"
    text = Requestor().request(val, ["Traditional Chinese",	"English",	"German",	"Japanese",	"French",	"Italian",	"Portuguese"])
    print(text)