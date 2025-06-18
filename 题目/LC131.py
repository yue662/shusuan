class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def is_palindrome(s):
            return s == s[::-1]

        def backtracking(start, path):
            if start == len(s):
                res.append(path)
                return
            for i in range(start, len(s)):
                if is_palindrome(s[start:i + 1]):
                    backtracking(i + 1, path + [s[start:i + 1]])

        res = []
        backtracking(0, [])
        return res