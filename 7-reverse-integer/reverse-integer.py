class Solution:
    def reverse(self, x: int) -> int:
        num = x
        sign=-1 if x<0 else 1
        num=abs(num)
        
        result=0
        while num>0:
            id=num%10
            result=(result*10)+id
            num=num//10
        result= sign*result
        if result <-2**31 or result >2**31 -1:
            return 0
        return result    