class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        new_matrix=[]
        for i in range(len(matrix[0])):
            arr = []
            for j in range(len(matrix)):
                arr.append(matrix[j][i])
            new_matrix.append(arr)
        return new_matrix