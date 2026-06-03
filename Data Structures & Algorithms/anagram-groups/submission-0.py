class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}
        for word in strs:
            key = "".join(sorted(word))
            if key not in groups:
                groups[key] = [] # initialize the value as a empty list. If the key didn't occur yet, create one

            groups[key].append(word)

        return list(groups.values())



