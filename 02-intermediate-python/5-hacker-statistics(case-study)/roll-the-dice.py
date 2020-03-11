"""
he following call generates the integer 4, 5, 6 or 7 randomly.
8 is not included.
    import numpy as np
    np.random.randint(4, 8)
"""
# Import numpy and set seed
import numpy as np
np.random.seed(123)

# Use randint() to simulate a dice
print(np.random.randint(1,7))

# Use randint() again
print(np.random.randint(1,7))