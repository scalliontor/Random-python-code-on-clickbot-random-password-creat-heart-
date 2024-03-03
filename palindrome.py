class Solution:
    def isPalindrome(self, n: int) -> bool:
        temp = n
        rev= 0 
        while n>0:
            dev = n%10
            rev = rev *10 + dev
            n = n //10
        if rev == temp:
            return True
        else:
            return False
            