import numpy as np
import sys
l=[x for x in range(1,10)]
Array=np.array(l)
print("Before",Array)
Array=Array+5
print("After adding",Array)
Array=Array-5
print("After sub",Array)
Array=Array*5
print("After mul",Array)
Array=Array/2
print("After division",Array)
Array=Array//2
print("After floor division",Array)