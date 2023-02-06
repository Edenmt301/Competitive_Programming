import heapq
class Solution(object):
    def longestStrChain(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        heap = []
        words_dict = defaultdict(list)
        for word in words:
            heapq.heappush(heap, [len(word), word])
        
        all_words = {} 
        while heap:
            length, popped = heapq.heappop(heap)
            current = 1
            for i in range(len(popped)):
                new = popped[:i] + popped[i+1:] 
                if new in all_words:
                    current = max(current, all_words[new] + 1)
            all_words[popped] = current

        return max(all_words.values())