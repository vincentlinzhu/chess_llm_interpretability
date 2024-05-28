import chess
import chess.svg
import chess.engine
import chess.pgn
import re

STOCKFISH_PATH = '/usr/games/stockfish'

def write_svg_to_file(filename, content):
    with open(filename, "w") as file:
        file.write(content)
        
def get_fen_after_moves(moves):
    scores = []
    board = chess.Board()  # Initialize a new chess board
    # Remove move numbers
    moves_cleaned = re.sub(r'\d+\.', '', moves)
    engine = chess.engine.SimpleEngine.popen_uci(STOCKFISH_PATH)
    for move in moves_cleaned.split():
        board.push_san(move)  # Apply each move to the board
        
        info = engine.analyse(board, chess.engine.Limit(time=0.3))  # Set time limit or depth for analysis
        cp_value = info['score'].white() if info['score'] else None
        if isinstance(cp_value, chess.engine.Cp):
            score = cp_value.score()
        scores.append(score)
        
    engine.quit()
        
    return board.fen()  # Return the FEN representation of the current board state

if __name__=="__main__":
    # # Moves provided, with move numbers
    # # san_moves = '1.e4 e5 2.Nf3 Nc6 3.d4 d6 4.d5 Nce7 5.c4 Nf6 6.Nc3 c6 7.Bg5 cxd5 8.cxd5 h6 9.Bxf6 gxf6 10.Bc4 b6 11.O-O Bb7 12.b3 Ng6 13.Re1 Nh4 14.Nxh4 Qc8 15.Nf5 Ba6 16.Ne3 Bg7 17.Nb5 Bxb5 18.Bxb5+ Kf8 19.Nf5 Qc5 20.Nxg7 Kxg7 21.Bc6 Rac8 22.Bd7 Rcd8 23.Bf5 a5 24.Rc1 Qa3 25.Re2 Rc8 26.Rxc8 Rxc8 27.Bxc8 Qc5 28.Bf5 b5 29.Rc2 Qb6 30.Rc6 Qd8 31.Ra6 h5 32.a4 bxa4 33.bxa4 Kh6 34.Qd2+ Kg7 35.Rxa5 Qb8 36.Ra6 Qb1+'
    # san_moves = '1.e4 b6 2.c4 Bb7 3.Nc3 Nf6 4.e5 Ne4 5.Qf3 Nc5 6.Qg3 Nc6 7.Nf3 Nb4 8.Kd1 Nbd3 9.Nd4 Nxc1 10.Rxc1 h5 11.Nf5 g6 12.Ne3 h4 13.Qf4 Bh6 14.Qd4 Ne6 15.Qg4 c5 16.Be2 Nd4 17.Bf3 Nxf3 18.gxf3 e6 19.f4 Bxh1 20.f3 h3 21.Ne4 Bg2 22.Nd6+ Kf8 23.Nxg2 hxg2 24.Qxg2 Bxf4 25.Qe2 Rxh2 26.Qe4 Rxd2+ 27.Ke1 Qh4+ 28.Kf1 Qh1#'
    # fen_output = get_fen_after_moves(san_moves)
    
    # # pgn = open('lichess_pgn_2024.05.18_Ryomen-Sukuna3004_vs_flo50.KdmbiVbu.pgn')
    # # game = chess.pgn.read_game(pgn)
    # # fen_output = get_fen_after_moves(san_moves)
            
    board = chess.Board("rnbqkbnr/pppp1ppp/8/4p3/4P3/5N2/PPPP1PPP/RNBQKB1R b KQkq - 1 2")
    print(board)
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
    # board_state_advantage_data = []
    # moves = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # desired_vectors = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
    # for move_idx, move in reversed(list(enumerate(moves[-15:]))):
    #     board_state_advantage_data.append(
    #         {
    #             "Move_Number": move_idx,
    #             "Model_Outputs": desired_vectors[move_idx], # Should be the corresponding vector (size 512) from the tensor
    #         }
    #     )
        
    # print(board_state_advantage_data)