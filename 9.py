class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x > 10 and x % 10 == 0):
            return False
        revertedNum: int = 0
        while (x > revertedNum):
            revertedNum = revertedNum * 10 + x % 10
            x //= 10
        return x == revertedNum or x == revertedNum // 10
