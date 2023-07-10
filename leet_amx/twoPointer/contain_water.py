class Solution:
    def maxArea(self, height) -> int:
        h = max(height)
        i=0
        j=len(height) -1
        res = 0
        while i < j:
            res = max(res,min(height[i],height[j])*(j-i))
            if height[i] < height[j]:
                i+=1
            elif height[j]<=height[i]:
                j-=1
            if (j-i)*h <= res:
                break
        return res

a=[1,8,6,2,5,4,8,3,7]

sol = Solution()
print(sol.maxArea(a))
