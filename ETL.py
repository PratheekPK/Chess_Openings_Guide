import re
import pandas as pd


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
    value = re.findall('"([^"]*)"', line)


def get_info(game : str):
    game_info = game.splitlines()
    event = get_quote(game_info[1])
    print(event)

get_info(test_game)
