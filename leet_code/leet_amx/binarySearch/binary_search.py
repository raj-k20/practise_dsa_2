class Solution:
    def search(self, nums, target: int) -> int:
        n = len(nums)
        i = 0
        k = n-1
        while i<=k:
            mid = i+((k-1)//2)
            if nums[mid]<target:
                i= mid+1
            elif nums[mid]>target:
                k=mid-1
            else:
                return mid


sol = Solution()
print(sol.search([1,2,3,4],1))
