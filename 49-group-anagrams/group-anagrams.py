from collections import defaultdict 

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anaDict = defaultdict(list)

        for s in strs:
            anaDict[tuple(sorted(s))].append(s)

        return list(anaDict.values())