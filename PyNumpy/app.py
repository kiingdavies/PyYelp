# Part 1
# run: pipenv install numpy
# import numpy as np
# call the array method on np & pass in an array [1,2,3]. Save in an array var
# print(array)
# if you print(type(array)) youd see its an instance of numpy array not normal array
# To create a multi-dimensional array go back up to np.array and change its value to: ([ [1,2,3], [4,5,6] ])
# run the code
# Also print(array.shape)

import numpy as np
array = np.array([ [1,2,3] , [4,5,6] ])
print(array)
print(type(array))
print(array.shape)

# Part 2
#import numpy as np
# run: np.zeros((3,4), dtype=int) save in array var (dtype is optional while (3,4) is the shape)
# print(array)
# You can also run: np.ones((3,4)), np.full((3,4), 5), np.random.random((3,4))
# You can access individual values by: print(array[0, 0]) , print(array > 0.2), print(array[array > 0.2])
# print(np.sum(array)), print(np.floor(array)), (you can use ceil, round etc)

import numpy as np
array = np.zeros((3,4), dtype=int)
print(array)

array1 = np.ones((3,4))
array2 = np.full((3,4), 5)
array3 = np.random.random((3,4))

print(array[0, 0])
print(array > 0.2) 
print(array[array > 0.2])

print(np.sum(array))
print(np.floor(array))


# Part 3 summation
import numpy as np
first = np.array([1,2,3])
second = np.array([4,5,6])
print(first + second) 
# (also - * / % can be used)