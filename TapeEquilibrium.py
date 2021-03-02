def solution(A):
    # write your code in Python 3.6
    import math 
    # get the array length for iteration
    array_len = len(A)
    # set the initial value of minimum difference variable
    min_difference = 99999000 # maximum value of N minus 1 (100,000 - 1) multiplied by the maximum element value (1,000)
    
    # initialize the sum of both parts
    left_sum = 0        # zero is the initial sum assigned to denote that the left array is empty initially
    right_sum = sum(A)  # sum of the entire array is set as the sum of right array which initially contains all the elements

    # iterate through the elements
    for i in range(array_len-1): # subtract 1 from the array length to let each array contain at least one element
        # add each beginning element of right array into the left array sum
        left_sum += A[i]
        # subtract each beginning element from the right array sum
        right_sum -= A[i]
        # compute for the absolute difference of the left and right array sums
        absolute_diff = abs(left_sum - right_sum)
        # if difference is less than the current minimum difference, assign the absolute difference as the new minumum difference
        if absolute_diff < min_difference:
                min_difference = absolute_diff
    # return the minimum difference
    return(min_difference)