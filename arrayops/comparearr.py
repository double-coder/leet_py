class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s1, t1 = list(s), list(t)
        iter = 0
        while iter < len(s1):
            if s1[iter] == '#':
                if iter > 0:
                    del s1[iter - 1]
                    iter = iter - 1
                del s1[iter]
                iter = iter - 1
            iter = iter + 1
        j = 0
        while j < len(t1):
            if t1[j] == '#':
                if j > 0:
                    del t1[j - 1]
                    j = j - 1
                del t1[j]
                j = j - 1
            j = j + 1
        print(s1, t1)
        if s1 == t1:
            return True
        return False