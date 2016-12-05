# SimpleAdditionofMatrices-in-Python
# Simple Addition of Matrices written in Python

from System import *
from System.Collections.Generic import *
from System.Collections import *

class firstMatrix(object):
	def __init__(self):

	def matrix_create(self):
		self._obj = Scanner(System.)
		Console.WriteLine("Enter the rows and columns of the First Matrix“)
		self._m = self._obj.nextInt()
		self._n = self._obj.nextInt()
		Console.WriteLine("Enter the Array Elements of the First Matrix“)
		self._a = Array.CreateInstance(int, self._m)
		self._b = Array.CreateInstance(int, self._m)
		self._c = Array.CreateInstance(int, self._m)
		self._i = 0
		while self._i < self._m:
			self._j = 0
			while self._j < self._n:
				self._a[self._i][self._j] = self._obj.nextInt()
				self._j += 1
			self._i += 1

	def display(self):
		Console.WriteLine("The array of the First Matrix:“)
		i = 0
		while self._i < self._m:
			j = 0
			while self._j < self._n:
				Console.Write("\t" + self._a[self._i][self._j])
				self._j += 1
			Console.WriteLine()
			self._i += 1

	def secondMatrix_create(self):
		Console.WriteLine("Enter the Array Elements of the Second Matrix:”)
		self._i = 0
		while self._i < self._m:
			self._j = 0
			while self._j < self._n:
				self._b[self._i][self._j] = self._obj.nextInt()
				self._j += 1
			self._i += 1

	def second_display(self):
		Console.WriteLine("The Array of the Second Matrix:“)
		i = 0
		while self._i < self._m:
			j = 0
			while self._j < self._n:
				Console.Write("\t" + self._b[self._i][self._j])
				self._j += 1
			Console.WriteLine()
			self._i += 1

class secondMatrix(object):
	firstMatrix = property()

	def add(self):
		i = 0
		while i < m:
			j = 0
			while j < n:
				c[i][j] = a[i][j] + b[i][j]
				j += 1
			i += 1

	def add_display(self):
		Console.WriteLine("The Array of the New Matrix:“)
		i = 0
		while i < m:
			j = 0
			while j < n:
				Console.Write("\t" + c[i][j])
				j += 1
			Console.WriteLine()
			i += 1

class Main(object):
	def main(args):
		pass

	main = staticmethod(main)
