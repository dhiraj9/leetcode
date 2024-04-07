class Solution:
    def minStartValue(self, nums: List[int]) -> int:
        j = 1
        while True:
            a = False
            s = j
            for i in nums:
                s += i 
                if s < 1:
                    j += 1
                    a = True
                    break
            if not a:
                return j
                
                    

