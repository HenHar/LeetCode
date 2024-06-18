class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:

        string_length = len(s1)
        substring = s2[0:string_length]
        s1_dict = {e:s1.count(e) for e in set(s1)}
        substring_dict = {e:substring.count(e) for e in set(substring)}


        for c in s2[string_length:]:
            substring_dict = {e:substring.count(e) for e in set(substring)}
            if s1_dict == substring_dict:
                return True
            substring = substring[1:] + c

        substring_dict = {e:substring.count(e) for e in set(substring)}
        return s1_dict == substring_dict
      