class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for str in strs:
            temp = sorted(str)
            key = "".join(temp)
            if groups.get(key):
                groups[key].append(str)
            else:
                groups[key] = [str]

        result = []
        for arr in groups.values():
            result.append(arr)

        return result