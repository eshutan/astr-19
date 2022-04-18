import sys #import sys

 #define class to describe favorite animal

class FavAnimal:

	def printFunction(self): 

		#describes characteristics of favorite animal

		print("My favorite animal is a wolf!")
		print(f"Length of the arms = {self.length_arms} inches")
		print(f"Length of the legs = {self.length_legs} inches")
		print(f"Number of eyes = {self.num_eyes}")
		print(f"Does it have a tail? = {self.tail}")
		print(f"Is it furry? = {self.furry}")

		#sets/initilizes default values of class's attributes 

	def __init__(self, length=5., numEyes=2, tail=True, furry=True):
		self.length_arms = length
		self.length_legs = length
		self.num_eyes = numEyes
		self.tail = tail
		self.furry = furry

def main():	

	#Creates an object from the FavAnimal class and assigns attributes

	MyFavAnimal = FavAnimal(length=5., numEyes=2, tail=True, furry=True)

	#Calls new object with printFunction()

	MyFavAnimal.printFunction() 

if __name__=="__main__":
	main()



	