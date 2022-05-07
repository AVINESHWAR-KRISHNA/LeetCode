class Solution:
    def isPalindrome(self, x: int) -> bool:
        num = []        
        
        
        for _ in str(x):
            num.append(_)

        rev_num = num.copy()
        rev_num.reverse()

        if ''.join(rev_num) == ''.join(num) :
            return True
        else:
            return False
        
Solution().isPalindrome(121)
