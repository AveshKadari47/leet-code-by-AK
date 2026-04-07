class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        # Edge case
        if num1 == "0" or num2 == "0":
            return "0"
        
        m, n = len(num1), len(num2)
        result = [0] * (m + n)
        
        # Multiply from right to left
        for i in range(m - 1, -1, -1):
            for j in range(n - 1, -1, -1):
                mul = int(num1[i]) * int(num2[j])
                sum_ = mul + result[i + j + 1]
                
                result[i + j + 1] = sum_ % 10
                result[i + j] += sum_ // 10
        
        # Convert result list to string
        result_str = ''.join(map(str, result))
        
        # Remove leading zeros
        return result_str.lstrip('0')