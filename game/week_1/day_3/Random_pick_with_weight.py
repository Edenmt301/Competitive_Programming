import bisect

class Solution(object):

    def __init__(self, w):
        """
        :type w: List[int]
        """
        self.weights = w
        self.prefix = []
        self.sumSoFar = 0
        for i in range(len(w)):
            self.sumSoFar += w[i]
            self.prefix.append(self.sumSoFar)


    def pickIndex(self):
        """
        :rtype: int
        """
        selected = random.randint(1, self.sumSoFar)
        return bisect.bisect_left(self.prefix, selected)

        
