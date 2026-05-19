class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        nums_set = set(nums)
        longest_consecutive = 0
        longest_consecutive = [1]
        print(nums_set)
        nums_set = sorted(nums_set)
        for num in nums_set:
            print(num)
            if num-1 in nums_set:
                longest_consecutive[len(longest_consecutive) - 1] +=1
            else:
                longest_consecutive.append(1)
        print(longest_consecutive)
        return max(longest_consecutive)



