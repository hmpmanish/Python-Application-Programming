import matplotlib.pyplot as plt
import numpy as np
# Example 1

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints)
plt.show()


# Example 2 (markers only)

import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 8])
ypoints = np.array([3, 10])

plt.plot(xpoints, ypoints ,'o')
plt.show()



# Example 3 (multiple points)
import matplotlib.pyplot as plt
import numpy as np

xpoints = np.array([1, 2 , 6 ,8])
ypoints = np.array([3,8 ,1 , 10])

plt.plot(xpoints, ypoints )
plt.show()


# Example 4 (default x)
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8 ,1 , 10])

plt.plot(xpoints, ypoints )
plt.show()


# Example 5 (markers)
import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8 ,1 , 10])

plt.plot(ypoints, marker ='*' )
plt.show()
# -------- Example 6: Format String --------

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8 ,1 , 10])

plt.plot(ypoints, 'o:r' )
plt.show()



# -------- Example 7: Line Width --------

import matplotlib.pyplot as plt
import numpy as np

ypoints = np.array([3,8 ,1 , 10])

plt.plot(ypoints, linewidth = '20.5' )
plt.show()


# -------- Example 8: Histogram --------
import matplotlib.pyplot as plt
import numpy as np

x= np.random.normal(170,10,250)

plt.hist(x)
plt.show()


# -------- Example 9 (Improved Histogram) --------

import matplotlib.pyplot as plt
import numpy as np

# Generate random data (mean=10000, std=100, size=1000)
data = np.random.normal(1000)

plt.hist(data, bins=30, color='skyblue', edgecolor='black')

plt.xlabel("Value")
plt.ylabel("Frequency")
plt.title("Basic Histogram")

plt.show()

































#create bar
#scatter plot
#pie chart
#subplot


