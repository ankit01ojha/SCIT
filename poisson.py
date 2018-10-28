import numpy as np
import matplotlib.pyplot as plt
import random

mean = 5
no_of_samples = 1000

def graphThousandSamples(mean, no_of_samples, i):
	data = np.random.poisson(mean, no_of_samples)
	count, bins, ignored = plt.hist(data, 14, density = True)
	plt.title('Histogram generated using numpy.random.poisson for 1000 samples')
	plt.savefig('Graphs/1000Poisson'+str(i)+'.png')
	plt.show()
	
for i in range(0,3):
	graphThousandSamples(mean,no_of_samples,i)

