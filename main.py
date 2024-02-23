from mower.mowercontroller import MowerController


def read_file(file):
	with open(file, "r") as f:
		data = f.read().split("\n")
	return data


def execute_mower(data):
	positions = []
	for i, line in enumerate(data):
		if i == 0:
			mowercontroller = MowerController(line)
		elif i % 2 != 0:
			if line in positions:
				print("A mower is already at this place")
			else:
				mowercontroller.setting(line)
		else:
			mowercontroller.lets_mow(line)
			positions.append(mowercontroller.get_position())
	for p in positions:
		print(p)


if __name__ == "__main__":
	data = read_file("src/data.txt")
	execute_mower(data)
