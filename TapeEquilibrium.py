def solution(A):
    # write your code in Python 3.6
    # get the array length for the iteration
    import math
    array_len = len(A)
    min_difference = 99999000
    left_sum = 0
    right_sum = sum(A)
    # iterate through the elements
    for i in range(array_len-1):
        # add each beginning element of right array into the left array sum
        left_sum += A[i]
        # subtract each beginning element from the right array sum
        right_sum -= A[i]
        # compute for the absolute difference of the left and right array sums
        absolute_diff = abs(left_sum - right_sum)
        # if difference is negative, negate
        if absolute_diff < min_difference:
                min_difference = absolute_diff
    # return the minimum difference
    return(min_difference)