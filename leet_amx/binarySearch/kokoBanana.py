class Solution:
    def minEatingSpeed(self, piles, h: int) -> int:
        maxP = max(piles)
        l = 1
        r= maxP
        res = r
        while l <r:
            sol = (l+r)//2
            loc_res = 0
            for pil in piles:
                loc_res+= pil//sol
            if loc_res <=h:
                res = max(res,sol)
                r = k-1
            else:
                l = k+1
        return res
