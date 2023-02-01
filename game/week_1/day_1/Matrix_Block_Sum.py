class Solution(object):
    def matrixBlockSum(self, mat, k):
        """
        :type mat: List[List[int]]
        :type k: int
        :rtype: List[List[int]]
        """
        m, n = len(mat), len(mat[0])
        prefix_sum = []

        for j in range(m):
            inner = []
            for i in range(n):
                x,y,z = 0, 0, 0
                if i - 1 >= 0:
                    x = inner[i-1]
                if j - 1 >= 0:
                    y = prefix_sum[j-1][i]
                if j - 1 >= 0 and i - 1 >= 0:
                    z = prefix_sum[j-1][i-1]
                current  = x + y + mat[j][i] - z
                inner.append(current)
            prefix_sum.append(inner)
            
        new_array = []
        for j in range(m):
            inner = []
            for i in range(n):
                a, b, c, d = 0, 0, 0, 0
                min_x, min_y, max_x, max_y = j - k, i - k, j + k, i + k 
                while not(max_x < m and max_y < n ):
                    if not max_x < m:
                        max_x -= 1
                    else:
                        max_y -= 1
                d = prefix_sum[max_x][max_y]
                if min_x - 1 >= 0:
                    a = prefix_sum[min_x - 1][max_y]
                if min_y - 1 >= 0:
                    b = prefix_sum[max_x][min_y - 1]
                if min_x - 1 >= 0 and min_y - 1  >= 0:
                    c = prefix_sum[min_x - 1][min_y - 1]
                current  = d - a - b + c 
                inner.append(current)
            new_array.append(inner)
        return new_array
    
                    