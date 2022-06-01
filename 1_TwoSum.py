# My code
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remains = [target-x for x in nums]
        for index, element in enumerate(remains):
            nums.pop(0)
            search_the_other_index = [i for i, e in enumerate(nums) if e==element]
            if search_the_other_index:
                return [index, search_the_other_index[0]+index+1]


'''
LeetCode
class Solution:
   def twoSum(self, nums: List[int], target: int) -> List[int]:
       seen = {}
       for i, value in enumerate(nums):
           remaining = target - nums[i]
           
           if remaining in seen:
               return [i, seen[remaining]]
            
           seen[value] = i 

'''