import chess
import chess.engine
import os
from fastapi import FastAPI

from pydantic import BaseModel

app = FastAPI()

class Data(BaseModel):
    fen: str
    depth: int
    class Config:
        orm_mode = True

engine = ''

if __name__ == '__main__':
    dir = os.getcwd()
    print(dir)

engine = chess.engine.SimpleEngine.popen_uci(r"/home/ubuntu/chess-backend-engine2/stockfish_15_linux_x64/stockfish")


@app.post("/bot/")
def hello(data : Data):
    print(data)
    try:
        board = chess.Board(data.fen)
    except Exception as e:
        return (str(e))
    if not board.is_game_over():
        
        result = engine.play(board, chess.engine.Limit(time=0.1,depth = data.depth))
        move = result.move
        board.push(result.move)
        return {"fen":board,"move":str(move)}
        
    else:
        return {"error":"Game is in Over State"}

@app.get("/")
def hello2():
    return {"Data":"Success"}
    
