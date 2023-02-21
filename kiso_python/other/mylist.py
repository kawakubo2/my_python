class MyList(list):
	def sum_plus_value(self):
		sum = 0
		for n in self:
			if n > 0:
				sum += n
		return sum
	
	def remove_minus_value(self):
		for i in range(len(self)):
			if self[i] < 0:
				self[i] = 0
