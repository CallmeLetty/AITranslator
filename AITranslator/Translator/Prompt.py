

class Prompt:
    """提词构建类"""
    @staticmethod
    def prompt(entry: str, langs: list[str]) -> str:
        # map_values = map(lambda x: "{}.{}".format(x[0], x[1]), enumerate(langs))
        # lang_args = ', '.join(list(map_values))
        lang_args = ', '.join(langs)
        prompt = """Translate the text below into {}
        
        {}    

        """.format(lang_args, entry)

        return prompt
    