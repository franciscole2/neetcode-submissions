class Solution:

    def encode(self, strs: List[str]) -> str:
        if not strs:
            return ""
        sizes = []
        sol = []
        for s in strs:
            sizes.append(len(s))
        for sz in sizes:
            sol.append(str(sz))
            sol.append(',')
        sol.append('#')
        sol.extend(strs)
        return ''.join(sol)

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        sizes = []
        sol = []
        i = 0
        while s[i] != '#':
            j = i
            while s[j] != ',':
                j += 1
            sizes.append(int(s[i:j]))
            i = j + 1
        i += 1
        for sz in sizes:
            sol.append(s[i: i + sz])
            i += sz
        return sol
