import re


class Parser:
	def __init__(self, data):
		self.data = data

	def lawn_parser(self):
		if re.findall(r"^\d+ \d+$", self.data):
			fields = self.data.split(" ")
			x, y = int(fields[0]), int(fields[1])
			print(f"lawn data : {x}, {y}")
			return x, y

	def mower_parser(self):
		if re.findall(r"^\d+ \d+ [N|E|W|S]$", self.data):
			fields = self.data.split(" ")
			x, y, o = int(fields[0]), int(fields[1]), str(fields[2])
			print(f"mower data : {x}, {y}, {o}")
			return x, y, o

	def action_parser(self):
		if re.findall(r"^\D[A|G|D]+", self.data):
			fields = self.data.split(" ")
			action = fields[0]
			print(f"action parser : {action}")
			return action
