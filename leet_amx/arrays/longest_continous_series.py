class Solution:
    def longestConsecutive(self, nums) -> int:
        ln = 0
        numset = set(nums)
        for n in nums:
            if (n-1) not in numset: # find first element of the series
                length=1
                while (n+length) in numset:
                    length+=1
                ln = max(length, ln)
        return ln

nums = [100,4,200,1,3,2]
sol = Solution()
print(sol.longestConsecutive(nums))


