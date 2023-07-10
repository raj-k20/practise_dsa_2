class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        temp = {}
        if len(s) != len(t):
            return False
        for char in s:
            temp[char] = temp.get(char,0)+1

        for char in t:
            if char not in temp or temp[char] == 0:
                return False
            temp[char] = temp.get(char,0)-1

        return True

sol = Solution()
print(sol.isAnagram("abb","bab"))