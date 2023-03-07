class PairFinder:
    def find_pair(self, nums, target):
        num_index = {}
        
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in num_index:
                return num_index[diff]+1, i+1
            num_index[nums[i]] = i
        return None
pair_finder = PairFinder()
numbers = [10, 20, 10, 40, 50, 60, 70]
target = 50
pair = pair_finder.find_pair(numbers, target)
print(f'Output: {pair}')
    
