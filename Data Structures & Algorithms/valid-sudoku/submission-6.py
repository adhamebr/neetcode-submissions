class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        #print(len(board[0]) , len(board[1]))
        check_duplicates = {}
        rows=[0] *9
        cols = [0]*9
        boxes = [0] *9
        #check squares
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.':
                    continue
                num = int(board[i][j]  )

                bits = 1<<(num-1)

                box = (i//3)*3 + (j//3)
                if rows[i] & bits:
                    return False
                if cols[j] & bits:
                    return False
                if boxes[box] & bits:
                    return False
                
                rows[i] = rows[i] | bits
                cols[j] = cols[j] | bits
                boxes[box] = boxes[box] | bits


        return True