class Solution:
    def productExceptSelf(self, nums) :
        n= len(nums)
        l_prod = [0]*n
        r_prod = [0]*n

        l_prod[0] = 1
        for i in range(1,n):
            l_prod[i] = l_prod[i-1]*nums[i-1]

        r_prod[n-1] = 1
        for i in range(n-2, -1, -1):
            r_prod[i] = r_prod[i + 1] * nums[i + 1]

        result = []
        for i in range(n):
            result.append(l_prod[i]*r_prod[i])
        return result

sol = Solution()
print(sol.productExceptSelf([1,2,3]))

