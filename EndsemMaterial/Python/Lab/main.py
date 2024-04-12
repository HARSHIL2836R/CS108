'''
    Distributions
'''

import numpy as np
from matplotlib import pyplot as plt

# Seeding for reproducibility
rs = np.random.RandomState(np.random.MT19937(np.random.SeedSequence(987654321)))
size = 1000000

# sampling from each of the six distributions
beta = rs.beta(4, 20, size=size) * 100 #multiplied by 100
exp = rs.exponential(0.1, size=size) * 100
gamma = rs.gamma(2, 0.1, size=size) * 100
laplace = rs.laplace(0, 0.5, size=size) * 100
normal = rs.normal(0,3, size= size)
poisson = rs.poisson(3, size=size)

# plotting histograms for each of the distributions
# plt.subplot(3,2,1)
plt.subplot(321)
plt.hist(beta, range=(-5,50), color='red', bins=55)
plt.title("Beta")

plt.subplot(322)
plt.hist(exp, range=(-1,50), color='green', alpha=0.5, bins=51)
plt.title("Exponential")

plt.subplot(323)
plt.hist(gamma, range=(-1,50), color='black', alpha=0.8, orientation='horizontal', bins=51)
plt.title("Gamma")

plt.subplot(324)
plt.hist(laplace, range=(-1,50), color='orange', bins=51)
plt.title("Laplace")

plt.subplot(325)
plt.hist(normal, range=(-10,11), bins=21)
plt.title("Normal")

plt.subplot(326)
plt.hist(poisson, range=(-1,11), bins=12)
plt.title("Poisson")

# adjust the sub-plots to fit the titles and labels
plt.tight_layout()
# save the plot as plot.png
plt.savefig('plot.png')