import numpy as np
import sys
l=[1,2,3,4]
Array=np.array(l)
print("memory space of list obj= {}, memory space of ndarray object= {}".format(sys.getsizeof(l),sys.getsizeof(Array)))
