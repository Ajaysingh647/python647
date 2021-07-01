# to create a matrix using shortform or numpy module.

import numpy as np
mat1= np.arange(12).reshape(3,4)
mat2=np.arange(12).reshape(4,3)
res=np.multiply(mat1,mat2)
print('the multiply of the mat1 and mat2',res)