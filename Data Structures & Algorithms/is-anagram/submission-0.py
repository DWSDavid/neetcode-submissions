class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        count = {} #Hashmap in java

        for char in s:
            count[char] = count.get(char,0) + 1 #if get return the value, vice versa return 0.

        for ch in t:
            if ch not in count:
                return False
            count[ch] -= 1# the count of char reduce by 1
            
            if count[ch] < 0:
                return False

        return True

