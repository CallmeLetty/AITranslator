class Prompt:
    """提词构建类"""
    @staticmethod
    def prompt(cls, entry: str, langs: list[str]) -> str:
        prompt = """Translate the text below into {}
        
        {}    

        """.format(' '.join(langs), entry)

        return prompt
    