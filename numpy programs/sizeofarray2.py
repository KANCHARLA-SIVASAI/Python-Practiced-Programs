import numpy as np
import sys
# l=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,21,22,23,24,25,26,27,28,29,30,31,32,33,34,35,36,37,38,39,40,41,42,43,44,45,46,47,48,49,50,51,52,53,54]
l=[x for x in range(1,1000)]
Array=np.array(l)
print("memory space of list obj= {}, memory space of ndarray object= {}".format(sys.getsizeof(l),sys.getsizeof(Array)))
