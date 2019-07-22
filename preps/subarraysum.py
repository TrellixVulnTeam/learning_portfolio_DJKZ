'''A naive approach to this problem would be to loop through each number
and then loop again through the array looking for a pair that sums to S.
The running time for the below solution would be O(n2) because in the worst
case we are looping through the array twice to find a pair. '''

 """For example, if the array is [3, 5, 2, -4, 8, 11] and the sum is 7,
 your program should return [[11, -4], [2, 5]] because 11 + -4 = 7 and 2 + 5 = 7."""
# our two sum function which will return
# all pairs in the list that sum up to S
def twoSum(arr, S):

  sums = []

  # check each element in array
  for i in range(0, len(arr)):

    # check each other element in the array
    for j in range(i+1, len(arr)):

      # determine if these two elements sum to S
      if (arr[i] + arr[j] == S):
        sums.append([arr[i], arr[j]])

  # return all pairs of integers that sum to S
  return sums

print twoSum([3, 5, 2, -4, 8, 11], 7)



#OR


'''We can write a faster algorithm that will find pairs that sum to S in linear time.
The algorithm below makes use of hash tables which have a constant lookup time.
As we pass through each element in the array, we check to see if S minus the current
element exists in the hash table. We only need to loop through the array once, resulting
in a running time of O(n) since each lookup and insertion in a hash table is O(1).'''

"""If the array is: [4, 5, 1, 8] and the sum is 6 the algorithm would proceed with the steps below:

(1) The hash table is initially empty and the first element in the array is 4. We simply put 4 into the hash table.

(2) The next element is 5. We check to see if the sum minus the current element exists in the hash table. 6 - 5 = 1 does not exist in the hash table. So add 5 to the hash table.

(3) The next element is 1. We check to see if the sum minus the current element exists in the hash table. 6 - 1 = 5 does exist in the hash table so we found a pair!
"""

# our two sum function which will return
# all pairs in the list that sum up to S
def twoSum(arr, S):

  sums = []
  hashTable = {}

  # check each element in array
  for i in range(0, len(arr)):

    # calculate S minus current element
    sumMinusElement = S - arr[i]

    # check if this number exists in hash table
    # if so then we found a pair of numbers that sum to S
    if sumMinusElement in hashTable:
      sums.append([arr[i], sumMinusElement])

    # add the current number to the hash table
    hashTable[arr[i]] = arr[i]

  # return all pairs of integers that sum to S
  return sums

print twoSum([3, 5, 2, -4, 8, 11], 7)   
