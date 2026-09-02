class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        for num in nums:
            count[num] = 1 + count.get(num, 0)
        
        freq = []
        for num, cnt in count.items():
            freq.append([cnt, num])
        freq.sort()

        solution = []
        while len(solution) < k:
            solution.append(freq.pop()[1])
        return solution