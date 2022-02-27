import timeit
import numpy as np
from timeit import Timer
from methods import binary_search,binary_search_updated, binary_search_updated2,findSmallest_1,findSmallest_2


""" binary_search(100,70,.95)
binary_search_updated(100,70,.95)
findSmallest_1(100,70,.95)
findSmallest_2(100,70,.95) """


# importing the module
import timeit
  

# using the timeit method and lambda
# expression to get the execution time of
# the function, number defines how many
# times we execute this function
input_array =[[100,70,.95],[1000,800,.80],[50,40,.80]]
binary_search_time=[]

for i in range (len(input_array)):
    print("inside loop")
    binary_search_time.append(timeit.timeit(lambda:binary_search_updated2(input_array[i][0],input_array[i][1],input_array[i][2]), number=1))
    print(binary_search_time)#binary_search_time = timeit.timeit(lambda:binary_search(100,70,.95), number=100)
    
# printing the execution time
print(binary_search_time)
