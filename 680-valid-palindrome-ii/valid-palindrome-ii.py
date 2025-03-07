class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s)-1

        while l < r:
            if s[l] != s[r]:
                if self.isPalindrome(s[l:r]) or self.isPalindrome(s[l+1:r+1]):
                    return True
                else:
                    return False
            l += 1
            r -= 1

        return True

    def isPalindrome(self, s):
        l, r = 0, len(s)-1
        while l < r:
            if s[l] != s[r]:
              return False
            l += 1
            r -= 1

        return True