class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        map = defaultdict(list)
        for string in strs:
            sortedStrings = ''.join(sorted(string))
            map[sortedStrings].append(string)
        return list(map.values())