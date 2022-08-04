import chess

class ChessGame:

    def __init__(self):
        self.board = chess.Board()
        self.whiteToMove = True
        self.gameIsOn = True
        self.checkmate = False
        self.stalemate = False

    def makeMove(self, move):
        if move in self.board.legal_moves:
            self.board.push(chess.Move.from_uci(str(move)))
            self.whiteToMove = not self.whiteToMove
            return self.board

    def isGameOver(self):
        if self.checkmate or self.stalemate:
            self.gameIsOn = False
            return True
    
    def getBoard(self):
        return self.board

    def boardToList(self):
        s = str(self.board)
        boardList = []
        x = []
        for i in range(len(s)):
            if s[i] != " " and s[i] != "\n":
                x.append(s[i])
            if s[i] == "\n":
                boardList.append(x)
                x = []
            if i == len(s) - 1:
                boardList.append(x)
        return boardList
    
class Move():
    def __init__(self, startsq, endsq, board):
        self.startRow = startsq[0]
        self.startCol = startsq[1]
        self.endRow = endsq[0]
        self.endCol = endsq[1]
        self.pieceMoved = board[self.startRow][self.startCol]
        self.pieceCaptured = board[self.endRow][self.endCol]