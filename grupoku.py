# a0 is the id

class Table():
	def __init__(self, n, id = 0):
		self.n = n
		self.table = []
		self.id = id
		
		# Generating table filled with 0's
		for i in range(n):
			self.table.append([])
			for j in range(n):
				self.table[i].append(0)
				
	
	def printTable(self):
		print("Table: ", end = '\n\n')
	
		n = self.n
		
		for j in range(n + 3):
			if (j < 3):
				print(" ", end = '')
			else:
				print("a" + str(j - 3), end = ' ')
		print('\n')
		
		for i in range(n):
			for j in range(n):
				if (j == 0): print("a" + str(i), end = ' ')
				print(self.table[i][j], end = ' ')
			print('\n')
	
	def setTable(self, newTable):
		self.table = newTable.copy()
		
	def alterTable(self, i, j, a):
		self.table[i][j] = a
	
	def check(self):
		return self.checkIdLaw() and self.checkInvLaw() and self.checkAssLaw()
		
	def checkIdLaw(self):		
		n = self.n
		id = self.id
		
		# for all a in G, id * a = a
		
		return all(self.operate(id, a) == a for a in range(n))
	
	def checkInvLaw(self):
		n = self.n
		id = self.id
		
		# for all a in G, there is a y such that a * y = id
		
		return all(any(self.operate(a, b) == id for b in range(n)) for a in range(n))
		
	def checkAssLaw(self):
		n = self.n
		
		# for all a,b and c, a*(b*c) = (a*b)*c
		
		return all(
			self.operate(a, self.operate(b, c)) == self.operate(self.operate(a, b), c) 
			for a in range(n) for b in range(n) for c in range(n)
		)
		
	def operate(self, a, b):
		return self.table[a][b]
		
t = Table(2)
t.setTable([

	[0, 1],
	[1, 0]


])
t.printTable()

print("Ass Law:", t.checkAssLaw())
print("Id Law:", t.checkIdLaw())
print("Inv Law:", t.checkInvLaw())

