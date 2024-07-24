def TwoSum(nums, target):
  prevMap = {}
  # this dictionary is used to store the previous elements(differnce) and their index
  for i, n in enumerate(nums):
    diff = target-n
    if diff in prevMap:
      return [prevMap[diff], i]
    prevMap[n] = i

# We can also solve this by using the for in for loop this gives the time complexity of n^2
def TwoSum(nums, target):
  for i in range(len(nums)-1):
    for j in range(i, len(nums)):
      if nums[i]+nums[j]==target:
        return [i,j]

#Driver Code
nums = [3,4,5,6]
target = 7
result = TwoSum(nums, target)
print(result)

#Problem Link : https://leetcode.com/problems/two-sum/description/
