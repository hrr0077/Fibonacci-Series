#bin/python3

print('HELLO, Wellcome to My programm, This code is use to print the fabonachi Sequnce')

def fabonachi(value):
    first = 0
    secound = 1
    print("0\n1")
    for x in range(value):
        term = first + secound
        first = secound
        secound = term
        print(term)

fabonachi(int(input("Enter the Number of terms to Print Fabonachi ")))