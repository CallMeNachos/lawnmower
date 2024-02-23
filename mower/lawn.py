from mower.parser import Parser


class Lawn(Parser):
    def __init__(self, data):
        super().__init__(data)
        self.limit_x, self.limit_y = self.lawn_parser()

    def __str__(self):
        return f"Lawn{{length={self.limit_x}, width={self.limit_y}}}"

    def area(self):
        return self.limit_x, self.limit_y
