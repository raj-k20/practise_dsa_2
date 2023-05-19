class Solution:
    def containsDuplicate(self, nums) -> bool:
        temp = {}
        for val in nums:
            temp[val] = temp.get(val,0)+1
            if temp[val] >1:
                return True

        return False


sol = Solution()
print(sol.containsDuplicate([1,2,221]))