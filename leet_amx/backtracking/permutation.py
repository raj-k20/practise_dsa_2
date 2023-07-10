class Solution:
    def permute(self, nums):
        res = []
        sub = []

        def dfs(i):
            if i==len(nums):
                res.append(sub.copy())
                return
            sub.append(nums[i])
            dfs(i+1)
            sub.pop()
            dfs(i+1)
        dfs(0)
        return res

nums = [1,2,3]
sol = Solution()
print(sol.permute(nums))