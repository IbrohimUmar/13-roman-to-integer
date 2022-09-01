class Solution:
    def romanToInt(self, s: str) -> int:
        se = {
            "R": 0,
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        res = 0
        s += 'R'
        i = 0
        while i < len(s) - 1:
            if se[s[i]] < se[s[i + 1]]:
                res += se[s[i + 1]] - se[s[i]]
                i += 2
            else:
                res += se[s[i]]
                i += 1

        return res
