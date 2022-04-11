def f(x):				#defines the function f(x)
	return(x**3+8)		#as x^3+8

def main():				#defines main function
	print(f(9))			#prints f(x) where x = 9
	if f(9) > 27:		#if result is greater than 27
		print("YAY!")	#prints out this statement

if __name__ == "__main__":	#runs main function
	main()