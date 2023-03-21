import numpy
import matplotlib.pyplot as plt

x = numpy.random.normal(5.0, 10.0, 100000)

plt.hist(x, 50)
plt.show()