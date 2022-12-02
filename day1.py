f = open("day1Input.txt", "r")
lines = f.read().splitlines()


#PART 1
max_calories = 0
current_elf_calories = 0
for line in lines:

    if line is "":
        max_calories = max(max_calories, current_elf_calories)
        current_elf_calories = 0
        continue

    calories = int(line)
    current_elf_calories += calories


print(max_calories)



#PART 2
# Guardar cuantas calorias tiene cada elf
# ordenar (sort) -> sumar el top 3

elf_calories = []
current_elf_calories = 0

for line in lines:
    if line is "":
        elf_calories.append(current_elf_calories)
        current_elf_calories = 0
        continue
    current_elf_calories += int(line)

elf_calories.sort()
elf_calories.reverse()

print(elf_calories)
print(elf_calories[0] +elf_calories[1] + elf_calories[2]   )












