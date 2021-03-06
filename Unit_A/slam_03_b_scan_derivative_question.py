# Compute the derivative of a scan.
# 03_b_scan_derivative
# Claus Brenner, 09 NOV 2012
import pylab as plt

import Unit_A.lego_robot as CL


# Find the derivative in scan data, ignoring invalid measurements.
def compute_derivative(scan, min_dist):
    jumps = [0]
    for i in range(1, len(scan) - 1):
        head = scan[i + 1]
        tail = scan[i - 1]
        if (head > min_dist and tail > min_dist):
            jump = 0.5 * (head - tail)
            jumps.append(jump)
        else:
            jumps.append(0)

    jumps.append(0)
    return jumps


if __name__ == '__main__':

    minimum_valid_distance = 20.0

    # Read the logfile which contains all scans.
    logfile = CL.LegoLogfile()
    logfile.read("robot4_scan.txt")

    # Pick one scan.
    scan_no = 5
    scan = logfile.scan_data[scan_no]
    # Compute derivative, (-1, 0, 1) mask.
    der = compute_derivative(scan, minimum_valid_distance)

    # Plot scan and derivative.
    plt.title("Plot of scan %d" % scan_no)
    plt.plot(scan)
    plt.plot(der)
    plt.show()
