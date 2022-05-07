class Solution:
    def romanToInt(self, S):

        raw = {'I' : 1, 'V' : 5, 'X' : 10, 'L' : 50, 'C' : 100, 'D' : 500, 'M' : 1000, 'IV':4,'IX':9,'XL':40,'XC':90,'CD':400,'CM':900}

        i = 0
        num = 0
        while i < len(S):
            if i+1<len(S) and S[i:i+2] in raw:
                num+=raw[S[i:i+2]]
                i+=2
            else:
            
                num+=raw[S[i]]
                i+=1
        return num
        

S = "III"
Solution().romanToInt(S)
