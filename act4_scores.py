students = int(input("Students: "))

total = 0
highest = 0

for i in range(1, students + 1):
    score = int(input("Score " + str(i) + ": "))

    total += score

    if score > highest:
        highest = score

average = total / students

print("Total:", total)
print("Avg:", format(average, ".2f"))
print("Highest:", highest)
