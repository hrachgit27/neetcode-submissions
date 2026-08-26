class Solution:
    def isValid(self, s: str) -> bool:
        
        keys = {
            "}": "{",
            "]": "[",
            ")": "("
        }

        stack = []

        for char in s:
            
            if char == "{" or char == "(" or char == "[":
                stack.append(char)
            
            if char == "}" or char == ")" or char == "]":
                if not stack:
                    return False
                top_item = stack[-1]
                if top_item != keys[char]:
                    return False
                else:
                    stack.pop()



        return len(stack) == 0
