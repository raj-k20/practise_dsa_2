class Solution:
    def combinationSum2(self, candidates, target):
        candidates.sort()
        res = []
        def dfs(cur,pos,target):
            if target == 0:
                res.append(cur.copy())
                return
            if target<=0:
                return
            prev=-1
            for i in range(pos,len(candidates)):
                if candidates[i] == prev:
                    continue
                cur.append(candidates[i])
                dfs(cur,i+1,target-candidates[i])
                cur.pop()
                prev = candidates[i]
        dfs([],0,target)
        return res
sol= Solution()
nums = [10,1,1,2,6,7,9]
print(sol.combinationSum2(nums,8))