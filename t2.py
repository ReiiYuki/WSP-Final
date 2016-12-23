def checknum(n) :
    if n%2 == 0 :
        return "Even"
    else :
        return "Odd"

if __name__ == '__main__' :
    n = int(input("Input n : "))
    print (checknum(n))
