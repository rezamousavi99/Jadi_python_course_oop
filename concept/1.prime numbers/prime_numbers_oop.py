# print prime numbers(OOP)

class PrintPrime:
    def __init__(self) -> None:
        self.prime_sum = 0
        self.last_prime_number = 0
    
    def is_prime(self,n):
        self.prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                self.prime = False
                break
        return self.prime

    # user can determine pass priod numbers as parameter to see prime numbers
    def print_prime_numbers(self, start=1, end=10000):
        self.prime_sum = 0
        print(40 * '*')
        for i in range(start, end + 1):
            if self.is_prime(i):
                self.prime_sum += 1
                self.last_prime_number = i
                print(i, end=' ')
        print()
        print(40 * '*')
    
    # display sum and last prime
    def display(self):
        print(40 * '*')
        print(f'sum prime numbers ----> {self.prime_sum}\nlast prime numbers ----> {self.last_prime_number}')
        print(40 * '*')



    def __str__(self) -> str:
        return f'{self.__class__.__name__}'

    def __repr__(self) -> str:
        return f'{self.__class__.__name__}()'



def commands():
    print('<< prime program >>\n1. enter arbitrary period numbers\n2.display sum and last prime\n3.exit')

def main():


    p = PrintPrime()
    while True:
        commands()
            
        uinput = input('enter a command: ')
        match uinput:
            case '1':
                pinput = input('Enter arbitrary period numbers(use space to seperate numbers e.g. 1 100): ').split()

                first_para = int(pinput[0])
                seconde_para = int(pinput[1])

                p.print_prime_numbers(first_para, seconde_para)
            
            case '2':
                p.display()
            
            case '3':
                print('thanks🤍')
                break
            


if __name__ == '__main__':
    main()