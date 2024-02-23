class Mower:
    LEFT = "G"
    RIGHT = "D"
    FORWARD = "A"

    def __init__(self, x: int, y: int, o: str, limit_x: int, limit_y: int):
        self.x = x
        self.y = y
        self.o = o
        self.limit_x = limit_x
        self.limit_y = limit_y

    def position(self):
        return str(self.x), str(self.y), str(self.o)

    def action(self, instruction):
        if isinstance(instruction, str):
            if self.FORWARD == instruction:
                self.movement()
            elif instruction in [self.LEFT, self.RIGHT]:
                self.orientation(instruction)
            else:
                raise ValueError("instruction must be 'A', 'G' or 'D'")
        else:
            raise TypeError("'instruction' must be str type")

    def movement(self):
        if self.o == "S" and self.y > 0:
            self.y -= 1
        elif self.o == "N" and self.y < self.limit_y:
            self.y += 1
        elif self.o == "E" and self.x < self.limit_x:
            self.x += 1
        elif self.o == "W" and self.x > 0:
            self.x -= 1

        return f"movement {{x={self.x}, y={self.y}, o={self.o}}}"

    def orientation(self, turn: str):
        direction = ['N', 'E', 'S', 'W']
        if self.o not in direction:
            raise ValueError(f"direction must be 'N', 'E', 'S' or 'W'")
        current_direction = direction.index(self.o)
        if self.LEFT == turn:
            try:
                val = current_direction - 1
                self.o = direction[val]
            except IndexError:
                self.o = "N"
        elif self.RIGHT == turn:
            try:
                val = current_direction + 1
                self.o = direction[val]
            except IndexError:
                self.o = "N"
        return self.o
