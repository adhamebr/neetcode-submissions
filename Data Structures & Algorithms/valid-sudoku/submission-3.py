class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #print(len(board[0]) , len(board[1]))
        check_duplicates = {}
        #check squares
        for i in range(0,len(board[0])-1,3):
            
            for j in range(0,len(board[1])-1,3):
                check_duplicates = {}
                for k in range(0,3):
                    for m in range(0,3):
                        if board[i+k][j+m] == '.':
                            continue
                        if board[i+k][j+m] in check_duplicates:
                            return False
                        else :
                            check_duplicates[board[i+k][j+m]] = 1
        
                  
        for i in range(0,len(board[0])):
            check_duplicates = {}
            for k in range(0,len(board[1])):
                if board[i][k] == '.':
                            continue
                if board[i][k] in check_duplicates:
                    return False
                else :
                    check_duplicates[board[i][k]] = 1
           
            check_duplicates = {}
            for k in range(0,len(board[1])):
                if board[k][i] == '.':
                            continue
                if board[k][i] in check_duplicates:
                    return False
                else :
                    check_duplicates[board[k][i]] = 1
                
        return True