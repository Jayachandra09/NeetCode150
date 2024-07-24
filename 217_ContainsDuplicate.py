def Duplicate(nums):
  dect = {}
  for i, n in enumerate(nums):
    if n in dect:
      return True
    dect[n] = i
  return False

#Driver Code
nums = [1, 2, 3, 3]
result = Duplicate(nums)
print(result)

#Problem Link : https://leetcode.com/problems/contains-duplicate/description/
