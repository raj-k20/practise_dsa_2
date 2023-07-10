class Solution:
    def generateParenthesis(self, n: int) :
        stack = []
        res = []
        def gp_util(openN,closeN):
            if openN == closeN == n:
                res.append("".join(stack))
                return
            if openN < n:
                stack.append('(')
                gp_util(openN+1,closeN)
                stack.pop()
            if closeN < openN:
                stack.append(')')
                gp_util(openN,closeN+1)
                stack.pop()
        gp_util(0,0)
        return res

sol = Solution()
print(sol.generateParenthesis(3))
