#Prints the Sum
#of 2 floating-point
#numbers
def PrintSum():
	a = 2.0+2.0
	print(a)
	print(type(a))

#Prints the difference
#between 2 integers
def PrintDif():
	a = 4/2
	print(a)
	print(type(a))

#Prints the product
#of a float num
#and integer
def PrintProd():
	a = 2.0*5
	print(a)
	print(type(a))

#defines main function
def main():
	PrintSum()
	PrintDif()
	PrintProd()

#excutes main function
if __name__=="__main__":
	main()	