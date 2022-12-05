



def create_range(a:str):
    minim,maxim = a.split("-")
    return [i for i in range(int(minim), int(maxim)+1)]


def are_contained(pair:str, problem1:bool):
    a,b = pair.split(",")

    rangeA = set(create_range(a))
    rangeB = set(create_range(b))
    if problem1:
        return rangeA.issubset(rangeB) or rangeB.issubset(rangeA) 
    return len(rangeA.intersection(rangeB)) > 0
    




if __name__ == "__main__":
    with open("day4Input.txt") as file:
        pairs_assignements = file.read().splitlines()

    print(sum(are_contained(pair, True) for pair in pairs_assignements))
    print(sum(are_contained(pair, False) for pair in pairs_assignements))