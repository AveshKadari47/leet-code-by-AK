class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        result = []
        i = 0
        n = len(words)
        
        while i < n:
            # Determine how many words fit in the current line
            line_len = len(words[i])
            j = i + 1
            
            while j < n and line_len + 1 + len(words[j]) <= maxWidth:
                line_len += 1 + len(words[j])
                j += 1
            
            # Number of words in this line
            num_words = j - i
            line = ""
            
            # Case 1: Last line or single word → left justify
            if j == n or num_words == 1:
                for k in range(i, j):
                    line += words[k]
                    if k < j - 1:
                        line += " "
                
                # Fill remaining spaces
                line += " " * (maxWidth - len(line))
            
            else:
                # Case 2: Fully justify
                total_chars = sum(len(words[k]) for k in range(i, j))
                total_spaces = maxWidth - total_chars
                spaces_between = total_spaces // (num_words - 1)
                extra_spaces = total_spaces % (num_words - 1)
                
                for k in range(i, j - 1):
                    line += words[k]
                    # Add extra space to left slots
                    spaces = spaces_between + (1 if k - i < extra_spaces else 0)
                    line += " " * spaces
                
                line += words[j - 1]  # last word
            
            result.append(line)
            i = j
        
        return result