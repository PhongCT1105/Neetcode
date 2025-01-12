class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        bracket = {
            '(': ')',
            '{': '}',
            '[': ']'
        }    

        for c in s:
            if c in bracket:
                stack.append(c)
            
            elif c in bracket.values():
                if stack and c == bracket[stack[-1]]:
                    stack.pop() 
                else:
                    return False

            else:
                return False
        
        if stack == []:
            return True
        else:
            return False   
