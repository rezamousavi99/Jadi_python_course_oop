from random import randrange

people = []
for i in range(0, 50):
    people.append(100)


# while (0 in people) == False:
for beshkan in range(0, 200):
    for person1 in range(0, 50):
        person2 = randrange(0, 50)

        # aviod giving money back to the same person
        while person1 == person2 or people[person2] == 0:
            person2 = randrange(0, 50)

        if people[person1] == 0:
            continue

        people[person1] -= 1
        people[person2] += 1

print(people)
