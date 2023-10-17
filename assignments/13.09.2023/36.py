class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        matrix = []
        for i in range(9):
            for j in range(9):
                element = board[i][j]
                if element !=".":
                    matrix += [(i,element),(element,j),(i//3,j//3,element)]
        return len(matrix)==len(set(matrix))