class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        sol_dict = {}
        for i in nums:
            if i in sol_dict:
                sol_dict[i] +=1
            else:
                sol_dict[i] = 1
        
        buckets = [[] for _ in range(len(nums)+1)]

        for key,value in sol_dict.items() :
            buckets[value].append(key)
        
        sol = []
        for i in range(len(buckets)-1, 0,-1):
            if buckets[i] != []:
                for j in range(0,len(buckets[i])):
                    sol.append(buckets[i][j])
                    if len(sol) == k:
                        return sol

                



            
            
        