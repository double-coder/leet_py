class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        if len(s) == 1 and s == '1':
            return True
        for i in range(len(s)-1):
            if s[i] == s[i+1] == '1':
                return True
        print(len(s))
        return False