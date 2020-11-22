class ParserCfg:
    def __init__(self, path):
        self.deli = '-----'
        self.ans_quote = '@@@'
        self.path = path

    def parse(self):
        f = open(self.path, mode='r', encoding='utf-8').read()
        blocks = list(map(lambda x: x.strip(), f.split(self.deli)[:-1]))
        questions = [x.split(self.ans_quote)[0].strip() for x in blocks]
        answers = [x.split(self.ans_quote)[1].strip() for x in blocks]
        return questions, answers
