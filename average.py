import numpy as np
import matplotlib.pyplot as plt
import random

mean = 5
no_of_samples = 1000
std_dev = 0.1


def graphHunderedSamples(mean, std_dev, no_of_samples, i):
	normal_data = np.random.normal(mean, std_dev, no_of_samples)
	poisson_data = np.random.poisson(mean, no_of_samples)

	average_data = []
	for i in range(0,100):
		rand_normal = random.randint(0,1000)
		rand_poisson = random.randint(0,1000)

		avg = (poisson_data[rand_poisson-1] + poisson_data[rand_normal-1])/ float(2)
		average_data.append(avg)
	counts, bins, ignored = plt.hist(average_data,30, density=True)

	plt.title('Histogram for average of Q1 and Q2 for 100 samples')
	plt.savefig('Graphs/Average/Average'+str(i)+'.png')
	
for i in range(0,100):
	graphHunderedSamples(mean,std_dev,no_of_samples, i)
