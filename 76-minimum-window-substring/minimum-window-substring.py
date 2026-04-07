from collections import Counter

class Solution(object):
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """
        if not s or not t:
            return ""
        
        need = Counter(t)
        missing = len(t)
        
        left = start = end = 0
        
        for right in range(len(s)):
            if need[s[right]] > 0:
                missing -= 1
            need[s[right]] -= 1
            
            # When all characters are matched
            while missing == 0:
                # Update result window
                if end == 0 or right - left + 1 < end - start:
                    start, end = left, right + 1
                
                # Shrink window
                need[s[left]] += 1
                if need[s[left]] > 0:
                    missing += 1
                left += 1
        
        return s[start:end]