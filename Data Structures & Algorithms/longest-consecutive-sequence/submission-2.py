class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numberSet = set(nums)
        longest = 0

        for num in numberSet:
            if (num - 1) not in numberSet:
                length = 1
                while (num + length) in numberSet:
                    length += 1
                longest = max(length, longest)
        return longest