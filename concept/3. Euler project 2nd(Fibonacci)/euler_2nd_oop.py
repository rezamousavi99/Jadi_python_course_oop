class Fibonacci:
    def __init__(self) -> None:
        self.first = 1
        self.second = 2
        self.last = 0
        self.fsum = 0
    
    def is_even(self, n):
        if n % 2 == 0:
            return True
        return False
    
    def sum_fib_even(self, loop=4000000):
        while self.first < loop:
            if self.is_even(self.first):
                self.fsum += self.first
            self.last = self.first + self.second
            self.first = self.second
            self.second = self.last

        return self.fsum

def main():

    f = Fibonacci()
    print(f.sum_fib_even())        

if __name__ == '__main__':
    main()