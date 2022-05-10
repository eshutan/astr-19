import sys
import numpy as np
from scipy.special import erf

#computes probability of an event
#of magnitude x or greater from a 
#gaussian distribution

def event_probability(x,mu=0.0,s=1.0):
	#x is value of event
	#mu is gaussian mean
	#s is standard deviation
	z = np.fabs( (x-mu/s) )
	def zfunc(z):
		return 0.5*(1.0 + erf(z/2**0.5))

	#return event probability
	return 1.0-(zfunc(z)-zfunc(-1.*z))

def main():

	#default 3*sigma
	x = 3.0

	#command line input
	if(len(sys.argv)>1):
		x = float(sys.argv[1])

	#get the event probability 
	prob = event_probability(x)

	print(f"The Gaussian probability of events larger than |{x}| is {prob*100:15.13f}%.")
	print(f"The Gaussian probability of events smaller than |{x}| is {(1-prob)*100:15.13f}%.")

if __name__ == '__main__':
	main()
