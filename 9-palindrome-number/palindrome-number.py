class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        # Negative numbers are not palindrome
        if x < 0:
            return False
        
        # Convert number to string and check reverse
        return str(x) == str(x)[::-1]