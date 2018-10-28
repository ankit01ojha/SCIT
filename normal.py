import numpy as np
import matplotlib.pyplot as plt
import random

mean = 5
no_of_samples = 1000
std_dev = 0.1

def graphThousandSamples(mean, no_of_samples, std_dev, i):
	data = np.random.normal(mean, std_dev, no_of_samples)
	count, bins, ignored = plt.hist(data, 30, density = True)
	plt.plot(bins, 1/(std_dev * np.sqrt(2 * np.pi)) *np.exp( - (bins - mean)**2 / (2 * std_dev**2) ),linewidth=2, color='r')
	plt.title('Histogram generated using numpy.random.normal for 1000 samples')
	plt.savefig('Graphs/1000Normal'+str(i)+'.png')
	plt.show()
	

for i in range(0,3):
	graphThousandSamples(mean,no_of_samples, std_dev,i)

'''We can infer from the graphs is that graph is in bell shape and symmetrical on both sides and denser at center than it is at its tails.'''
