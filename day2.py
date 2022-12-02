


from typing import List


def isWin_A(A: str , B:str):
    if A == B:
        return False
    if  A == "Rock" and B == "Paper":
            return False
    if  A == "Paper" and B == "Scissors":
            return False
    if  A == "Scissors" and B == "Rock":
            return False
    return True



def score_Prob1(round:str):
    returned = 0
    elf_move = {"A": "Rock", "B": "Paper", "C":"Scissors"}[round.split(" ")[0]]
    player_move = {"X": "Rock", "Y": "Paper", "Z":"Scissors"}[round.split(" ")[1]]

    # Add shape score
    returned += {"Rock": 1, "Paper": 2, "Scissors":3}[player_move]

    if elf_move == player_move:
        returned += 3
    elif isWin_A(elf_move, player_move):
        returned += 0
    else: 
        returned += 6

    return returned



def GetMove(elf_move: str, status: str):
    if status is "Draw":
        return elf_move
    
    if status is "Win":
        return {"Rock": "Paper", "Paper":"Scissors", "Scissors":"Rock"}[elf_move]    
    return {"Rock": "Scissors", "Paper":"Rock", "Scissors":"Paper"}[elf_move]
    


def score_Prob2(round:str):
    returned = 0
    elf_move = {"A": "Rock", "B": "Paper", "C":"Scissors"}[round.split(" ")[0]]
    match_status = {"X": "Loose", "Y": "Draw", "Z":"Win"}[round.split(" ")[1]]

    returned += {"Loose": 0, "Draw": 3, "Win": 6} [match_status]
    returned += {"Rock": 1, "Paper": 2, "Scissors":3}[GetMove(elf_move, match_status)]
    return returned





f = open("day2input.txt", "r")
rounds = f.read().splitlines()

total_score = 0
for round in rounds:
    total_score += score_Prob1(round)
print(total_score)


total_score_problem2 = 0
for round in rounds:
    total_score_problem2 += score_Prob2(round)
print(total_score_problem2)

