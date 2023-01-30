class Solution:
    def minBitFlips(self, start: int, goal: int) -> int:
        s1, g1 = list(bin(start).replace('0b', '')), list(bin(goal).replace('0b', ''))
        c = 0
        
        while len(s1) != len(g1):
            if len(s1) < len(g1):
                s1.insert(0, '0')
            elif len(g1) < len(s1):
                g1.insert(0, '0')

        print(s1, g1)
        for i in range(len(s1)-1, -1, -1):
            if s1 == g1:
                return c
            else:
                if s1[i] != g1[i] and s1[i] == '0':
                    s1[i] = '1'
                    c = c + 1
                elif s1[i] != g1[i] and s1[i] == '1':
                    s1[i] = '0'
                    c = c + 1
        print(s1, g1)
        if s1 == g1:
            return c
        return -1