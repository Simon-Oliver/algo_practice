class Logger:
    def __init__(self, path, data):
        self.path = path
        self.data = data


class Printer:
    def __init__(self, data):
        print("---", data)


p = Printer({"name": "test"})
