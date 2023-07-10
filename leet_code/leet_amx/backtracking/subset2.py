class Solution:
    def subsetsWithDup(self, nums):
        res = []
        sub = []
        nums.sort()
        def dfs(i):
            if i == len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            while i+1<=len(nums)-1 and nums[i] == nums[i+1]:
                i+=1
            dfs(i+1)
        dfs(0)
        return res

sol = Solution()
print(sol.subsetsWithDup([1,2,2]))