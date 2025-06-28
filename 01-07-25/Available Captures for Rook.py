
class Solution(object):
    def numRookCaptures(self, board):
        def findWhiteRook(board):
            for i in range(len(board)):
                for j in range(len(board[0])):
                    if board[i][j] == 'R':
                        return (i,j)
            return -1
        rr, rc = findWhiteRook(board)
        kills = 0
        for ic in range(rc-1,-1,-1):
            if board[rr][ic] == 'p':
                kills += 1
                break
            elif board[rr][ic] == 'B' or board[rr][ic] == 'P':
                break
        for ic in range(rc+1,len(board[0])):
            if board[rr][ic] == 'p':
                kills += 1
                break
            elif board[rr][ic] == 'B' or board[rr][ic] == 'P':
                break
        for ir in range(rr+1,len(board)):
            if board[ir][rc] == 'p':
                kills += 1
                break
            elif board[ir][rc] == 'B' or board[ir][rc] == 'P':
                break
    
        for ir in range(rr-1,-1,-1):
            if board[ir][rc] == 'p':
                kills += 1
                break
            elif board[ir][rc] == 'B' or board[ir][rc] == 'P':
                break
        return kills
                
        
