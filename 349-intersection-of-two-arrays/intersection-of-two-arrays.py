class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return self.sol1(nums1, nums2)

    def sol1(self, nums1, nums2):
        intersection_map = {}

        for n1 in nums1:
            intersection_map[n1] = False

        for n2 in nums2:
            if n2 in intersection_map:
                intersection_map[n2] = True

        return [k for k, v in intersection_map.items() if v == True]

    def sol2(self, nums1, nums2):
        set1 = set(nums1)
        set2 =  set(nums2)

        return list(set1 & set2)