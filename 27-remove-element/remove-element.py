class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        return self.sol2(nums, val)
        
    # two pointers
    def sol2(self, nums, val):
        i = 0
        k = len(nums)
        
        while (i < k):
            if nums[i] == val:
                if nums[k-1] != val:
                    nums[i] = nums[k-1]
                    nums[k-1] = val
                    i += 1
                k -= 1
            else:
                i += 1

        return k

    # list.remove() operation
    def sol1(self, nums, val):
        for index, num in enumerate(nums.copy()):
            if num == val:
                nums.remove(num)

        return len(nums)
        