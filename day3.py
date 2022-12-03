


def value(item:str) -> int:
    # Devolver el valor del caracter (a:1,...,z:26, A:27,...Z:52)
    if item.isupper():
        return ord(item) - ord('A') + 27
    elif item.islower():
        return ord(item) - ord('a') + 1
    return 0

def get_duplicated_item(rucksack:str) -> str:
    # encontrar que caracter se repite entre la primera y la segunda mitad del ruckstac.
    first_compartment = set(rucksack[0:len(rucksack)//2])
    second_compartment = set(rucksack[len(rucksack)//2:])
    intersection_set = first_compartment.intersection(second_compartment)
    return intersection_set.pop()

def priority_value(rucksack:str):
    duplicatedItem = get_duplicated_item(rucksack)
    return value(duplicatedItem)

def badge_value(rucksack1, rucksack2, rucksack3):
    badge = set(rucksack1).intersection(set(rucksack2)).intersection(set(rucksack3))
    return value(badge.pop())

if __name__ == "__main__":

    with open("day3Input.txt") as file:
        rucksacks = file.read().splitlines()

    # problem1Solution = sum(priority_value(rucksack) for rucksack in rucksacks)
    # print(problem1Solution)

    iter_sacks = iter(rucksacks)
    print( sum(badge_value(a,b,c) for (a,b,c) in zip(iter_sacks, iter_sacks, iter_sacks)) )
    






