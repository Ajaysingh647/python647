# arange
# find the graph of the sine amd cosine from math to print his range graph.

import matplotlib.pyplot as plt
import numpy as np
k=np.arange(0,10,.25)
value=np.sin(k)

plt.plot(k,value,linewidth=10)
plt.show