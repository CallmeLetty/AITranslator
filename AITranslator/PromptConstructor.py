from ExcelParser import ExcelParser

class PromptConstructor(object):
    def __init__(self,excelPath):
        self.parser = ExcelParser(excelPath)
        self.source_map = []

        self.langs = self.parser.get_row_value(1)
        self.keys = self.parser.get_column_value(1)
        self.__source_map__()

    def __source_map__(self):
        index_list = []
        # 过滤self.keys中的空值
        for index in range(0, len(self.keys)):
            key = self.keys[index]
            if not key:
                continue
            index_list.append(index)

        # souce add (from_source_word的判断)
        self.source_map = {}
        for index in range(0, len(self.keys)):
            if not index in index_list:
                continue
            key = self.keys[index]

            # source判断（取该行中不为空的值）
            current_row = self.parser.get_row_value(index+2)

            # 过滤掉已经翻译完成的行
            if None not in current_row:
                continue

            # 取第一个不为空的值作为source（不关心语言）
            for word in current_row:
                if not word:
                    continue

                self.source_map[key] = word
                break

    def prompt_list(self):
        if len(self.source_map) == 0:
            self.__source_map__()

        # promptPrefix = "Translate this into "
        promptPrefix = "Translate the text below into "
        for index in range(0, len(self.langs)):
            promptPrefix = promptPrefix+str(index+1)+"."+self.langs[index]+" "
        
        to_trans_list = []
        for key,source in self.source_map.items():
            singlePrompt = promptPrefix + "\n\n" + source + "\n\n"
            to_trans_list.append(singlePrompt)

        return to_trans_list

if __name__ == '__main__':
    p=PromptConstructor("/Users/doublecircle/Code/AI/AITranslator/Femometer_V2_0.0.3266.xlsx")
    
    # p=PromptConstructor("/Users/doublecircle/Desktop/test.xlsx")
    # print(p.langs)
    # print(p.source_map)
    prompt = p.prompt_list()
    print(prompt[0])
