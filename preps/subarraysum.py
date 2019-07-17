# METHOD 1
# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum'
# otherwise returns
# false. Also, prints
# the result
def subArraySum(arr, n, sum):

    # Pick a starting
    # point
    for i in range(n):
        curr_sum = arr[i]

        # try all subarrays
        # starting with 'i'
        j = i+1
        while j <= n:

            if curr_sum == sum:
                print ("Sum found in the sub subarray")
                print(arr[i:j])

                return 1

            if curr_sum > sum or j == n:
                break

            curr_sum = curr_sum + arr[j]
            j += 1

    print ("No subarray found")
    return 0

# METHOD 2
# Returns true if the
# there is a subarray
# of arr[] with sum
# equal to 'sum'
# otherwise returns
# false. Also, prints
# the result.
def subArraySum_(arr, n, sum): 

    # Initialize curr_sum as
    # value of first element
    # and starting point as 0
    curr_sum = arr[0]
    start = 0

    # Add elements one by
    # one to curr_sum and
    # if the curr_sum exceeds
    # the sum, then remove
    # starting element
    i = 1
    while i <= n:

        # If curr_sum exceeds
        # the sum, then remove
        # the starting elements
        while curr_sum > sum and start < i-1:

            curr_sum = curr_sum - arr[start]
            start += 1

        # If curr_sum becomes
        # equal to sum, then
        # return true
        if curr_sum == sum:
            print ("Sum found between indexes")
            print ("%d and %d"%(start, i-1))
            return 1

        # Add this element
        # to curr_sum
        if i < n:
            curr_sum = curr_sum + arr[i]
        i += 1

    # If we reach here,
    # then no subarray
    print ("No subarray found")
    return 0

# Driver program
arr = [15, 2, 4, 8, 9, 5, 10, 23]
n = len(arr)
sum = 23

subArraySum(arr, n, sum)
