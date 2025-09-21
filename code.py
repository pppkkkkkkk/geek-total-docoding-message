#User function Template for python3
class Solution:
	def countWays(self, digits):
        
        n = len(digits)
        dp = {n:1}
        
        def dfs (i):
            nonlocal dp, digits
            if i in dp:
                return dp[i]
            if digits[i] == "0":
                return 0
            ans = dfs(i+1)
            if (i+1) < n and (digits[i] == "1" or (digits[i] == "2" and digits[i+1] in ("0123456"))):
                ans += dfs(i+2)
                
            dp[i] = ans
            return ans
            
		return dfs(0) 
		