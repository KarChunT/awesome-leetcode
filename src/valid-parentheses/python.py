# Solution 1
class Solution:
    def isValid(self, s: str) -> bool:
        mapping= {
            ')': '(',
            '}': '{',
            ']': '['
        }
        stack = []
        for c in s:
            if c not in mapping:
                stack.append(c)
            else:
                if not stack or mapping[c] != stack.pop():
                    return False
        return stack == []


# Solution 2
class Solution:
    def isValid(self, s: str) -> bool:
        mapping= {
            '(': ')',
            '{': '}',
            '[': ']'
        }
        stack = []
        result = False
        for c in s:
            if c in mapping:
                stack.append(c)
            else:
                if not stack or mapping[stack.pop()] != c:
                    return False
        return stack == []
