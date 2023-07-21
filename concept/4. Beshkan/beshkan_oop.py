from random import randrange

class Beshkan:
    def __init__(self, people_number=50) -> None:
        self.people = []
        self.people_number = people_number
        self.person1 = 0
        self.person2 = 0

        # dedicate 100$ for each person
        for i in range(0, self.people_number):
            self.people.append(100)

    def beshkan(self, beshkan_number=200):
        for _ in range(0, beshkan_number):
            for self.person1 in range(0, self.people_number):
                self.person2 = randrange(0, self.people_number)

                # aviod giving money back to the same person
                while self.person1 == self.person2 or self.people[self.person2] == 0:
                    self.person2 = randrange(0, self.people_number)

                if self.people[self.person1] != 0:
                    self.people[self.person1] -= 1
                    self.people[self.person2] += 1
        return self.people

    def display_people(self):
        print(self.people)

def main():
    b = Beshkan()
    b.display_people()
    print(b.beshkan())


if __name__ == '__main__':
    main()