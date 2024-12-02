numbers = [5, 5, 2, 2, 4, 3, 4]
uniques = []
for number in numbers:
    if number not in uniques:
        uniques.append(number)
print(uniques)
