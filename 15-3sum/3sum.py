class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        triplets = set()
        nums = sorted(nums)
        seen = []
        for i in range(len(nums)):
            target = nums[i]
            l, r = i + 1, len(nums) - 1
            if target in seen:
                continue
            elif target > 0:
                break
            else:
                seen.append(target)
                while l < r:
                    if nums[l] + nums[r] == -target:
                        triplet = tuple(sorted((nums[i], nums[l], nums[r])))
                        triplets.add(triplet)
                    if nums[i] + nums[l] + nums[r] < 0:
                        l += 1
                    else:
                        r -= 1
        
        return list(list(x) for x in triplets)