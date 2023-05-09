import os, re, openai
from Translator.Prompt import Prompt

class Requestor(object):
    """openai请求"""
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def request(self, entry, langs) -> dict:
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
        for line in lines:
            res = re.match(r'(.+):\s(.+)', line)
            if res:
                result[res.group(1)] = res.group(2)
            else:
                print("error: \n{}".format(line))
        return result
    

if __name__ == '__main__':    
    # p=PromptConstructor("/Users/doublecircle/Desktop/test.xlsx")
    prompt ="Translate this into 1. Chinese 2. English 3. Turkish\n\n· Solo %s dopo la prova gratuita\n\n"
    text = Requestor().request(prompt)    
    print(text)