class Solution(object):
    def myAtoi(self, s):
        """
        :type s: str
        :rtype: int
        """
        s = s.lstrip()  # remove leading spaces
        if not s:
            return 0
        
        sign = 1
        i = 0
        result = 0
        
        # Check sign
        if s[i] == '+':
            i += 1
        elif s[i] == '-':
            sign = -1
            i += 1
        
        # Convert digits
        while i < len(s) and s[i].isdigit():
            result = result * 10 + int(s[i])
            i += 1
        
        result *= sign
        
        # Clamp to 32-bit signed integer range
        INT_MIN = -2**31
        INT_MAX = 2**31 - 1
        
        if result < INT_MIN:
            return INT_MIN
        if result > INT_MAX:
            return INT_MAX
        
        return result