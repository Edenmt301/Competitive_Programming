class Solution(object):
    def earliestFullBloom(self, plantTime, growTime):
        """
        :type plantTime: List[int]
        :type growTime: List[int]
        :rtype: int
        """
        elements = []
        for i in range(len(plantTime)):
            elements.append([growTime[i], plantTime[i]])
        elements.sort(key=lambda x:-x[0])
        
        maxtime = 0
        currenttime = 0
        for element in elements:
            currenttime += element[1]
            maxtime = max(maxtime, currenttime + element[0])
        return maxtime