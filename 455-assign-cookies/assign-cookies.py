class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g = sorted(g)
        s = sorted(s)

        children_index = 0
        cookie_index = 0
        while children_index < len(g) and cookie_index < len(s):
            if g[children_index] <= s[cookie_index]:
                children_index += 1
            cookie_index += 1

        return children_index