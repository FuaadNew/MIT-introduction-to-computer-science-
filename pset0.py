


import pylab

def is_a_number(num):
    for c in num:
        if not ord('0') <= ord(c) <= ord('9'):
            return False
    return True

def main():
    X = input("Enter a number X: ")
    Y = input("Enter a number Y: ")
    
    if (not is_a_number(X) or not is_a_number(Y)):
        print("please actually choose two numbers")
        main()
    else:
        X,Y = int(X), int(Y)
        print("X**y =", X**Y)
        print("log(x) =",pylab.log2(X))
    
        
    
        
        


if __name__ == "__main__":
    main()