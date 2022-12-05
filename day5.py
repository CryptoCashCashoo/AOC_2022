


from typing import List


def get_crates():
    """
            [H]     [W] [B]            
        [D] [B]     [L] [G] [N]        
    [P] [J] [T]     [M] [R] [D]        
    [V] [F] [V]     [F] [Z] [B]     [C]
    [Z] [V] [S]     [G] [H] [C] [Q] [R]
    [W] [W] [L] [J] [B] [V] [P] [B] [Z]
    [D] [S] [M] [S] [Z] [W] [J] [T] [G]
    [T] [L] [Z] [R] [C] [Q] [V] [P] [H]
    1   2   3   4   5   6   7   8   9 
    """

    returned = [
        [],
        ["T","D","W","Z","V","P"],
        ["L","S","W","V","F","J","D"],
        ["Z","M","L","S","V","T","B","H"],
        ["R","S","J"],
        ["C","Z","B","G","F","M","L","W"],
        ["Q","W","V","H","Z","R","G","B"],
        ["V","J","P","C","B","D","N"],
        ["P","T","B","Q"],
        ["H","G","Z","R","C"],
    ]

    return  returned



def apply_instruction_on_cratemover_9000(crates, instruccion:str):
    "move 3 from 2 to 9"
    crates_to_move, stack_from, stack_to = [int(s) for s in instruccion.split() if s.isdigit()]

    for _ in range(0, crates_to_move):
        box = crates[stack_from].pop()
        crates[stack_to].append(box)

def apply_instruction_on_cratemover_9001(crates:List[List[str]], instruccion:str):
    "move 3 from 2 to 9"
    crates_to_move, stack_from, stack_to = [int(s) for s in instruccion.split() if s.isdigit()]

    box_stack =  crates[stack_from][-crates_to_move:]
    del(crates[stack_from][-crates_to_move:])
    crates[stack_to].extend(box_stack)



if __name__ == "__main__":
    with open("day5InputInstructions.txt") as file:
        instructions = file.read().splitlines()
    

    crates = get_crates()
    for instruction in instructions:
        apply_instruction_on_cratemover_9000(crates, instruction)
    print([stack[len(stack)-1] for stack in crates[1:]])


    crates = get_crates()
    for instruction in instructions:
        apply_instruction_on_cratemover_9001(crates, instruction)
    print([stack[len(stack)-1] for stack in crates[1:]])


