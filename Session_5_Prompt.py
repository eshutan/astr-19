import numpy as np
import math
from astropy.table import Table

#import libaries needed

def main():

	#define x where x is tabulated between 0 and 2pi with 1000 entries

	x = np.linspace(0,2*math.pi,1000)

	#create an Astropy table 'data' with 2 columns 
	#comparing sin(x) and x

	data = Table([np.sin(x),x], names = ['sin(x)', 'x'])

	#print the entire table 'data'

	data.pprint_all()

	#run program
	
if __name__ == '__main__':
	main()
