class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        dict = {}
        for i in arr:
            if i in dict:
                dict[i] += 1
            else:
                dict[i] = 1
        occurence = []
        for x in dict:
            if dict[x] in occurence:
                return False
            else:
                occurence.append(dict[x])
                
        return True
