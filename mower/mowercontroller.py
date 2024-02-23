from mower.mower import Mower


class MowerController:
	def __init__(self, line):
		self.limit_x, self.limit_y = line.split(" ")

	def setting(self, line):
		x, y, o = line.split(" ")
		self.mower = Mower(int(x), int(y), str(o), int(self.limit_x), int(self.limit_y))
		self.parcours = [(x, y, o)]
		return self.mower

	def get_position(self):
		return " ".join(self.mower.position())

	def lets_mow(self, instruction):
		for i in instruction:
			self.mower.action(i)
			self.parcours.append(self.get_position())
