class Solution:
    def dailyTemperatures(self, temperatures) :
        hot_days = []
        res = [0]*len(temperatures)
        for i,t in enumerate(temperatures):
            while hot_days and t > hot_days[-1][1]:
                stackind, stacktemp = hot_days.pop()
                res[stackind] = i-stackind
            hot_days.append((i,t))
        return res


sol = Solution()
print(sol.dailyTemperatures([73,74,75,71,69,72,76,73]))
