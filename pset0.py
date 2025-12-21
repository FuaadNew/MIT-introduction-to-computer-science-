


import math

def is_a_number(num):
    return ord('0') <= ord(num) <= ord('9')

def main():
    X = input("Enter a number X: ")
    Y = input("Enter a number Y: ")
    
    if (not is_a_number(X) or not is_a_number(Y)):
        print("please actually choose two numbers")
        main()
    else:
        X,Y = int(X), int(Y)
        print(X**Y)
        print(math.log(X))
    
        
    
        
        


if __name__ == "__main__":
    main()