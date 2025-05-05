import matplotlib.pyplot as plt
import numpy as np
import time

# Turn on interactive mode
plt.ion()

# Create the figure and axis
fig, ax = plt.subplots()
x_data, y_data = [], []
line, = ax.plot([], [], 'b-')  # blue line

# Set axis limits (adjust as needed)
ax.set_xlim(0, 100)
ax.set_ylim(0, 1)

for i in range(100):
    x_data.append(i)
    y_data.append(np.random.rand())  # Simulate real-time data

    line.set_data(x_data, y_data)

    ax.relim()
    ax.autoscale_view()

    plt.draw()
    plt.pause(0.1)  # Pause for 0.1 second

print("Done plotting.")
plt.ioff()
plt.show()
