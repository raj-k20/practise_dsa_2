class Solution:
    def checkCharcter(self,c):
        return (ord('a') <= ord(c) <= ord('z') ) \
               or (ord('0') <= ord(c) <= ord('9') ) \
               or (ord("A") <= ord(c) <= ord("Z"))

    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = len(s)
        i = 0
        j = n-1
        while i < j:
            while i < j and not self.checkCharcter(s[i]):
                i+=1
            while i < j and not self.checkCharcter(s[j]):
                j-=1
            if s[i].lower() != s[j].lower():
                return False
            i+=1
            j-=1
        return True

sol = Solution()
print(sol.isPalindrome("adda,abba,adda"))
