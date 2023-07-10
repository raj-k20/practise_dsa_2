class Solution:
    def isValid(self, s: str) -> bool:
        pstack = []
        map = {"}":"{",']':'[',')':'('}
        for chr in s:
            if chr not in map:
                pstack.append(chr)
                continue
            if not pstack or pstack[-1] != map[chr]:
                return False
            pstack.pop()
        return True


sol = Solution()
print(sol.isValid("[{()}[]]"))