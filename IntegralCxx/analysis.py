import numpy as np
import matplotlib.pyplot as plt

MarkerSize = 10

data = np.genfromtxt("analysis.txt", delimiter='\t')

p, t = data[:, 0], data[:, 1]

fig_width = 20 #inch
fig_height = fig_width / 16 * 9 #inch
fig_dpi = 100
fig = plt.figure(figsize = (fig_width, fig_height), dpi = fig_dpi)
ax = fig.add_subplot(111)

ax.plot(p, t, label = 'Time', marker = 'D', linestyle = '', markersize = MarkerSize)

ax.set_xlabel('number of processes')
ax.grid()
ax.set_xticks(p)

spup = t[0]/t
ax.plot(p, spup, 'rD', label = 'Speed up', markersize = MarkerSize)

eff = spup/p;

ax.plot(p, eff, 'bD', label = 'Efficiency', markersize = MarkerSize)


cost = t*p
ax.plot(p, cost, 'gD', label = 'Cost', markersize=MarkerSize)

ax.legend()
ax.set_title('C++ parallel computing')
fig.savefig('result1.png')

