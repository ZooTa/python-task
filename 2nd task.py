def show_menu():
    print("Choose an operation\n[0] Check Pplindrom        [1] Check if Prime\n[99] Exit")

def is_prime(num):
    if num > 2 :
        for i in range(2,num):
            if (num % i) == 0:
                print(num , " is not a prime number")
                break
        else :
            print(num , " is a prime number")
    elif num == 2:
         print(num , " is a prime number")           
    else:
        print(num , " is not a prime number")  

def is_palindrome():
    if word == wordR :
       print("yes")
    else:
       print("no") 

while True :
    show_menu()
    x = int(input(''))
    if x == 0:
        word = input("Enter the word you want to check ")
        wordR = word[::-1]
        is_palindrome()
        print(" ")
    elif x == 1:
        is_prime(num = int(input('Enter the number ')))              
        print(" ")
    elif x == 99:
        break
    else:
        print("invalide number, please try again")
        print("")