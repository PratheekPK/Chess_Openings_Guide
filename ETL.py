import re
import pandas as pd

class game_data:
    
    def __init__(self, game_string):
        self.game_string = game_string
        self.game_info = game_string.splitlines()
        self.event = get_quote(self.game_info[2])
        self.Site  = get_quote(self.game_info[4])
        self.White = get_quote(self.game_info[10])
        self.Black = get_quote(self.game_info[12])
        self.Result = get_quote(self.game_info[14])
        self.UTCDate = get_quote(self.game_info[6])
# =============================================================================
#         self.UTCTime = get_quote(self.game_info[7])
# =============================================================================
        self.WhiteElo = get_quote(self.game_info[16])
        self.BlackElo = get_quote(self.game_info[18])
# =============================================================================
#         self.WhiteRatingDiff = get_quote(self.game_info[10])
#         self.BlackRatingDiff = get_quote(self.game_info[11])
# =============================================================================
        self.ECO = get_quote(self.game_info[20])
# =============================================================================
#         self.Opening = get_quote(self.game_info[13])
# =============================================================================
        
# =============================================================================
#         self.InitialTime = str(get_quote(self.game_info[14])).split('+')[0]
#         self.Increment = str(get_quote(self.game_info[14])).split('+')[1]
#         
# =============================================================================
# =============================================================================
#         self.Termination = get_quote(self.game_info[15])
# =============================================================================
        
    
    def get_info(self):
        
        print(self.event)
        print(self.Site)
        print(self.White)
        print(self.Black)
        print(self.Result)
        print(self.UTCDate)
        print(self.UTCTime)
        print(self.WhiteElo)
        print(self.BlackElo)
        print(self.WhiteRatingDiff)
        print(self.BlackRatingDiff)
        print(self.ECO)
        print(self.Opening)
        print(self.InitialTime)
        print(self.Increment)
        print(self.Termination)

def extraction():
    file = open(r"C:\Users\hp\Code\GitHub\Chess_Openings_Guide\carlsen.txt")
    lines = file.readlines()
    count = 0
    blank_line_count=0
    games_strings=["" for i in range(0,len(lines))]
    for i in range(0,len(lines)):
        if (len(lines[i])==1):
            blank_line_count+=1
        if((blank_line_count%2)==1):
            games_strings[blank_line_count//2]=games_strings[blank_line_count//2]+lines[i]
        else:
            games_strings[blank_line_count//2]=games_strings[blank_line_count//2]+lines[i]+'\n'
            
    while("" in games_strings):
        games_strings.remove("")
        
    file.close()
    return games_strings
    

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


if __name__=='__main__':
    
    main_games_strings=extraction()
    game_objects = []
    main_games_strings[0]="\n\n"+main_games_strings[0]
    for strings in main_games_strings:
        if ((len(strings))>2):
            game_objects.append(game_data(strings))
    
