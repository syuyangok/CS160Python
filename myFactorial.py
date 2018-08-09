
# recursion to calculate factorial n

def myFactorial (n):
    if n == 0:        
        return 1;
    else:        
        return n*myFactorial(n-1);

def main():
    n = eval(input ("Enter an int number for factorial:"));

    print(myFactorial(n));


main()
    
