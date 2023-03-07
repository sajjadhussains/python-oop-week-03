class Subset:
    def generate_subsets(self, nums):
        subsets = [[]]
        for num in nums:
            for i in range(len(subsets)):
                subsets.append(subsets[i] + [num])
                # print(subsets,len(subsets))
        return subsets
subset_obj = Subset()
nums = [4, 5, 6]
subsets = subset_obj.generate_subsets(nums)
print(subsets)
