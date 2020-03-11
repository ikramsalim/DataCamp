
"""
Import the numpy package under the local alias np.
Write a for loop that iterates over all elements in np_height and prints out "x inches" for each element, where x is the value in the array.
Write a for loop that visits every element of the np_baseball array and prints it out.
"""
# Import numpy as np
import numpy as np

# For loop over np_height -> it's 1D Numpy array
for x in np_height :
    print( str(x) + " inches")

# For loop over np_baseball -> 2D Numpy array
for x in np.nditer(np_baseball) :
    print(x)
"""
LOOPING OVER 2D Numpy Array
for x in np.nditer(my_array) :
    ...

LOOPING OVER 1D Numpy Array
for x in my_array :
    ...
"""
