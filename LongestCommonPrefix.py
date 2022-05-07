class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        
        small = min(strs , key = len)
        size = len(small)

        difsize = len(strs) - len(set(strs)) 

        if difsize != 0:
            lsize = len(set(strs)) + (difsize)
        else:
            lsize = len(strs)

        prefix = []
        
        j = 0
        counter = 0

        for _ in range(len(small)):
            for item in strs:
                if small[_] == item[j]:
                    counter += 1
                    if (small[_] not in prefix and counter == lsize) or(counter == lsize):
                        if _ == j and (len(prefix) == j):
                            prefix.append(small[_])
                    
            j += 1
            counter = 0
            
        if len(prefix) != 0:
            return ''.join(prefix)
        else:
            return ""
        
        

Solution().longestCommonPrefix(["flower","flow","flight"])
