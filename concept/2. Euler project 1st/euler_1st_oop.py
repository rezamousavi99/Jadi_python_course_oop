class Multiple3or5:
    def __init__(self) -> None:
        self.msum = 0

    def is_multiple3or5(self, n):
        if (n % 3 == 0) or (n % 5 == 0):
            return True
        return False

    def calculate_multiple3or5(self, start=1, end=1000):
        for i in range(start, end):
            if self.is_multiple3or5(i):
                self.msum += i
        return self.msum

def main():
    m = Multiple3or5()

    # you can also pass arbitrary period number as arguman
    print(m.calculate_multiple3or5())

if __name__ == '__main__':
    main()