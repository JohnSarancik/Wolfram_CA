# install Pygame Zero with: pip install pgzero
# docs: https://pygame-zero.readthedocs.io/

import pgzrun
import math

WIDTH = 800   # window dimensions
HEIGHT = 600


def decimal_to_binary(num):
    return [int(d) for d in bin(num)[2:]]   # list comprehension for binary number

decimal_val = int(input("Enter a number: "))
binary_num = decimal_to_binary(decimal_val)
print(binary_num)

class CA:
	def __init__(self, cells=[1], num_cells = 100):
		self.cells = [0] * (math.floor((num_cells-len(cells))/2)) + cells + [0] * (math.ceil((num_cells-len(cells))/2))
		self.ruleset = binary_num  # number 165 in binary
		self.w = WIDTH / num_cells               # size of a cell in px
		self.generation = 0                      # current generation

	def generate(self):
		"""Calculate a new generation of cells from the current ones."""
		nextgen = self.cells.copy()
		# for i in range(1, len(self.cells)-1):
		for i in range(0, len(self.cells)):
			if i == (len(self.cells)-1):
				left  = self.cells[i-1]
				same  = self.cells[i]
				right = self.cells[0]
			else:
				left  = self.cells[i-1]
				same  = self.cells[i]
				right = self.cells[i+1]
			# if not right:	# if the right doesnt exist
			# 	right = self.cells[0]	# use the first element
			# else:
			# 	right = self.cells[i+1]
			nextgen[i] = self.rules(left, same, right)
		self.cells = nextgen
		self.generation += 1

	def rules(self, left, same, right):
		"""Lookup a rule by a given neighborhood of cells."""
		rule = left << 2 | same << 1 | right
		return self.ruleset[rule]

	def draw(self):
		"""Draw the current generation to the screen."""
		for i in range(len(self.cells)):
			cell = Rect((i*self.w, self.generation*self.w), (self.w, self.w))
			if self.cells[i] == 0:
				screen.draw.filled_rect(cell, (255, 255, 255))
			else:
				screen.draw.filled_rect(cell, (0, 0, 0))

	def draw_ruleset(self):
		"""Draw the ruleset to the screen."""
		for rule in range(8):
			for bit in range(3):
				if rule & (1 << bit):
					screen.draw.filled_rect(Rect((WIDTH-10-rule*50-(1+bit)*10, HEIGHT-30), (10, 10)), (0, 0, 0))
				else:
					screen.draw.rect(Rect((WIDTH-10-rule*50-(1+bit)*10, HEIGHT-30), (10, 10)), (0, 0, 0))
			if self.ruleset[rule] == 0:
				screen.draw.rect(Rect((WIDTH-rule*50-30, HEIGHT-20), (10, 10)), (0, 0, 0))
			else:
				screen.draw.filled_rect(Rect((WIDTH-rule*50-30, HEIGHT-20), (10, 10)), (0, 0, 0))

ca = CA()

def draw():
	screen.fill((255, 255, 255))
	ca.draw()
	for generation in range(math.ceil(HEIGHT/ca.w)):
		ca.generate()
		ca.draw()
	# optional: draw ruleset
	#ca.draw_ruleset()



pgzrun.go()
