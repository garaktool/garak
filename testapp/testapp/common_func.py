
class getInfo:
    def __init__(self):
        self.result = 0

    def get_code(self,name):
        self.result = name[name.rfind('(')+1:-1]
        return self.result