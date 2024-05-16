import chess
import chess.svg
import re

def write_svg_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
        
def get_fen_after_moves(moves):
    board = chess.Board()  # Initialize a new chess board
    # Remove move numbers
    moves_cleaned = re.sub(r'\d+\.', '', moves)
    for move in moves_cleaned.split():
        board.push_san(move)  # Apply each move to the board
    return board.fen()  # Return the FEN representation of the current board state

if __name__=="__main__":

    # Moves provided, with move numbers
    san_moves = "1.e4 c6 2.Nf3 d5 3.d3 dxe4 4.dxe4 Qxd1+ 5.Kxd1 Bg4"
    fen_output = get_fen_after_moves(san_moves)
            
    board = chess.Board(fen_output)
    board_render = chess.svg.board(
        board,
        # fill=dict.fromkeys(board.attacks(chess.E4), "#cc0000cc"),
        # arrows=[chess.svg.Arrow(chess.E4, chess.F6, color="#0000cccc")],
        # squares=chess.SquareSet(chess.BB_DARK_SQUARES & chess.BB_FILE_B),
        size=350,
    )

    write_svg_to_file(
        "sample_svg_board.svg",
        board_render,
    )