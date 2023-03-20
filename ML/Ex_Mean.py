"""Mean
The mean value is the average value.
To calculate the mean, find the sum of all values, and divide the sum by the number of values:
(99+86+87+88+111+86+103+87+94+78+77+85+86) / 13 = 89.77"""

import numpy as np

speed = [99,86,87,88,111,86,103,87,94,78,77,85,86]
x = np.mean(speed)

print("%.2f"%x)