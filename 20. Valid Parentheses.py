class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        dic = {')': '(', ']': '[', '}': '{'}

        # (()){}[]
        stack = [None]
        for c in s:
            if c in dic and dic[c] == stack[len(stack) - 1]:
                stack.pop()
            else:
                stack.append(c)

        if len(stack) == 1:
            return True
        return False