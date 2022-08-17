import chess
import chess.engine
import os
from fastapi import FastAPI
import stat
import sys

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
    
# engine = chess.engine.SimpleEngine.popen_uci(r"D:\internship\chess\chess-backend-engine-windows\stockfish_15_win_x64_avx2\stockfish_15_x64_avx2.exe")
# engine = chess.engine.SimpleEngine.popen_uci(r"D:\internship\chess\chess-engine-backend1\chess-backend-engine\stockfish_15_linux_x64\stockfish.exe")
# engine = chess.engine.SimpleEngine.popen_uci(r"/home/ubuntu/chess-backend-engine/stockfish_15_linux_x64/stockfish")


if __name__ == '__main__':
    dir = os.getcwd()
    print(dir)



@app.post("/bot/")
def hello(data : Data):
    print(data)

    if sys.platform == "linux":
        os.chmod("./stockfish_20011801_x64", stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
        engine = chess.engine.SimpleEngine.popen_uci("./stockfish_15_linux_x64/stockfish")
    else:
        engine = chess.engine.SimpleEngine.popen_uci("./stockfish_15_win_x64_avx2/stockfish_15_x64_avx2.exe")

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
    
