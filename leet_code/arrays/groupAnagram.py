class Solution:
    def groupAnagrams(self, strs):
        temp = {}

        for word in strs:
            chrs = [0]*26

            for chr in word:
                chrs[ord(chr)-ord('a')] += 1
            key = tuple(chr)
            temp.setdefault(key, []).append(word)
        return list(temp.values())


sol = Solution()
print(sol.groupAnagrams(["ddddddddddg","dgggggggggg"]))
