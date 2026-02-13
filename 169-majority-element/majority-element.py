from typing import List
class Solution(object):
   def majorityElement(self, nums):
     freq = 0
     ans = 0
     n = len(nums)
     
     for i in range(n):
        
        if (freq ==0):
            ans = nums[i]
        
        if ans == nums[i]:
            freq +=1
        else:
            freq -=1       

     return ans