class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l < r:

            Cur_sum = numbers[l] + numbers[r]

            if Cur_sum > target:
                r -= 1
            elif Cur_sum < target:
                l +=1
            else:
                return [l+1, r+1]        