class Solution:
    def twoSum(self, nums, target: int) :
        temp = {}
        for i, val in enumerate(nums):
            complement = target - val
            if complement in temp:
                return [temp[complement], i]
            temp[val] = i
        return None

sol = Solution()
print(sol.twoSum([1,2,21],3))
