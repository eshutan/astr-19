import sys #import sys

class FavAnimal: #define class to describe favorite animal

	def printFunction(self): 

		#describes characteristics of favorite animal

		print("My favorite animal is a wolf!")
		print(f"Length of the arms = {self.length_arms} inches")
		print(f"Length of the legs = {self.length_legs} inches")
		print(f"Number of eyes = {self.num_eyes}")
		print(f"Does it have a tail? = {self.tail}")
		print(f"Is it furry? = {self.furry}")

	def __init__(self, length=5., numEyes=2, tail=True, furry=True):
		self.length_arms = length
		self.length_legs = length
		self.num_eyes = numEyes
		self.tail = tail
		self.furry = furry

def main():

	length=5.
	numEyes=2
	tail=True
	furry=True

	MyFavAnimal = FavAnimal(length=length, numEyes=numEyes, tail=tail, furry=furry)
	MyFavAnimal.printFunction()

if __name__=="__main__":
	main()



	