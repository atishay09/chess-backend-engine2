import chess
import chess.engine
import os
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    fen: str
    depth: int

dir = os.getcwd()
print(dir)
engine = chess.engine.SimpleEngine.popen_uci("/app/stockfish_15_linux_x64/stockfish")

while not board.is_game_over():
    board.push_san(input("\nEnter your move : \n"))
    print(board)
    print("\n\n\nBot : \n")
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)
    print(board)
if board.is_game_over():
    print("Game Over")


@app.post("/bot/")
def hello(data : Data):
    board = chess.Board(data.fen)
    if not board.is_game_over():
        result = engine.play(board, chess.engine.Limit(time=0.1,depth = data.depth))
        board.push(result.move)
        return {"fen":board,"move":result.move}
    else:
        return {"error":"Game is in Over State"}

@app.get("/")
def hello2():
    return {"Data":"Success"}
    