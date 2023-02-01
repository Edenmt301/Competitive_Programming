class Solution(object):
    def minimumRecolors(self, blocks, k):
        """
        :type blocks: str
        :type k: int
        :rtype: int
        """
        minimum = k

        left = 0
        right = k
        count = 0

        for i in range(k):
            count += 1 if blocks[i] =="W" else 0 
        minimum = min(minimum, count)

        while(right < len(blocks)):
            print(count)
            if blocks[left] == "W":
                count -= 1
            if blocks[right] == "W":
                count += 1
            left += 1
            right += 1
            minimum = min(minimum, count)

        return minimum
