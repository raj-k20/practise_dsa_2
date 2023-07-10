class Solution:
    def trap(self, height) -> int:
        l,r = 0,len(height)-1
        res = 0
        leftm, rightm = height[l],height[r]
        while l < r :
            if leftm < rightm:
                l+=1
                leftm = max(leftm,height[l])
                res+= leftm-height[l]
            else:
                r-=1
                rightm= max(rightm,height[r])
                res+=rightm-height[r]

        return res

height=[0,1,0,2,1,0,1,3,2,1,2,1]
sol = Solution()
print(sol.trap(height))