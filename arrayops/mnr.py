from collections import defaultdict

class Solution:
    def maxnr(self, n: int, roads: list[list[int]]) -> int:
        dic = defaultdict(set)

        for i, j in roads:
            dic[i].add(i)
            dic[j].add(j)

        t = 0
        for i in range(n):
            for j in range(i+1, n):
                t = max(t, len(dic[i]) + len(dic[j]) - (i in dic[j]))
    
        return t