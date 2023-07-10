class Solution:
    def searchMatrix(self, matrix, target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        top=0
        bot = rows-1
        while top <= bot:
            mid = (bot+top)//2
            if matrix[mid][-1] < target:
                top = mid + 1
            elif matrix[mid][0] > target:
                bot = mid - 1
            else:
                break

        if not (top <= bot):
            return False
        row = (top + bot) // 2

        left = 0
        right = columns-1
        while left <= right:
            mid = (right+left)//2
            if matrix[row][mid] < target:
                left = mid + 1
            elif matrix[row][mid] >target:
                right = mid-1
            else:
                return True
        return False


sol = Solution()
print(sol.searchMatrix([[1,3,5,7],[10,11,16,20],[23,30,34,60]],3))

