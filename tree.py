class Tree:
	def __init__(self,left,right):
		self.left = left
		self.right = right
	def __str__(self):
		name = [k for k,v in locals().items() if v is self][0]
		return f'\t {name} \t \n \t{self.left} \t{self.right} \t'
