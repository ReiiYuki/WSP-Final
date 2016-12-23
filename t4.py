def stamp7(money) :
    stamp = [0,0]
    while money >= 40 :
        if money >= 120 :
            stamp[1] += 1
            money -= 120
        elif money >= 40 :
            stamp[0] +=1
            money -= 40
    return stamp

def memberCheck(id) :
    if id == '1234' :
        return "You are a member"
    return "You are not a member"

if __name__ == '__main__':

    id = input('Input ID : ')
    print (memberCheck(id))

    money = float(input('Input money : '))
    stamps = stamp7(money)
    print ('Stamp-1B = %d, Stamp-3B = %d'%(stamps[0],stamps[1]))
