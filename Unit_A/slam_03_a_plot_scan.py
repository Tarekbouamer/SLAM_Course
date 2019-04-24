# Plot a scan of the robot using matplotlib.
# 03_a_plot_scan
# Claus Brenner, 09 NOV 2012
import pylab as plt
from lego_robot import LegoLogfile

# Read the logfile which contains all scans.
logfile = LegoLogfile()
logfile.read("robot4_scan.txt")

# Plot one scan.
plt.plot(logfile.scan_data[1])
plt.show()
