class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        cols = defaultdict(set) # key is col index
        rows = defaultdict(set) # key is row index
        grid = defaultdict(set) # key is square index as a tuple (i//3, j//3)

        for i in range(len(board)):
            
            for j in range(len(board[i])):
                if board[i][j] == '.':
                    continue

                if board[i][j] in rows[i]:
                    return False  
                if board[i][j] in cols[j]:
                    return False 
                if board[i][j] in grid[(i//3, j//3)]:
                    return False
                
                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                grid[(i//3, j//3)].add(board[i][j])
        return True
        
