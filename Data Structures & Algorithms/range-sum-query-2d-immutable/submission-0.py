class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        self.matrix = matrix

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        ans = 0
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                if row1 <= i <= row2 and col1 <= j <= col2:
                    ans += self.matrix[i][j]
        return ans




# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)