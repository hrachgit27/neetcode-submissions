class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        

        s_frequency = Counter(s)
        t_frequency = Counter(t)

        str1 = dict(s_frequency)
        str2 = dict(t_frequency)
        

        if str1 == str2:
            return True
        else:
            return False
