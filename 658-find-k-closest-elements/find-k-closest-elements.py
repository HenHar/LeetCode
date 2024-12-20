class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        start_index_min_subarray = 0
        current_difference = sum([abs(i - x) for i in arr[0:k]])
        min_difference = current_difference
        for i, num in enumerate(arr[k:]):
            current_difference += abs(num-x) - abs(arr[i]-x)
            if current_difference < min_difference:
                min_difference = current_difference
                start_index_min_subarray = i+1
                

        return arr[start_index_min_subarray:start_index_min_subarray+k]