import heapq


class Solution:
    def topKFrequent(self, nums, k: int):
        temp = {}
        result = []
        for val in nums:
            temp[val] = temp.get(val,0) + 1
        max_vals = list(temp.values())
        max_vals.sort(reverse=True)
        for key in temp:
            if temp[key] in max_vals[:k]:
                result.append(key)

        return result

    def topKFrequent_heap(self, nums, k: int):
        temp = {}
        heap = []
        for val in nums:
            temp[val] = temp.get(val, 0) + 1
        for key,value in temp.items():
            heapq.heappush(heap,(-value,key))
        result = []
        for _ in range(k):
            result.append(heapq.heappop(heap)[1])
        return result



sol = Solution()
print(sol.topKFrequent_heap([1,1,2,2,2,21],2))

