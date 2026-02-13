class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        N = len(grid)
        count = [0] * N * N
        res = [0,0]
        for i in grid:
         for j in i:
                count[j-1] += 1
 
        for p in range(len(count)):
            if count[p] == 2:
                res[0] = p+1
            if count[p] == 0:
                res[1] = p+1
        
        return res          