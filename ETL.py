import re
import pandas as pd

file = open(r"/Users/jon/PycharmProjects/Chess/test_game.txt")
lines = file.readlines()
count = 0
for line in lines:
    print(f"{count } {line}")
    count +=1
file.close()

test_game ="""
[Event "Rated Bullet game"]
[Site "https://lichess.org/yd5d4l9a"]
[White "claudiomat"]
[Black "MisterBiggStuff"]
[Result "0-1"]
[UTCDate "2013.12.31"]
[UTCTime "23:00:14"]
[WhiteElo "1711"]
[BlackElo "2035"]
[WhiteRatingDiff "-4"]
[BlackRatingDiff "+3"]
[ECO "A43"]
[Opening "Old Benoni Defense"]
[TimeControl "60+0"]
[Termination "Time forfeit"]	
1. d4 c5 2. e3 cxd4 3. exd4 d5 4. c3 Nc6 5. f4 e5 6. Nf3 e4 7. Ne5 f6 8. Qh5+ g6 9. Nxg6 hxg6 10. Qxh8 Kf7 11. Qh7+ Bg7 12. f5 g5 13. h4 gxh4 14. Bh6 Qf8 15. Rxh4 Nxh6 16. Rxh6 Ne7 17. Rh3 Bxf5 18. Qh4 Bxh3 19. Qxh3 Qh8 20. Qd7 Qh4+ 21. Kd2 Bh6+ 22. Kc2 Qf2+ 23. Nd2 Qxd2+ 24. Kb3 e3 0-1
"""

def get_quote(line: str):
    return re.findall('"([^"]*)"', line)

def get_moves(moves: str):
    movelist = moves.split(' ')
    white_move_list = []
    black_move_list = []

    count = 0
    for move in movelist:
        if count == 1:
            white_move_list.append(move)
        elif count == 2:
            black_move_list.append(move)

        count += 1
        if count == 3:
            count = 0
    print(white_move_list)
    print(black_move_list)

def get_info(game : str):
    game_info = game.splitlines()
    event = get_quote(game_info[1])
    Site  = get_quote(game_info[2])
    White = get_quote(game_info[3])
    Black = get_quote(game_info[4])
    Result = get_quote(game_info[5])
    UTCDate = get_quote(game_info[6])
    UTCTime = get_quote(game_info[7])
    WhiteElo = get_quote(game_info[8])
    BlackElo = get_quote(game_info[9])
    WhiteRatingDiff = get_quote(game_info[10])
    BlackRatingDiff = get_quote(game_info[11])
    ECO = get_quote(game_info[12])
    Opening = get_quote(game_info[13])
    InitialTime = get_quote(game_info[14]).split('+')[0]
    Increment = get_quote(game_info[14]).split('+')[1]
    Termination = get_quote(game_info[15])


    print(event)
    print(Site)
    print(White)
    print(Black)
    print(Result)
    print(UTCDate)
    print(UTCTime)
    print(WhiteElo)
    print(BlackElo)
    print(WhiteRatingDiff)
    print(BlackRatingDiff)
    print(ECO)
    print(Opening)
    print(InitialTime)
    print(Increment)
    print(Termination)


