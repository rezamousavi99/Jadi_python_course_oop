class PinFinder:
    def __init__(self) -> None:
        pass

    def find_pin(self):
        for i in range(0, 100000):
            ramz = str(i).zfill(5)

            condition1 = int(ramz[2]) + int(ramz[4]) == 14
            condition2 = int(ramz[0]) == (2 * int(ramz[1])) - 1
            condition3 = int(ramz[3]) == int(ramz[1]) + 1
            condition4 = int(ramz[1]) + int(ramz[2]) == 10

            # convert items of tuple into int
            tuple_numbers = tuple(map(int, tuple(ramz)))
            condition5 = sum(tuple_numbers) == 30

            if condition1 and condition2 and condition3 and condition4 and condition5:
                return i

def main():
    p = PinFinder()
    print(p.find_pin())

if __name__ == '__main__':
    main()

    