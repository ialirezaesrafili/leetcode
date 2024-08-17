class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Dictionary to hold the mapping of closing and opening brackets
        bracket_map = {')': '(', '}': '{', ']': '['}
        stack = []

        for char in s:
            # If the character is a closing bracket
            if char in bracket_map:
                # Pop the top element if the stack is not empty, else assign a dummy value
                top_element = stack.pop() if stack else '#'

                # If the mapping for the current bracket doesn't match the stack's top element, return false
                if bracket_map[char] != top_element:
                    return False
            else:
                # It's an opening bracket, push it onto the stack
                stack.append(char)

        # If the stack is empty, all opening brackets were properly closed
        return not stack
