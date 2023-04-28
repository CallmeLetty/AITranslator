import os
import json
import openai

class Requestor(object):
    """openai请求"""
    def __init__(self):
        openai.api_key = os.getenv("OPENAI_API_KEY")

    def request(self,prompt):
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt=prompt,
            temperature=0.0,
            max_tokens=1000,
            top_p=0.1,
            n=1,
            frequency_penalty=0.0,
            presence_penalty=0.0,
            echo=False
        )
        return response.choices[0].text
    

if __name__ == '__main__':
    # p=PromptConstructor("/Users/doublecircle/Code/AI/AITranslator/Femometer_V2_0.0.3266.xlsx")
    
    # p=PromptConstructor("/Users/doublecircle/Desktop/test.xlsx")
    prompt ="Translate this into 1. Chinese 2. English 3. Turkish\n\n· Solo %s dopo la prova gratuita\n\n"
    text = Requestor().request(prompt)    
    print(text)