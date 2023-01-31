class Solution:
    def reverseWords(self, s: str) -> str:
        l = list(s)
        s = 0
        for i in range(len(l)):
            if l[i] == ' ':
                self.swap(l, s, i - 1)
                s = i + 1
        self.swap(l, s, len(l) - 1)
        return ''.join(l)

    def swap(self, s: list[str], l: int, r: int) -> None:
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1