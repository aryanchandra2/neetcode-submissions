class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        u,d = 0, len(matrix) - 1
        while u <= d:
            m = (u+d) // 2
            if target >= matrix[m][0] and target <= matrix[m][len(matrix[0]) - 1]:
                l,r = 0, len(matrix[0]) - 1
                while l <= r:
                    m2 = (l + r) // 2
                    if target > matrix[m][m2]:
                        l = m2 + 1
                    elif target < matrix[m][m2]:
                        r = m2 - 1
                    else:
                        return True
                return False
            elif target > matrix[m][0]:
                u = m + 1
            elif target < matrix[m][0]:
                d = m - 1
        return False
