import numpy as np
import pandas as pd
s = pd.Series(np.random.rand(5), index=['a','b','c','d','e'])

print(s)
print(s.index)

s1 = pd.Series(np.random.rand(5))
print(s1)

d = {'b':1, 'a': 0, 'c': 2}
s2 = pd.Series(d)
print(s2)

s3 = pd.Series(d, index = ['b', 'c', 'd', 'a'])
print(s3)