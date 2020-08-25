import matplotlib.pyplot as plt
import numpy as np

sprmatrix = np.loadtxt('Ti_Ref-00001.spr', skiprows=1)
a = plt.imshow(sprmatrix)
print(type(a))
plt.show()