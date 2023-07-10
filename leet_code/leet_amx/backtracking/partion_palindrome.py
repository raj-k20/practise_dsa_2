class Solution:
    def partition(self, s: str):
        res= []
        part = []
        def dfs(i):
            if i >=len(s):
                res.append(part.copy())
                return
            for j in range(i,len(s)):
                if self.check_palindrome(s,i,j):
                    part.append(s[i:j+1])
                    dfs(j+1)
                    part.pop()
        dfs(0)
        return res

    def check_palindrome(self,s,i,j):
        while i < j:
            if s[i] != s[j]:
                return False
            i,j = i+1,j-1
        return True

sol = Solution()
print(sol.partition("abb"))