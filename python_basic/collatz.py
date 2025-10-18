number = int(input('Input a number: '))

def collatz(number):
    print(number)
    while number != 1:
        try:
            if number %2 == 0: # if even
                number//=2
                print(number)
            elif number %2 != 0:
                number*=3
                number+=1
                print(number)
            else:
                print(number)
        except Exception as e:
            print(e)
    
collatz(number)