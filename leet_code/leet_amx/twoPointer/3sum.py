class Solution:
    def threeSum(self, nums):
        n = len(nums)
        nums.sort()
        result = []
        for indx in range(n - 1):
            if nums[indx] > 0:
                break
            if indx > 0 and nums[indx] == nums[indx - 1]:
                continue
            i = indx + 1
            j = n - 1
            while i < j:
                if nums[i] + nums[j] > 0 - nums[indx]:
                    j -= 1
                elif nums[i] + nums[j] < 0 - nums[indx]:
                    i += 1
                else:
                    result.append([nums[indx], nums[i], nums[j]])
                    i += 1
                    j -= 1
                    while nums[i] == nums[i - 1] and i < j:
                        i += 1

        return result


sol = Solution()
print(sol.threeSum([0,0,0]))


