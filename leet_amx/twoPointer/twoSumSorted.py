class Solution:
    def twoSum(self, numbers, target) :
        n= len(numbers)
        i=0
        j = n-1

        while i < j:
            cursum = numbers[i] + numbers[j]
            if cursum > target:
                j-= 1
            elif cursum < target:
                i += 1
            else:
                return [i+1,j+1]

        return [j,j]


sol = Solution()
print(sol.twoSum([2,7,12,13],9))
