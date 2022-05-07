class Solution:
    def isValid(self, s: str) -> bool:
        
        items = []
        for item in s:
            items.append(item)
        
        if len(items) % 2 != 0:
            return False
        else:            
            current = []
            
            if items[0] == "}" or items[0] == "]" or items[0] == ")":
                
                return False                
            else:
                for i in items:
                    if i == "(" or i == "{" or i == "[":
                        current.append(i)
                    elif i == ")" or i == "}" or i == "]":
                        if len(current) > 0:
                            open = current[len(current) - 1] 
                            if (open == "(" and i == ")") or (open == "{" and i == "}") or (open == "[" and i == "]"):
                                    current.pop()
                            else:
                                return False
                        else:
                            return False
                if len(current) == 0:
                    return True
                else:
                    return False
Solution().isValid("()")
